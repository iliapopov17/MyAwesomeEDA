from IPython.display import display, HTML

COLORS = [
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[96m",  # Cyan
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
]


def display_welcome_gif():
    html_code = """
    <img src="imgs/welcome.gif" width="200" height="200">
    """
    display(HTML(html_code))


def display_hruler():
    print()
    print(" ".join([f"{color}\033[1m=====\033[0m" for color in COLORS]))
    print(" ".join([f"{color}\033[1m=====\033[0m" for color in COLORS[::-1]]))
