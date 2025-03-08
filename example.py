from EasyMenu3 import easymenu
def example1():
    app.print_success("example1 ran")
def example2():
    app.print_error("example2 ran")
    
def custom():
    app.print_info("Custom Option")
    input("Press enter to kill this!!!")
    app.exit_app()

# With optional attributes
app = easymenu(name="My Custom App", author="Joe Schmo", url="https://github.com", url_label="My Site", quit_item=True, debug=False, make_screen=True)

# Most Basic
#app = easymenu()

app.add_menu_option(item_name="Option 1", action=example1)
app.add_menu_option(item_name="Option 2", action=example2)
app.add_menu_option(item_name="Custom Option", action=custom, item_key="c", order_weight=1, color='\033[92m')

#app.print_menu()
app.start()
