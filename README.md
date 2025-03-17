# EasyMenu3

# EasyMenu3

EasyMenu3 is a Python-based interactive menu system that allows users to create customizable command-line menus with ease. It provides a structured way to display options, handle user input, and execute actions, making it useful for CLI-based applications.

Available at https://pypi.org/project/easymenu3

[Screenshot](https://github.com/pitterpatter22/EasyMenu3/blob/main/example.png)

[Example](https://github.com/pitterpatter22/EasyMenu3/blob/main/example.py)

## New Version 0.3.0
- Added support for submenus.
- Simplified entry point for app (`start()`) and added options to trap errors instead of using a seperate method.
- Adjusted formatting.

## Features
- Customizable menu title, author, and URL display
- ASCII art title generation using `pyfiglet`
- Automatic debug message handling with `icecream`
- Screen handling for clean terminal output
- Color-coded menu options using a formatter `cprint`
- Customizable menu item ordering and shortcut keys
- Supports both function-based and static value-based actions

## Installation
To use EasyMenu3, ensure you have Python installed along with the required dependencies:

```bash
pip install pyfiglet icecream easymenu3
```

## Usage
Import `easymenu` and create an instance:

```python
from EasyMenu3 import easymenu


# Create main menu
main_menu = easymenu(name="Main Menu", author="Joe Schmo", url="https://github.com/pitterpatter22/EasyMenu3/tree/main", url_label="EasyMenu3")

# Create a submenu
sub_menu = easymenu(name="Sub Menu")
sub_menu.add_menu_option("Sub Option 1", lambda: print("Sub Option 1 Selected"), item_key="1")
sub_menu.add_menu_option("Sub Option 2", lambda: print("Sub Option 2 Selected"), item_key="2")


main_menu.add_menu_option(item_name="Option 1", action=lambda: print("Main Option 1 Selected"))
main_menu.add_menu_option(item_name="Option 2", action=lambda: print("Main Option 2 Selected"))

# Add submenu to main menu
main_menu.add_menu_option("Go to Submenu", sub_menu, item_key="s")


# Start the main menu
main_menu.start()
```

## Class: `easymenu`
### Constructor Parameters:
- `name` (str): Optional menu title.
- `title_font` (str): Font used for the ASCII title (default: "slant").
- `print_ascii_title`: Boolean that prints the ASCII title if enabled.
- `print_ascii_title_each_time`: Boolean that prints the ASCII Title each time the menu items are printed.
- `author` (str): Author name.
- `url` (str): URL displayed in the menu.
- `url_label` (str): Custom label for the URL.
- `debug` (bool): Enable debug messages.
- `make_screen` (bool): Create a separate terminal screen.
- `quit_item` (bool): Include a quit option automatically.
- `catch_errors`: Boolean that runs the menu in a "try except" block to catch errors. Useful for debugging, bad for production...

### Methods:
- `add_menu_option(item_name, action, item_key=None, order_weight=None, color=None)`: Adds a new menu item.
- `__print_menu()`: Displays the menu and handles user input. Newly a private method.
- `start()`: Start the app and continue on errors. Also exits 'cleaner' / handles ctrl+c if a screen is created.
- `clear_screen()`: Clears the terminal screen.
- `exit_app()`: Gracefully exits the menu system.
- `print_menu()`: A placeholder that indicates this method has been depricated and that `start()` should be used instead.

### Adding a Menu Option:
Create a new menu item to be displayed:
- `item_name`: The name to be displayed as a menu item ex: `Do Action`
- `action`: A function to be run if an item is selected from the menu. 
    - If this is not a function, the value will be printed instead.
    - *** NEW *** If action is a submenu, set parent menu for tracking
    - *** NEW *** This allows the use of submenus
- `item_key`: Optional string to change the key that is displayed in the menu instead of the index. 
    - Instead of `1. Item` the number will be replaced with the `item_key` provided `c. Item`
- `order_weight`: Optional Integer to change the order of a menu item in the printed menu. 
    - Default values are `5` for menu items with a custom `item_key` and `15` for an item without an `item_key`.
    - The goal is to have any special items ahead of normal items in the menu. 
    - Menu items with the same weight will be sorted.
- `color`: Optional ASCII color for the menu item or item from cprint 
    - ex: `\\033[91m`
    - Defaults to no color


## Example Menu Output
```
    __  ___         ______           __                     ___              
   /  |/  /_  __   / ____/_  _______/ /_____  ____ ___     /   |  ____  ____ 
  / /|_/ / / / /  / /   / / / / ___/ __/ __ \/ __ `__ \   / /| | / __ \/ __ \
 / /  / / /_/ /  / /___/ /_/ (__  ) /_/ /_/ / / / / / /  / ___ |/ /_/ / /_/ /
/_/  /_/\__, /   \____/\__,_/____/\__/\____/_/ /_/ /_/  /_/  |_/ .___/ .___/ 
       /____/                                                 /_/   /_/      

Made by: Joe Schmo
Visit: [My Site](https://github.com/pitterpatter22/EasyMenu3)

Menu:
c. Custom Option
2. Option 1
3. Option 2
q. Quit


What option do you want?:
```

## Building

```
python3 setup.py sdist bdist_wheel

twine upload dist/*
```

## License
This project is licensed under the MIT License.

