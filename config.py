from os import path # To allow file to be run anywhere

# Gives full path of this file
PATH = path.abspath(path.join(path.dirname(__file__), ''))

# Default widths
LABEL_WIDTH = 140
SEARCHBOX_WIDTH = 200
SPACER = 120

# Theme
FG_COLOR = "#D4483B"
HOVER_COLOR = "#b23327"

# Image logo location
IMG_FILE = f"{PATH}/logo.png"

# User's email
EMAIL_PATH = f"{PATH}/email.txt"
default_email = "johndoe@email.com"
EMAIL = default_email
try:
    with open(EMAIL_PATH, 'r') as file:
        EMAIL = file.readline().strip()
    
        if EMAIL == "":
           EMAIL = default_email
except:
    with open(EMAIL_PATH, 'w') as file:
        file.write("")
