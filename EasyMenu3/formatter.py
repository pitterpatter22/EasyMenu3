


class colors:
    """
    A utility class for ANSI terminal text formatting.

    This class provides various ANSI escape codes as class attributes to format text with different
    colors, styles (bold, underline, italic, etc.), and background colors in terminal outputs.
    In addition to the color codes, it includes static methods that wrap messages in these codes,
    making it easy to output colored and styled text in command-line applications.

    Functions:
        colored(message, color):
            Returns the given message wrapped in the specified ANSI color code, then resets the styling.
        
        warning(message):
            Returns the message formatted with the warning color (yellow), useful for alert messages.
        
        fail(message):
            Returns the message formatted with the fail color (red), suitable for error messages or exits.
        
        ok(message):
            Returns the message formatted with the OK color (green), typically used to indicate success.
        
        okblue(message):
            Returns the message formatted with a blue color, which can be used for informational outputs.
        
        header(message):
            Returns the message formatted with a header color (purple-ish), ideal for highlighting headings.
    """
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
    #    print(colors.colored("My colored message", colors.OKBLUE))
    @staticmethod
    def colored(message, color):
      return color + message + colors.ENDC

    # Method that returns a yellow warning
    # usage:
    #   print(colors.warning("What you are about to do is potentially dangerous. Continue?"))
    @staticmethod
    def warning(message):
      return colors.WARNING + message + colors.ENDC

    # Method that returns a red fail
    # usage:
    #   print(colors.fail("What you did just failed massively. Bummer"))
    #   or:
    #   sys.exit(colors.fail("Not a valid date"))
    @staticmethod
    def fail(message):
      return colors.FAIL + message + colors.ENDC

    # Method that returns a green ok
    # usage:
    #   print(colors.ok("What you did just ok-ed massively. Yay!"))
    @staticmethod
    def ok(message):
      return colors.OKGREEN + message + colors.ENDC

    # Method that returns a blue ok
    # usage:
    #   print(colors.okblue("What you did just ok-ed into the blue. Wow!"))
    @staticmethod
    def okblue(message):
      return colors.OKBLUE + message + colors.ENDC

    # Method that returns a header in some purple-ish color
    # usage:
    #   print(colors.header("This is great"))
    @staticmethod
    def header(message):
      return colors.HEADER + message + colors.ENDC
    
    

def print_table(data, headers=None, sort_by=None, ascending=True, theme="default", header_style=colors.OKGREEN):
    """
    Prints a table based on the provided data with optional sorting, theming, 
    and header formatting. The header text is centered, bold, and underlined,
    while the surrounding spaces remain unformatted.

    Parameters:
        data (list of lists): The table data, where each sublist is a row.
        headers (list, optional): List of header labels for the columns.
        sort_by (int or str, optional): Column index or header name to sort by.
        ascending (bool, optional): True for ascending order, False for descending.
        theme (str, optional): Table theme to use. Options:
            - "default": Simple table with header separator.
            - "bordered": Entire table enclosed in a border with lines after each row.
        header_style (str, optional): ANSI escape code for styling the header row)
    """
    
    # Helper function to format a header cell so that only the text is formatted.
    def format_header_cell(text, width):
        text = str(text)
        text_len = len(text)
        left_pad = (width - text_len) // 2
        right_pad = width - text_len - left_pad
        return " " * left_pad + colors.BOLD + colors.UNDERLINE + header_style + text + colors.ENDC + " " * right_pad

    # Determine number of columns
    if headers:
        columns = len(headers)
    elif data:
        columns = len(data[0])
    else:
        print("No data to display.")
        return

    # Optional sorting
    if sort_by is not None:
        sort_index = None
        if isinstance(sort_by, int):
            sort_index = sort_by
        elif isinstance(sort_by, str) and headers:
            try:
                sort_index = headers.index(sort_by)
            except ValueError:
                print(f"Header '{sort_by}' not found in headers. Table will not be sorted.")
        else:
            print("Invalid sort_by parameter. Table will not be sorted.")
        
        if sort_index is not None:
            try:
                data = sorted(data, key=lambda row: row[sort_index], reverse=not ascending)
            except Exception as e:
                print(f"Error during sorting: {e}. Table will not be sorted.")

    # Calculate maximum width for each column based on headers and data
    col_widths = [0] * columns
    if headers:
        for i in range(columns):
            col_widths[i] = len(str(headers[i]))

    for row in data:
        for i in range(columns):
            col_widths[i] = max(col_widths[i], len(str(row[i])))

    if theme == "default":
        # Build row format string for data rows (left-aligned)
        row_format = " | ".join(["{{:<{}}}".format(w) for w in col_widths])
        
        # Print headers with centered text formatting if provided
        if headers:
            header_cells = [format_header_cell(headers[i], col_widths[i])
                            for i in range(columns)]
            print(" | ".join(header_cells))
            print("-+-".join(['-' * w for w in col_widths]))
        
        # Print each row of data
        for row in data:
            print(row_format.format(*row))
    
    elif theme == "bordered":
        # For bordered theme, compute the border line with extra padding (1 space on each side)
        border_line = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

        print(border_line)
        if headers:
            header_cells = [
                " " + format_header_cell(headers[i], col_widths[i]) + " " 
                for i in range(columns)
            ]
            print("|" + "|".join(header_cells) + "|")
            print(border_line)
        
        # Print each data row enclosed in borders with a line after each row.
        for row in data:
            row_cells = [" " + str(row[i]).ljust(col_widths[i]) + " " for i in range(columns)]
            print("|" + "|".join(row_cells) + "|")
            print(border_line)
    
    else:
        print(f"Theme '{theme}' not recognized. Using default theme.")
        row_format = " | ".join(["{{:<{}}}".format(w) for w in col_widths])
        if headers:
            header_cells = [format_header_cell(headers[i], col_widths[i])
                            for i in range(columns)]
            print(" | ".join(header_cells))
            print("-+-".join(['-' * w for w in col_widths]))
        for row in data:
            print(row_format.format(*row))
