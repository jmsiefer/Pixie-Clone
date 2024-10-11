# PixieClone

A simple and lightweight color picker and analyzer built with Python using the `tkinter` library. PixieClone allows you to pick colors from your screen, display RGB, HEX, CMYK, HSV values, and find approximate Pantone-like colors. It also includes a magnifier tool and hotkeys for quick actions.

## Features

- Real-time color detection from your screen.
- Displays the following color information:
  - HEX value
  - RGB values
  - CMYK values
  - HSV values
  - Approximate Pantone-like colors.
- Copy HEX color code to the clipboard with a hotkey.
- Built-in color mixer for choosing custom colors.
- Magnifier tool for pixel-level color selection.
- Simple and intuitive UI with minimal design.

## Hotkeys

- **Ctrl+Alt+C**: Copy the current color's HEX code to the clipboard.
- **Ctrl+Alt+X**: Open the color mixer.
- **Ctrl+Alt+Z**: Open the magnifier window for precise color selection.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/PixieClone.git
    cd PixieClone
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:
    ```bash
    python PixieClone.py
    ```

## Dependencies

- `tkinter`: For building the user interface.
- `pyautogui`: To capture the screen position.
- `PIL` (Pillow): To capture and manipulate images.
- `pyperclip`: To copy the HEX color code to the clipboard.
- `colorsys`: For HSV conversion.

You can install the dependencies with:
```bash
pip install pyautogui Pillow pyperclip

## How to Use

1. Launch the application.
2. Hover over any part of your screen to automatically detect the color.
3. Use the hotkeys for quick actions:
   - Copy the HEX value with `Ctrl+Alt+C`.
   - Use the color mixer with `Ctrl+Alt+X` to pick a new color.
   - Open the magnifier with `Ctrl+Alt+Z` for precise color selection.
4. The application will continuously update the color information displayed.

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

