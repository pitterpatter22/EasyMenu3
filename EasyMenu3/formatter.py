class cprint:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    RED       = '\033[91m'
    FAIL      = '\033[91m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC    = '\033[3m'
    CYAN      = '\033[96m'  # Light Cyan
    LIGHTGRAY = '\033[37m'  # Light Gray
    DARKGRAY  = '\033[90m'  # Dark Gray
    YELLOW    = '\033[33m'  # Yellow
    MAGENTA   = '\033[35m'  # Magenta
    WHITE     = '\033[97m'  # Bright White

    DIM        = '\033[2m'   # Dim text
    BLINK      = '\033[5m'   # Blinking text (might not work in all terminals)
    REVERSE    = '\033[7m'   # Invert colors (swap foreground & background)
    HIDDEN     = '\033[8m'   # Hidden text (useful for passwords)
    STRIKETHROUGH = '\033[9m'  # Strikethrough text
    
    BG_BLACK   = '\033[40m'
    BG_RED     = '\033[41m'
    BG_GREEN   = '\033[42m'
    BG_YELLOW  = '\033[43m'
    BG_BLUE    = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN    = '\033[46m'
    BG_WHITE   = '\033[47m'
    
    ENDC      = '\033[0m'

    # Method that returns a message with the desired color
    # usage:
    #    print(cprint.colored("My colored message", cprint.OKBLUE))
    @staticmethod
    def colored(message, color):
      return color + message + cprint.ENDC

    # Method that returns a yellow warning
    # usage:
    #   print(cprint.warning("What you are about to do is potentially dangerous. Continue?"))
    @staticmethod
    def warning(message):
      return cprint.WARNING + message + cprint.ENDC

    # Method that returns a red fail
    # usage:
    #   print(cprint.fail("What you did just failed massively. Bummer"))
    #   or:
    #   sys.exit(cprint.fail("Not a valid date"))
    @staticmethod
    def fail(message):
      return cprint.FAIL + message + cprint.ENDC

    # Method that returns a green ok
    # usage:
    #   print(cprint.ok("What you did just ok-ed massively. Yay!"))
    @staticmethod
    def ok(message):
      return cprint.OKGREEN + message + cprint.ENDC

    # Method that returns a blue ok
    # usage:
    #   print(cprint.okblue("What you did just ok-ed into the blue. Wow!"))
    @staticmethod
    def okblue(message):
      return cprint.OKBLUE + message + cprint.ENDC

    # Method that returns a header in some purple-ish color
    # usage:
    #   print(cprint.header("This is great"))
    @staticmethod
    def header(message):
      return cprint.HEADER + message + cprint.ENDC