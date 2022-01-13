from cgitb import text
from tkinter import *

root = Tk()
root.title("Quản lý sách")
root.minsize(height=300, width=350)

Label(root, text="Quản lý sách", fg='blue', font=("cambria",16)).grid(row=0, columnspan=2)
listbox = Listbox(root, width=50)
listbox.grid(row=1, columnspan=2)
Label(root, text="Ma Sach:").grid(row=2, column=0)
Entry(root, width=30).grid(row=2, column=1)
Label(root, text="Ten Sach:").grid(row=3, column=0)
Entry(root, width=30).grid(row=3, column=1)
Label(root, text="Nam XB:").grid(row=4, column=0)
Entry(root, width=30).grid(row=4, column=1)

frameButton = Frame(root)
Button(frameButton, text="Add").pack(side=LEFT)
Button(frameButton, text="Search").pack(side=LEFT)
Button(frameButton, text="Sort").pack(side=LEFT)
Button(frameButton, text="Exit").pack(side=LEFT)
frameButton.grid(row=5,column=1)

root.mainloop()