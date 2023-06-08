import tkinter as tk
from tkinter import messagebox
import json
import pyperclip
import customtkinter
from PIL import  ImageTk,Image




# Function to authenticate the user
def authenticate():
    username = username_entry.get()
    password = password_entry.get()

    # Load the stored login credentials from the file
    try:
        with open("login_credentials.json", "r") as file:
            login_credentials = json.load(file)
    except FileNotFoundError:
        login_credentials = {}

    # Check if the entered username and password match the stored credentials
    if username in login_credentials and login_credentials[username] == password:
        open_password_manager()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")

# Function to create a new account
def create_account():
    # Load the stored login credentials from the file
    try:
        with open("login_credentials.json", "r") as file:
            login_credentials = json.load(file)
    except FileNotFoundError:
        login_credentials = {}

    # Check if any accounts exist already
    if len(login_credentials) > 0:
        messagebox.showerror("Account Creation Failed", "Only one account can be created!")
        return

    username = username_entry.get()
    password = password_entry.get()

    # Add the new username and password to the login credentials
    login_credentials[username] = password

    # Save the updated login credentials to the file
    with open("login_credentials.json", "w") as file:
        json.dump(login_credentials, file)

    messagebox.showinfo("Account Created", "Account created successfully!")


# Function to open the password manager
def open_password_manager():
    login_window.destroy()  # Close the login window

    def save_credentials():
        website = website_entry.get()
        username = username_entry.get()
        password = password_entry.get()

        # Load existing credentials from the file
        try:
            with open("credentials.json", "r") as file:
                credentials = json.load(file)
        except FileNotFoundError:
            credentials = {}

        # Add or update the credentials for the given username
        credentials[website] = username
        credentials[username] = password

        # Save the updated credentials to the file
        with open("credentials.json", "w") as file:
            json.dump(credentials, file)

        messagebox.showinfo("Success", "Credentials saved!")

    # Function to retrieve saved password for a given username
    def get_password():
        get_website = website_entry.get()

        # Load the credentials from the file
        try:
            with open("credentials.json", "r") as file:
                credentials = json.load(file)
        except FileNotFoundError:
            credentials = {}

        # Retrieve the password for the given username
        username = credentials.get(get_website, "Not found")
        password = credentials.get(username, "Not found")

        # Copy the password to the clipboard
        credentials_text = f"Username: {username}\nPassword: {password}"
        pyperclip.copy(credentials_text)

        messagebox.showinfo("Credentials", f"{get_website}\nusername: {username}\npassword: {password}")


    # Create the main window
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    window = customtkinter.CTk()
    window.geometry("600x400")
    window.resizable(False, False)
    window.title("Password Manager")

    img1 = ImageTk.PhotoImage(Image.open("img.png"),width=600,height=400)
    l1 = customtkinter.CTkLabel(master=window, image=img1)
    l1.pack()

    frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=6)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    # Create and position form elements

    website_label = customtkinter.CTkLabel(master=frame,
                                           text="Enter your credentials & save it\n Click Get to know your credentials",
                                           font=("Century Gothic", 15))
    website_label.place(x=50, y=45)

    website_entry = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Enter Website name")
    website_entry.place(x=50, y=110)

    username_entry = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Enter username or Email")
    username_entry.place(x=50, y=165)

    password_entry = customtkinter.CTkEntry(master=frame, show="*", width=220, placeholder_text="Enter password", )
    password_entry.place(x=50, y=220)

    save_button = customtkinter.CTkButton(master=frame, width=100, text="Save", corner_radius=6, compound="left",
                                          command=save_credentials)
    save_button.place(x=50, y=270)

    get_button = customtkinter.CTkButton(master=frame, width=100, text="Get", corner_radius=6, command=get_password)
    get_button.place(x=170, y=270)

    # Start the Tkinter event loop
    window.mainloop()






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    login_window = customtkinter.CTk()
    login_window.geometry("600x400")
    login_window.resizable(False, False)
    login_window.title("Password Manager Login")

    img1 = ImageTk.PhotoImage(Image.open("img.png"),width=600,height=400)
    l1 = customtkinter.CTkLabel(master=login_window, image=img1)
    l1.pack()

    frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=6)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    login_lable = customtkinter.CTkLabel(master=frame,text="Create OR Login",font=("Century Gothic", 20))
    login_lable.place(x=50, y = 55)
    # Create and position form elements for login
    username_entry = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Enter username or Email")
    username_entry.place(x=50, y=110)

    password_entry = customtkinter.CTkEntry(master=frame, width=220, show = "*", placeholder_text="Enter your password")
    password_entry.place(x=50, y=165)

    login_button = customtkinter.CTkButton(master=frame, width=220, text="Login", corner_radius=6, command=authenticate)
    login_button.place(x = 50, y = 220)

    create_account_button = customtkinter.CTkButton(master=frame, width=220, text="Create account",corner_radius=6,command=create_account)
    create_account_button.place(x=50,y=275)


    # Start the Tkinter event loop for the login window
    login_window.mainloop()


