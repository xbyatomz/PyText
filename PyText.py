import sys, tkinter
from tkinter import *
import tkinter.filedialog as fdialog

root = Tk("Text Editor")
root.title = 'Python Text Editor'
text = Text(root)
text.grid()

def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = fdialog.asksaveasfilename(title='Save as...', defaultextension=".py", filetypes= [('All Files', '.*'),('Python', '.py'), ('HTML', '.html')])
    file1 = open(savelocation, 'w+')
    file1.write(t)
    file1.close()

buttonSave = Button(root, text="Save", command=saveas)
buttonSave.grid()
root.mainloop()
