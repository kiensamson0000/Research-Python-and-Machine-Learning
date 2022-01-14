from cgitb import text
from tkinter import *
from XuLyFile import *

#def
def themAction():
    line = stringMa.get() + ";" + stringTen.get() + ";" + stringNam.get() 
    luu_file(line)
    stringMa.set("")
    stringNam.set("")
    stringTen.set("")
    showSach()

def showSach():
    arrSach = doc_file()
    listbox.delete(0,END)
    for item in arrSach:
        listbox.insert(END, item)

def sapXep():
    arrSach = doc_file()
    for i in range(len(arrSach)):
        for j in range(len(arrSach)):
            a = arrSach[i]
            b = arrSach[j]
            if a[2] > b[2]:  #=> vtri namxb = 2
                arrSach[j] = a
                arrSach[i] = b
    listbox.delete(0,END)
    for item in arrSach:
        listbox.insert(END, item)

def searchSach(): #search follow Ma
    arrSach = doc_file()
    ma = stringMa.get()
    found = False
    for sach in arrSach:
        if sach[0] == ma: #=> vtri ma sach = 0
            found = True
            break
    if found:
        pass 
        #xu ly not show len man hinh
        #listbox.delete(0,END)
        #show
    else:
        pass 
        #xu ly 

root = Tk()

# Declare variable
stringMa = StringVar()
stringTen = StringVar()
stringNam = StringVar()

root.title("Quản lý sách")
root.minsize(height=300, width=350)

#UI
Label(root, text="Quản lý sách", fg='blue', font=("cambria",16)).grid(row=0, columnspan=2)
listbox = Listbox(root, width=50)
listbox.grid(row=1, columnspan=2)

# run program => show all in DB
showSach()

Label(root, text="Ma Sach:").grid(row=2, column=0)
Entry(root, width=30, textvariable=stringMa).grid(row=2, column=1)
Label(root, text="Ten Sach:").grid(row=3, column=0)
Entry(root, width=30, textvariable=stringTen).grid(row=3, column=1)
Label(root, text="Nam XB:").grid(row=4, column=0)
Entry(root, width=30, textvariable=stringNam).grid(row=4, column=1)

frameButton = Frame(root)
Button(frameButton, text="Add", command=themAction).pack(side=LEFT) #them cạnh trái
Button(frameButton, text="Search", command=searchSach).pack(side=LEFT)
Button(frameButton, text="Sort", command=sapXep).pack(side=LEFT)
Button(frameButton, text="Exit", command=exit).pack(side=LEFT)
frameButton.grid(row=5,column=1)

#mainloop()
root.mainloop()