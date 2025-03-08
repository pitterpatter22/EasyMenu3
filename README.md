# EasyMenu3

# EasyMenu3

EasyMenu3 is a Python-based interactive menu system that allows users to create customizable command-line menus with ease. It provides a structured way to display options, handle user input, and execute actions, making it useful for CLI-based applications.

Available at https://pypi.org/project/easymenu3

[Screenshot](example.png)

[Example](example.py)

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
pip install easymenu3
```

## Usage
Import `easymenu` and create an instance:

```python
from EasyMenu3 import easymenu
def example1():
    app.print_success("example1 ran")
def example2():
    app.print_error("example2 ran")
    
def custom():
    app.print_info("Custom Option")
    input("Press enter to kill this!!!")
    app.exit_app()

app = easymenu(name="My Custom App", author="Joe Schmo", url="https://github.com", url_label="My Site")
app.add_menu_option(item_name="Option 1", action=example1)
app.add_menu_option(item_name="Option 2", action=example2)
app.add_menu_option(item_name="Custom Option", action=custom, item_key="c", order_weight=1, color='\033[92m')

app.start()
# or 
#app.print_menu()
```

## Class: `easymenu`
### Constructor Parameters:
- `name` (str): Optional menu title.
- `title_font` (str): Font used for the ASCII title (default: "slant").
- `author` (str): Author name.
- `url` (str): URL displayed in the menu.
- `url_label` (str): Custom label for the URL.
- `debug` (bool): Enable debug messages.
- `make_screen` (bool): Create a separate terminal screen.
- `quit_item` (bool): Include a quit option automatically.

### Methods:
- `add_menu_option(item_name, action, item_key=None, order_weight=None, color=None)`: Adds a new menu item.
- `print_menu()`: Displays the menu and handles user input.
- `start()`: Start the app and continue on errors. Also exits 'cleaner' / handles ctrl+c if a screen is created.
- `clear_screen()`: Clears the terminal screen.
- `exit_app()`: Gracefully exits the menu system.

### Adding a Menu Option:
Create a new menu item to be displayed:
- `item_name`: The name to be displayed as a menu item ex: `Do Action`
- `action`: A function to be run if an item is selected from the menu. 
    - If this is not a function, the value will be printed instead.
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
Visit: [My Site](https://github.com)

Menu:
c. Custom Option
2. Option 1
3. Option 2
q. Quit


What option do you want?:
```

## License
This project is licensed under the MIT License.

