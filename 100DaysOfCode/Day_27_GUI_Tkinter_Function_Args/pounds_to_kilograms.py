from tkinter import *

FONT_STYLE = ("Console", 14, "normal")
KG_TO_POUNDS_CONVERSION_RATE = 2.205


def convert_kg_to_pounds():
    """
    Convert the value from kilograms to pounds and update the output label.
    """
    kg_value = float(kg_entry.get())
    pounds_value = kg_value * KG_TO_POUNDS_CONVERSION_RATE
    pounds_result_label.config(text=f"{pounds_value:.2F}")
    pounds_result_label.grid(column=1, row=1)


# Initialize the main window
window = Tk()
window.title('Kilograms to Pounds Converter')
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)


# Create and place the labels
equivalence_label = Label(text='is equal to: ', font=FONT_STYLE)
equivalence_label.grid(column=0, row=1)

pounds_result_label = Label(text='0', font=FONT_STYLE)
pounds_result_label.grid(column=1, row=1)

kg_label = Label(text='Kilograms: ', font=FONT_STYLE)
kg_label.grid(column=2, row=0)
kg_label.config(padx=10, pady=10)

pounds_label = Label(text='Pounds: ', font=FONT_STYLE)
pounds_label.grid(column=2, row=1)
pounds_label.config(padx=10, pady=10)

# Create and place the entry field for kilograms
kg_entry = Entry(width=10)
kg_entry.grid(column=1, row=0)

# Create and place the calculation button
convert_button = Button(text='Calculate', font=FONT_STYLE)
convert_button.config(command=convert_kg_to_pounds)
convert_button.grid(column=1, row=2)

# Run the main loop
window.mainloop()
