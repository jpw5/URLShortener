import customtkinter as ctk
import tkinter
from tkinter import messagebox
import pyshorteners
import pyperclip


def shorten():
    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(longurl_entry.get())
        copy = pyperclip.copy(short_url)
        messagebox.showinfo(title="Success", message="The URL has been copied")
        # shorturl_entry.insert(0, short_url)
    except:
        messagebox.showinfo(title="Error", message="Invalid Entry")


root = ctk.CTk()
root.title("URL Shortener")
root.geometry("300x120")

longurl_label = ctk.CTkLabel(root, text="Enter a Long URL")
longurl_entry = ctk.CTkEntry(root)
# shorturl_label = ctk.CTkLabel(root, text="Output shortened URL")
# shorturl_entry = ctk.CTkEntry(root)
shorten_button = ctk.CTkButton(root, text="Shorten URL", command=shorten)

longurl_label.pack()
longurl_entry.pack()
# shorturl_label.pack()
# shorturl_entry.pack()
shorten_button.pack(pady=5)

root.mainloop()
