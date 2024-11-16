from tkinter import *

FONT = ("Arial", 15, "normal")


def code_copy_validation():
    user_code = user_input.get()
    code_copied_label = Label(text=user_code, font=FONT)
    code_copied_label.grid(column=1, row=5)


window = Tk()
window.title("GUI TKinter")
window.minsize(width=400, height=100)

# Code label
code_label = Label(text="Enter code: ", font=FONT)
code_label.config(padx=10)
code_label.grid(column=0, row=0)

code_check_label = Label(text='Code check: ', font=FONT)
code_check_label.config(padx=20, pady=20)
code_check_label.grid(column=0, row=5)

# Button
button = Button(text="Save", command=code_copy_validation)
button.grid(column=1, row=1)

new_button = Button(text="Cancel")
new_button.grid(column=1, row=2)
new_button.config()

# Entry
user_input = Entry(width=20)
user_input.get()
user_input.grid(column=1, row=0)

# Run the main event loop to display the window and keep it open
window.mainloop()
