import customtkinter as ctk    # For UI
import CTkMessagebox as ctkMb  # For Popup Boxes
from PIL import Image          # To insert images
import config                  # Global varibales
import commands                # Import files containing commands


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
            dark_image=Image.open(config.IMG_FILE),
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
            width=config.LABEL_WIDTH,
            anchor="e",
        )
        website_label.grid(row=0, column=0)

        # Search box
        self.website_entry = ctk.CTkEntry(master=website_frame, width=config.SEARCHBOX_WIDTH)
        self.website_entry.grid(row=0, column=1)
        self.website_entry.focus()

        search_button = ctk.CTkButton(
            master=self.website_entry,
            text="Search",
            fg_color="#D4483B",
            hover_color="#b23327",
            width=120,
            command=lambda: commands.search_for_pw(self.website_entry, self)
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
            width=config.LABEL_WIDTH,
            anchor="e"
        )
        email_label.grid(row=0, column=0)

        # Entry
        self.email_entry = ctk.CTkEntry(master=email_frame, width=(config.SEARCHBOX_WIDTH + config.SPACER))
        self.email_entry.grid(row=0, column=1)
        self.email_entry.insert(0, config.EMAIL) # prepopulate text entry
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
            width=config.LABEL_WIDTH,
            anchor='e'
        )
        pw_label.grid(row=0, column=0)

        # Entry
        self.password_entry = ctk.CTkEntry(master=pw_frame, width=config.SEARCHBOX_WIDTH)
        self.password_entry.grid(row=0, column=1)

        # Button
        password_button = ctk.CTkButton(
            master=pw_frame,
            text="Generate",
            fg_color="#D4483B",
            hover_color="#b23327",
            width=120,
            command=lambda: commands.insert_gen_pw(self.password_entry)
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
            command=lambda: commands.save_pw(self.website_entry, self.email_entry, self.password_entry, self)
        )
        add_button.grid(row=4, column=0, pady=(20, 0))
        #--------------------------------------
