# Day 27 - Graphical User Interface with Tkinter and Function Arguments
import tkinter

window = tkinter.Tk()
window.title('GUI Tkinter')
window.minsize(width=500, height=500)
label = tkinter.Label(text='Day 27', font=('Arial', 24, 'bold'))
label.pack()

window.mainloop()
