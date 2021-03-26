from file import *

ma= input("Nhập mã: ")
ten= input("Nhập tên sp: ")
dgia= float(input("Nhập giá: "))

line= ma + ";" + ten + ";" + str(dgia)

ghifile("datatest.txt",line)

