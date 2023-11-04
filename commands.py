import json
import random
import CTkMessagebox as ctkMb

from customtkinter import END
from config import JSON_FILE


def _gen_pw() -> str:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pw_letters = [ random.choice(letters) for _ in range(nr_letters) ]
    pw_symbols = [ random.choice(symbols) for _ in range(nr_symbols) ]
    pw_numbers = [ random.choice(numbers) for _ in range(nr_numbers) ]

    pw_list = pw_letters + pw_symbols + pw_numbers

    random.shuffle(pw_list)
    password = "".join(pw_list)

    return password


def load_pw(password_entry):
    password = _gen_pw()                    # Returns randomy generated string
    password_entry.delete(0, END)  # delete the data in the prompt if any
    password_entry.insert(0, password)      # autofill data in prompt


def find_pw(website_entry):
    website = website_entry.get().title()

    try:
        with open(JSON_FILE) as file:
            data = json.load(file)
    except FileNotFoundError:
         ctkMb.CTkMessagebox(
             title=website,
             message=f"No saved passwords in data file",
             icon="cancel"
         )
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            ctkMb.CTkMessagebox(
                title=website,
                message=f"Email: {email}\nPassword: {password}"
            )
        else:
            ctkMb.CTkMessagebox(
                title=website,
                message=f"{website} entry is not found",
                icon="warning",
            )


def save(website_entry, email_entry, password_entry):
    website = website_entry.get().title()
    email = email_entry.get()
    pw = password_entry.get()

    if not website or not pw:
        ctkMb.CTkMessagebox(
            title="Error",
            message="Left website blank and/or password blank\nPlease try again.",
            icon="warning"
        )
    else:
        confirmbox = ctkMb.CTkMessagebox(
            title="Confirm",
            message=f"Website: {website}\nEmail: {email}\nPassword: {pw}\n",
            option_1="Ok",
            option_2="Retry"
        )

        if confirmbox.get() == "Ok":

            new_data = {
                website: {
                    "email": f"{email}",
                    "password": f"{pw}",
                }
            }

            try: # Open the file
                with open(JSON_FILE, 'r') as file:
                    data = json.load(file)
            except FileNotFoundError: # Write the file with new data
                with open(JSON_FILE, 'w') as file:
                    json.dump(new_data, file, indent=4)
            else: # Otherwise update the data in the json with new data
                data.update(new_data)
                with open(JSON_FILE, 'w') as file:
                    json.dump(data, file, indent=4)
            finally: # Clear entries from GUI
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            confirmbox.destroy()
