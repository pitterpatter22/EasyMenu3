from EasyMenu3 import easymenu

def example_function():
    print("This is a function")


# Create main menu
main_menu = easymenu(name="Main Menu", author="Joe Schmo", url="https://github.com/pitterpatter22/EasyMenu3/tree/main", url_label="EasyMenu3")

# Create a submenu
sub_menu = easymenu(name="Sub Menu")
sub_menu.add_menu_option("Sub Option 1", lambda: print("Sub Option 1 Selected"), item_key="1")
sub_menu.add_menu_option("Sub Option 2", action=example_function, item_key="2")


main_menu.add_menu_option(item_name="Option 1", action=lambda: print("Main Option 1 Selected"))
main_menu.add_menu_option(item_name="Option 2", action=lambda: print("Main Option 2 Selected"))

# Add submenu to main menu
main_menu.add_menu_option("Go to Submenu", sub_menu, item_key="s")


# Start the main menu
main_menu.start()