# EasyMenu3

# EasyMenu3

EasyMenu3 is a Python-based interactive menu system that allows users to create customizable command-line menus with ease. It provides a structured way to display options, handle user input, and execute actions, making it useful for CLI-based applications.

Available at https://pypi.org/project/easymenu3

[Screenshot](https://github.com/pitterpatter22/EasyMenu3/blob/main/example.png)

[Example](https://github.com/pitterpatter22/EasyMenu3/blob/main/example.py)

## New Version 0.3.1
- Added `print_table` function
- Adjusted formatting.
- tidied up a bit

## New Version 0.3.0
- Added support for submenus.
- Simplified entry point for app (`start()`) and added options to trap errors instead of using a seperate method.
- Adjusted formatting.

## Features
- Customizable menu title, author, and URL display
- ASCII art title generation using `pyfiglet`
- Automatic debug message handling with `icecream`
- Screen handling for clean terminal output
- Color-coded menu options using included formatter `colors`
- Easily print a table using `print_table`
  - Prints a table based on the provided data with optional sorting, theming, and header formatting.
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
from EasyMenu3 import easymenu, print_table, colors

def example_table():
    # Example Table usage:
    data = [
        ["Alice", 30, "Engineer"],
        ["Bob", 25, "Designer"],
        ["Charlie", 35, "Teacher"]
    ]
    headers = ["Name", "Age", "Occupation"]

    print("Default theme, sorted by Age (ascending):")
    print_table(data, headers, sort_by="Age", ascending=True, theme="default", header_style=colors.BG_BLUE)
    
# Create main menu
main_menu = easymenu(name="Main Menu", author="Joe Schmo", url="https://github.com/pitterpatter22/EasyMenu3/tree/main", url_label="EasyMenu3")

# Create a submenu
sub_menu = easymenu(name="Sub Menu")
sub_menu.add_menu_option("Sub Option 1", lambda: print("Sub Option 1 Selected"), item_key="1")
sub_menu.add_menu_option("Sub Option 2", lambda: print("Sub Option 2 Selected"), item_key="2")


main_menu.add_menu_option(item_name="Option 1", action=lambda: print("Main Option 1 Selected"))
main_menu.add_menu_option(item_name="Option 2", action=example_table)

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
- `color`: Optional ASCII color for the menu item or item from `colors` 
    - ex: `\\033[91m` or `colors.ENDC`
    - Defaults to no color


## Class: `colors`:
A utility class for ANSI terminal text formatting.

This class provides various ANSI escape codes as class attributes to format text with different
colors, styles (bold, underline, italic, etc.), and background colors in terminal outputs.
In addition to the color codes, it includes static methods that wrap messages in these codes,
making it easy to output colored and styled text in command-line applications.

### Methods:
- `colored(message, color)`: Wraps the given message with the specified ANSI color code and resets the formatting afterward.
    - Usage example: `print(colors.colored("Hello, world!", colors.OKBLUE))`
- `warning(message)`: Returns the message formatted in yellow to indicate a warning or caution.
    - Usage example: `print(colors.warning("Be careful!"))`
- `fail(message)`: Returns the message formatted in red to denote an error or failure. It can also be used with sys.exit() for terminating the program.
    - Usage example: `print(colors.fail("Operation failed."))`
- `ok(message)`: Returns the message formatted in green, typically used to indicate success or a positive outcome.
    - Usage example: `print(colors.ok("Operation successful."))`
- `okblue(message)`: Returns the message formatted in blue for informational output.
    - Usage example: `print(colors.okblue("Information message."))`
- `header(message)`: Returns the message formatted in a header (purple-ish) style, suitable for emphasizing titles or section headings.
    - Usage example: `print(colors.header("Section Header"))`


## Function: `print_table`:
A utility function that prints a table based on the provided data with optional sorting, theming, 
and header formatting.

### Parameters
- `data` (list of lists): The table data, where each sublist is a row.
- `headers` (list, optional): List of header labels for the columns.
- `sort_by` (int or str, optional): Column index or header name to sort by.
- `ascending` (bool, optional): True for ascending order, False for descending.
- `theme` (str, optional): Table theme to use. Options:
    - `"default"`: Simple table with header separator.
    - `"bordered"`: Entire table enclosed in a border with lines after each row.
- `header_style` (str, optional): ANSI escape code for styling the header row)


## Example Menu Output
```
    __  ___      _          __  ___                
   /  |/  /___ _(_)___     /  |/  /__  ____  __  __
  / /|_/ / __ `/ / __ \   / /|_/ / _ \/ __ \/ / / /
 / /  / / /_/ / / / / /  / /  / /  __/ / / / /_/ / 
/_/  /_/\__,_/_/_/ /_/  /_/  /_/\___/_/ /_/\__,_/  

Made by: Joe Schmo
Visit: [My Site](https://github.com/pitterpatter22/EasyMenu3)

Main Menu:
1. Option 1
2. Option 2
s. Go to Submenu
q. Quit


What option do you want?: 2


[+] Item Selected: Option 2

Default theme, sorted by Age (ascending):
 Name   | Age | Occupation
--------+-----+-----------
Bob     | 25  | Designer  
Alice   | 30  | Engineer  
Charlie | 35  | Teacher 

What option do you want?: q

[✓] Main Menu Exited Successfully!

```

## License
This project is licensed under the MIT License.

