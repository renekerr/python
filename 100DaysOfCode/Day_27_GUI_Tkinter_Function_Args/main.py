# Day 27 - Graphical User Interface with Tkinter and Function Arguments

# Import all classes and functions from the tkinter library
from tkinter import *

# Create the main window for the GUI application
window = Tk()
window.title('Day 27 | GUI Tkinter')  # Set the window title
window.minsize(width=500, height=500)  # Set minimum window size to 500x500 pixels

# Create a label widget with initial text, font, and style
label_sample = Label(text='Day 27', font=('Arial', 24, 'bold'))
label_sample.pack()  # Place the label in the window using pack for default centering

# Update the label's text directly by modifying the 'text' property
label_sample['text'] = "*args & **kwargs"  # Change text to explain function arguments

# Update label's text again using the config() method for flexibility
label_sample.config(text='Tkinter GUI')  # Set label to display 'Tkinter GUI'


# Define button click action to update label with entry text
def button_clicked():
    """Display entry text in the label when button is clicked."""
    user_new_text = input_sample.get()  # Get text from input field
    label_sample.config(text=user_new_text)  # Update label text with entry content


# Create a button widget and set its action to the button_clicked function
button_sample = Button(text='Click here!', command=button_clicked)
button_sample.pack()  # Place the button in the window using pack()

# Create an entry widget for user text input
input_sample = Entry()
input_sample.pack()  # Place the entry widget in the window using pack()

# Run the main event loop to display the window and keep it open
window.mainloop()


