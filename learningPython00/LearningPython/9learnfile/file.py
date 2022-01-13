
### FILE
#---------------------------------------------

# ghi file
#--------------------
def savefile(path):

    file=open(path, 'w',encoding="utf-8")
    file.writelines("SV001; KHUẤT HUY KIÊN;4/7/1999")
    file.writelines("\nSV002;NGUYỄN HẢI LONG;1/1/1999")
    file.writelines("\nSV003;NGUYỄN VĂN LONG;2/2/1999")
    file.close()
savefile("learningfile")


# đọc file
# --------------------

def readfile(path):
    file=open(path,'r',encoding="utf-8")
    for line in file:
        data=line.strip()
        print(data)
    file.close()

readfile("learningfile")



def writefile(path):
    file= open(path,"a",encoding="utf-8")
    file.writelines("\nHELLO WORLD ; CHÀO THẾ GIỚI")
    file.writelines("\nCHÀO MỪNG BẠN; WELCOME")
    file.writelines("\nChào em; em cần giúp gì")
    file.close()

writefile("hoctienganh.txt")


def readfile():
    file=open("hoctienganh.txt","r", encoding="utf-8")
    for line in file:
        data= line.strip()
        print(data)
    file.close()

readfile()




# revision
#--------------------

#------
#dữ liệu Sản Phẩm

def ghifile(path,line):
    file=open(path,"a",encoding="utf-8")
    file.writelines(line)
    file.writelines("\n")
    file.close()

def docfile(path):
    arrProduct=[]
    file=open(path,"r",encoding="utf-8")
    for line in file:
        data=line.strip()
        arr=data.split(";")
        arrProduct.append(arr)
    file.close()
    return arrProduct





#------
#Dữ liệu chuỗi số










