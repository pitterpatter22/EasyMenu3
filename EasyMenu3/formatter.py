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