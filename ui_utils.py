def print_separator(token="=", length=40):
    print(token * length)


def print_title(title):
    print_separator()
    print(title)
    print_separator()


def print_warning():
    print_separator("-")
    print("WARNING")
    print("Use this tool only on systems you own")
    print("or have explicit permission to test.")
    print_separator("-")