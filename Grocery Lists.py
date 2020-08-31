import tkinter as tk
from tkinter import *


# Function for adding items to a list
def add_lists(lists_entry, lists_box):

    grocery = lists_entry.get()

    lists_box.insert(1, grocery)


# Entry point of the program
def main():

    app = tk.Tk()

    app.title("Grocery lists")

    app.geometry("800x500")

    app.configure(background="Gray")

    # Set up Label for title
    title = Label(app, text="Grocery lists app", font="Helvetica 20", background="Gray")
    title.grid(row=0, column=3)

    # Set up Label Frame and Entry for adding items to list
    lists_frame = LabelFrame(app, text="Add to lists", font="Helvetica 10", background="Gray", foreground="Black")
    lists_frame.grid(row=1, column=3)
    lists_entry = tk.Entry(lists_frame, width=20, font="Helvetica 10", background="White", foreground="Black", bd=5)
    lists_entry.grid(row=2, column=3)

    # Set up Listbox to append or insert items from Entry
    lists_box = tk.Listbox(app, height=10, width=30, font="Helvetica 12", background="White", foreground="Black")
    lists_box.grid(row=1, column=4)

    # Set up a button to add items to list
    add_btn = tk.Button(app, text="Add", font='Helvetica 10', width=7, bd=5,
                        command=lambda: add_lists(lists_entry, lists_box))
    add_btn.grid(row=3, column=3)

    app.mainloop()


# The following if statement helps Python determine whether or not the main()
# function in this program is our entry point.
if __name__ == "__main__":
    main()
