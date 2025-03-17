from .formatter import cprint
import pyfiglet
import subprocess
import os
import sys
from icecream import install, ic
install()

ic.configureOutput(prefix='debug -> ')

class easymenu:
    ''' Create an EasyMenu with some options:\n
        name: Optional Name of the App/Menu to be displayed when printing the menu.\n
        print_ascii_title: Boolean that prints the ASCII title if enabled\n
        print_ascii_title_each_time: Boolean that prints the ASCII Title each time the menu items are printed\n
        title_font: The Pyfiglet font to use when printing the title. Defaults to "slant"\n
        author: Optional Value to be printed with the title.\n
        url: Optional Value to be printed with the title.\n
        url_label: Optional Value to mask the url with a custom value instead. Assumes url provided. May not work in all terminals.\n
        debug: Boolean that enables more debug messages if set to True.\n
        make_screen: Boolean that creates a new terminal screem for app output and then removes it when the app is finished.\n
        quit_item: Boolean that includes a Quit Menu option with a red color at the bottom of the menu if True.\n
        catch_errors: Boolean that runs the menu in a "try except" block to catch errors. Useful for debugging, bad for production...\n
    '''
    def __init__(self, name: str = None, print_ascii_title: bool = True, print_ascii_title_each_time: bool = False, title_font = "slant", author: str = None, url: str = None, url_label: str = None, debug: bool = False, make_screen: bool = True, quit_item: bool = True, catch_errors: bool = False):
        
        self.name = name
        self.print_ascii_title = print_ascii_title
        self.print_ascii_title_each_time = print_ascii_title_each_time
        self.author = author
        self.title_font = title_font
        self.url_label = url_label
        self.url = url
        self.debug = debug
        self.menu_items = []
        self.make_screen = make_screen
        self.screen_made = False
        self.quit_item = quit_item
        self.catch_errors = catch_errors
        
        # Use this to pass exit code when exiting app with the start() method. Without this, the exit function runs twice to escape try except finally
        self.exit_code = None
        
        ''' If debug is enabled, enable ic printing to screen '''
        if self.debug:
            ic.enable()
        else:
            ic.disable()
        
        ''' if create_screen is True, try to create a screen and set screen_made to True for tracking '''
        if self.make_screen:
            ic(self.make_screen)
            try:
                self.create_screen()
                self.screen_made = True
            except Exception as e:
                self.print_error(e)
                ic(e)
                
        
        ''' Debug Attributes if enabled '''
        ic(name, print_ascii_title, author, url, debug, make_screen, quit_item, catch_errors)
        
        ''' Add a default quit option with an order weight of 99 to make sure it is last, and a color of red IF TRUE'''
        if self.quit_item:
            self.add_menu_option(item_name="Quit", action=self.exit_app, item_key="q", order_weight=99, color=cprint.RED)
        
    @staticmethod
    def print_info(message):
        ''' Print a message in an Info Format\n Ex: [+] Message'''
        print(cprint.okblue(f"[+] {message}"))
    
    def print_debug(self, message):
        ''' Print a debug message if the self.debug is set to true\n Ex: [+][+] Message'''
        if self.debug:
            print(cprint.okblue(f"[+][+] {message}"))
    
    @staticmethod
    def print_error(message):
        ''' Print a message in an Error Format\n Ex: [-] Message'''
        print(cprint.fail(f"[-] {message}"))
    
    @staticmethod
    def print_success(message):
        ''' Print a message in a Success Format with a check mark\n Ex: [\u2713] Message'''
        print(cprint.ok(f"[\u2713] {message}"))
        
    def print_title(self, font, message):
        ''' Print a Title in large text using pyfiglet if enabled '''
        if self.print_ascii_title:
            f = pyfiglet.figlet_format(message, font=font)
            print(cprint.header(f))
        else:
            self.print_debug(f"Not printing ASCII Title because {self.print_ascii_title=}")

    @staticmethod
    def create_screen():
        ''' Create a new screen so output from the app is not present in the main termainal screen '''
        subprocess.run(["tput", "smcup"])
        
    @staticmethod
    def close_screen():
        ''' Close a created screen to return the app back to the normal terminal screen '''
        subprocess.run(["tput", "rmcup"])
    
    def add_menu_option(self, item_name: str, action, item_key: str = None, order_weight: int = None, color=cprint.ENDC):
        ''' Create a new menu item to be displayed:\n
            item_name: The name to be displayed as a menu item ex "Perform Action"\n
            action: A function to be run if an item is selected from the menu. If this is not a function, the value will be printed instead.\n
            item_key: Optional string to change the key that is displayed in the menu instead of the index. Instead of "1. Item" the number will be replaced with the item_key provided.\n
            order_weight: Optional Integer to change the order of a menu item in the printed menu. Default values are 5 for menu items with a custom item_key and 15 for an item without a key.\n
                        The goal is to have any special items ahead of normal items in the menu. Menu items with the same weight will be sorted.\n
            color: Optional ASCII color for the menu item or item from cprint ex: '\\033[91m'. Defaults to no color\n
        '''
        if isinstance(action, easymenu):  # If action is a submenu, set parent menu
            action.parent_menu = self  # Track parent menu
            action.add_menu_option("Back", lambda: None, item_key="b", order_weight=98, color=cprint.BG_GREEN)
            # if no color is provided, make background green to distinguish between sub menu and menu item
            if color == cprint.ENDC:
                color = cprint.BG_GREEN


        if item_key:
            if not order_weight: 
                order_weight = 15
            _entry = {'name': item_name, 'action': action, 'key': item_key, 'order_weight': order_weight, 'color': color}
            self.print_debug("Added menu item:")
            ic(_entry)
            self.menu_items.append(_entry)
            
        else:
            if not order_weight: 
                order_weight = 5
            _entry = {'name': item_name, 'action': action, 'order_weight': order_weight, 'color': color}
            self.print_debug("Added menu item:")
            ic(_entry)
            self.menu_items.append(_entry)
                        
    def sort_menu(self):
        ''' Sort the menu based on item weight before printing it '''
        sorted_list = sorted(self.menu_items, key=lambda d: d['order_weight'])
        ic(sorted_list)
        return sorted_list
    
    @staticmethod
    def create_link(uri, label=None):
        if label is None: 
            label = uri
        parameters = ''

        # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
        escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

        return escape_mask.format(parameters, uri, label)

    
    def __print_menu(self):
        ''' Main Function to print the menu and execute the actions'''
        sorted_menu = self.sort_menu() # Sort the Menu before printing
        
        self.first_time_run = True
        self.submenu_check = False
        
        # Print an ascii name if one is provided
        if self.name:
            self.print_title(font=self.title_font, message=f"{self.name}\n")
        
        if self.author:
            print(cprint.header(f"{cprint.ITALIC}Made by: {self.author}"))
        if self.url:
            link = self.create_link(self.url, self.url_label)
            print(cprint.header(f"{cprint.ITALIC}Visit: {link}"))
            
        print("\n")
                
        while True:
            index_counter = 1  # Reset for correct numbering before printing
            
            # print the ascii title if was just on a submenu and print again if this isnt the first time the menu was printed AND the option to print each time is true
            if self.submenu_check:
                self.print_title(font=self.title_font, message=f"{self.name}\n")
                self.submenu_check = False
            elif not self.first_time_run and self.print_ascii_title_each_time:
                self.print_title(font=self.title_font, message=f"{self.name}\n")
            elif self.first_time_run:
                self.first_time_run = False
            
            print(cprint.header(f"{cprint.BOLD}{cprint.UNDERLINE}{self.name}:"))
            
            success = False
            ''' Print the menu.
                If an item has an item_key, print that
                If it does not, print the index +1 because they start at 0
            '''
            for index, value in enumerate(sorted_menu):
                if value.get('key', None):
                    print(cprint.colored(f"{value['key']}. {value['name']}", value['color']))
                else:
                    #print(cprint.colored(f"{index+1}. {value['name']}", value['color']))
                    # If no key, print the correct index and increment counter
                    print(cprint.colored(f"{index_counter}. {value['name']}", value['color']))
                    index_counter += 1  # Only increment for items without a key

            choice = input("\nWhat option do you want?: ")
            if choice == '':
                choice = None
            else:
                self.print_debug(f"Choice: {choice}")
            print("\n")
            
            
            '''
            Logic to determine action based on selection:
                1. Check first if the input matches a defined key because this is "not the default" kind of match.
                2. Then check if the input matches the index of the item AND make sure the match does not have a key set. 
                    This makes sure a menu item can only be matched by the key if one is provided, rather than both a key and index
                    Example:
                    1. Option 1
                    s. Option S
                    
                    An input of 2 would match the index of "Option S" but fail the check because "Option S" has a key of "s" set. Thus, an input of 2 should not match anything.
                    An input of "s" would match "option S"
                    
                3. Once a match happens, Check if the action passed is callable (meaning it is a function) and run it if so. 
                    If it is not, print the value (and a debug message if enabled)
                4. If no match, print an error message
                
            '''
            index_counter = 1 # Reset before matching input
            for index, value in enumerate(sorted_menu):
                if value.get('key', "") == choice:
                    self.print_debug("Match on key")
                    ic(choice)
                    ic(value)
                    self.print_info(f"Item Selected: {value['name']}\n")
                    
                    if isinstance(value['action'], easymenu):  # If the action is a submenu
                        self.submenu_check = True
                        value['action'].start()  # Start the submenu
                    elif value['name'] == "Back":  # If "Back" is selected, just return
                        return  
                    
                    elif callable(value['action']):
                        value['action']()
                        print("\n\n")
                        
                    else:
                        self.print_success(value['action'])
                        print("\n\n")
                    success = True
                    break
                
                #elif str(index+1) == choice:
                elif str(index_counter) == choice:
                    if not value.get('key', False):
                        self.print_debug("\t[+] Match on index")
                        self.print_info(f"Item Selected: {value['name']}\n")
                        ic(choice)
                        ic(value)
                        if callable(value['action']):
                            value['action']()
                            print("\n\n")
                        else:
                            self.print_debug(f"Action {value['action']} is not a function")
                            self.print_success(value['action'])
                            print("\n\n")
                        success = True
                        break
                if not value.get('key', None):  # Only increment index counter for non-key items
                    index_counter += 1
            if not success:
                self.print_error("Invalid Choice")
                print("\n\n")

    @staticmethod
    def clear_screen():
        ''' Clear the Screen in a way that will work regardless of OS '''
        os.system('cls' if os.name == 'nt' else 'clear')

    def exit_app(self, code=0):
        ''' Exit the app gracefully and close a screen if one is open '''
        self.print_success("Exiting Gracefully...")
        if self.screen_made and self.make_screen:
            ic(self.make_screen)
            ic(self.screen_made)
            try:
                self.close_screen()
                self.print_success(f"{self.name} Exited Successfully!")
            except Exception as e:
                self.print_error(e)
                ic(e)        
        else:
            self.print_success(f"{self.name} Exited Successfully!")
        self.exit_code = code
        sys.exit(code)
        
    @staticmethod
    def print_menu():
        print(cprint.fail("This method is deprecated. use the 'start' method instead.\nExiting..."))
        sys.exit(1)
        
    def start(self):
        ''' Start the app and continue on errors. Also exits 'cleaner' / handles ctrl+c if a screen is created. '''
        if self.catch_errors:
            self.print_debug("Catching all errors, you can disable this message by setting debug=False")
            try:
                self.__print_menu()
            except Exception as e:
                self.print_error(f"Error: {e}")
            finally:
                if self.exit_code is not None:  # Only exit if exit_code is explicitly set
                    sys.exit(self.exit_code)
        else:
            self.__print_menu()
