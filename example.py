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