import tkinter as tk
from tkinter.colorchooser import askcolor
import pyautogui
from PIL import ImageGrab, ImageTk, Image
import colorsys
import pyperclip
from math import sqrt

# Predefined Pantone-like colors with hex values for approximation
pantone_colors = {
    "Pantone Black C": (0, 0, 0),
    "Pantone White": (255, 255, 255),
    "Pantone 185 C": (228, 0, 43),
    "Pantone 354 C": (0, 166, 81),
    "Pantone 2935 C": (0, 61, 165),
    "Pantone 7409 C": (223, 181, 66),
}

# Function to calculate color distance for RGB values
def color_distance(c1, c2):
    return sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))

# Function to convert RGB to CMYK
def rgb_to_cmyk(r, g, b):
    if (r, g, b) == (0, 0, 0):
        return 0, 0, 0, 100
    c = 1 - r / 255
    m = 1 - g / 255
    y = 1 - b / 255
    min_cmy = min(c, m, y)
    c = (c - min_cmy) / (1 - min_cmy)
    m = (m - min_cmy) / (1 - min_cmy)
    y = (y - min_cmy) / (1 - min_cmy)
    k = min_cmy
    return int(c * 100), int(m * 100), int(y * 100), int(k * 100)

# Function to convert RGB to closest Pantone-like color
def rgb_to_pantone(r, g, b):
    closest_color_name = min(pantone_colors, key=lambda name: color_distance(pantone_colors[name], (r, g, b)))
    return f"{closest_color_name} (Approximate)"

# Function to copy HTML color to clipboard
def copy_html_color():
    pyperclip.copy(hex_var.get().replace("HEX: ", ""))
    print(f"Copied to clipboard: {hex_var.get()}")

# Function to open color mixer and allow user to pick a color
def color_mixer():
    color = askcolor()[1]  # Get the hex color
    if color:
        pyperclip.copy(color)  # Copy the selected color to the clipboard
        print(f"Copied to clipboard: {color}")

# Function to create a live magnifier of the current pixel area
def magnifier():
    magnifier_win = tk.Toplevel(root)
    magnifier_win.title("Magnifier")
    magnifier_win.geometry("200x200")
    
    def update_magnifier():
        x, y = pyautogui.position()
        img = ImageGrab.grab(bbox=(x - 25, y - 25, x + 25, y + 25))
        img = img.resize((200, 200))  # Resize for magnification
        img_tk = ImageTk.PhotoImage(img)
        magnifier_label.config(image=img_tk)
        magnifier_label.image = img_tk
        magnifier_win.after(50, update_magnifier)

    magnifier_label = tk.Label(magnifier_win)
    magnifier_label.pack()
    update_magnifier()

# Function to hide color info and show hotkey info
def show_hotkeys():
    for widget in color_widgets:
        widget.grid_remove()
    color_preview.grid_remove()
    hotkey_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

# Function to hide hotkey info and show color info
def hide_hotkeys():
    hotkey_label.grid_remove()
    for widget in color_widgets:
        widget.grid()
    color_preview.grid(row=0, column=0, rowspan=1, columnspan=1)

# Function to check if the mouse is inside the window
def check_mouse_position(event=None):
    widget = root.winfo_containing(root.winfo_pointerx(), root.winfo_pointery())
    if widget is None or widget.winfo_toplevel() != root:  # Mouse is outside the main window
        hide_hotkeys()
    else:  # Mouse is inside the main window
        show_hotkeys()

# Function to update the color values and the color preview
def update_color():
    x, y = pyautogui.position()
    img = ImageGrab.grab(bbox=(x, y, x+1, y+1))
    pixel_color = img.getpixel((0, 0))
    r, g, b = pixel_color

    tolerance = 15
    if r <= tolerance and g <= tolerance and b <= tolerance:
        r, g, b = 0, 0, 0

    hex_color = f"#{r:02x}{g:02x}{b:02x}".upper()
    pantone_color = rgb_to_pantone(r, g, b)

    hsv = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    hsv = (int(hsv[0] * 360), int(hsv[1] * 100), int(hsv[2] * 100))
    cmyk = rgb_to_cmyk(r, g, b)

    hex_var.set(f"HEX: {hex_color}")
    pixel_var.set(f"[{x},{y}]")
    rgb_var.set(f"RGB: ({r},{g},{b})")
    cmyk_var.set(f"CMYK: {cmyk}")
    hsv_var.set(f"HSV: {hsv}")
    pantone_var.set(f"Pantone: {pantone_color}")

    color_preview.config(bg=hex_color)

    root.after(100, update_color)

# Create the main window
root = tk.Tk()
root.title("Pixie - Color Picker")
root.geometry("200x160")
root.resizable(False, False)

# Create the variables to store color values
pixel_var = tk.StringVar()
hex_var = tk.StringVar()
rgb_var = tk.StringVar()
cmyk_var = tk.StringVar()
hsv_var = tk.StringVar()
pantone_var = tk.StringVar()

# Set a very small font and ensure tight line spacing
small_font = ("Arial", 8)

# Add a color preview box where the red box is (top-left corner)
color_preview = tk.Label(root, width=5, height=3, bg="#FFFFFF")
color_preview.grid(row=0, column=0, rowspan=1, padx=2, pady=0, sticky="nw")

# Add screen coordinates label where the blue box is (below color preview)
pixel_label = tk.Label(root, textvariable=pixel_var, font=small_font)
pixel_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=2, pady=0)

# Create and place the other labels in the window
hex_label = tk.Label(root, textvariable=hex_var, font=small_font)
rgb_label = tk.Label(root, textvariable=rgb_var, font=small_font)
cmyk_label = tk.Label(root, textvariable=cmyk_var, font=small_font)
hsv_label = tk.Label(root, textvariable=hsv_var, font=small_font)
pantone_label = tk.Label(root, textvariable=pantone_var, font=small_font)

color_widgets = [hex_label, rgb_label, cmyk_label, hsv_label, pantone_label]

# Grid the labels with minimal padding
for i, widget in enumerate(color_widgets):
    widget.grid(row=i+2, column=0, columnspan=2, sticky="w", padx=2, pady=0)

# Create the hotkey info label
hotkey_label = tk.Label(root, text="HOTKEYS:\nCtrl+Alt+C: Copy HTML\nCtrl+Alt+X: Color Mixer\nCtrl+Alt+Z: Magnifier", 
                        font=("Arial", 8), bg="white", relief="solid", bd=1)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
hotkey_label.grid_remove()  # Start hidden

# Bind the hotkeys to the corresponding functions
root.bind("<Control-Alt-c>", lambda event: copy_html_color())
root.bind("<Control-Alt-x>", lambda event: color_mixer())
root.bind("<Control-Alt-z>", lambda event: magnifier())

# Use a loop to continuously check mouse position
root.bind_all('<Motion>', check_mouse_position)

# Start the color update loop
update_color()

# Start the Tkinter main loop
root.mainloop()
