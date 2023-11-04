import customtkinter as ctk    # For UI
import CTkMessagebox as ctkMb  # For Popup Boxes
from PIL import Image          # To insert images
from os import path            # To allow file to be run anywhere


# Gives full path of this file
PATH = path.abspath(path.join(path.dirname(__file__), ''))


LABEL_WIDTH = 140
SEARCHBOX_WIDTH = 200
GAP = 120
FG_COLOR = "#D4483B"
HOVER_COLOR = "#b23327"

IMG_FILE = f"{PATH}/logo.png"


class UI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.configure()
        self.configure(padx=50, pady=50)

        # Create frame to hold content
        content_frame = ctk.CTkFrame(master=self)
        content_frame.grid(row=0, column=0)
        content_frame.grid_columnconfigure(0, weight=1)

        # Center content to center of window
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        logo_image = ctk.CTkImage(
            dark_image=Image.open(IMG_FILE),
            size=(200, 200)
        )
        logo_label = ctk.CTkLabel(
            master=content_frame,
            image=logo_image,
            text="",
        )
        logo_label.grid(row=0, column=0)

        #--------------------------------------
        # WEBSITE ENTRY
        #--------------------------------------
        # Frame
        website_frame = ctk.CTkFrame(master=content_frame)
        website_frame.grid(row=1, column=0, columnspan=3)

        # Label
        website_label = ctk.CTkLabel(
            master=website_frame,
            text="Website: ",
            width=LABEL_WIDTH,
            anchor="e",
        )
        website_label.grid(row=0, column=0)

        # Search box
        website_entry = ctk.CTkEntry(master=website_frame, width=SEARCHBOX_WIDTH)
        website_entry.grid(row=0, column=1)
        website_entry.focus()

        search_button = ctk.CTkButton(
            master=website_entry,
            text="Search",
            fg_color="#D4483B",
            hover_color="#b23327",
            width=120,
        )
        search_button.grid(row=0, column=2)
        #--------------------------------------

        #--------------------------------------
        # EMAIL ENTRY
        #--------------------------------------
        # Frame
        email_frame = ctk.CTkFrame(content_frame)
        email_frame.grid(row=2, column=0, columnspan=3)

        # Label
        email_label = ctk.CTkLabel(
            master=email_frame,
            text="Email/Username: ",
            width=LABEL_WIDTH,
            anchor="e"
        )
        email_label.grid(row=0, column=0)

        # Entry
        email_entry = ctk.CTkEntry(master=email_frame, width=(SEARCHBOX_WIDTH + GAP))
        email_entry.grid(row=0, column=1)

        # email_entry.insert(0, "johndoe@gmail.com") # prepopulate text entry
        #--------------------------------------


        #--------------------------------------
        # PASSWORD ENTRY
        #--------------------------------------
        # Frame
        pw_frame = ctk.CTkFrame(content_frame)
        pw_frame.grid(row=3, column=0, columnspan=3)

        # Label
        pw_label = ctk.CTkLabel(
            master=pw_frame,
            text="Password: ",
            width=LABEL_WIDTH,
            anchor='e'
        )
        pw_label.grid(row=0, column=0)

        # Entry
        self.password_entry = ctk.CTkEntry(master=pw_frame, width=SEARCHBOX_WIDTH)
        self.password_entry.grid(row=0, column=1)

        # Button
        password_button = ctk.CTkButton(
            master=pw_frame,
            text="Generate",
            fg_color="#D4483B",
            hover_color="#b23327",
            width=120,
        )
        password_button.grid(row=0, column=2)
        #--------------------------------------

        #--------------------------------------
        # ADD BUTTON
        #--------------------------------------
        add_button = ctk.CTkButton(
            master=content_frame,
            text="Add",
            fg_color="#D4483B",
            hover_color="#b23327",
        )
        add_button.grid(row=4, column=0, pady=(20, 0))
        #--------------------------------------

ui = UI()
ui.mainloop()

