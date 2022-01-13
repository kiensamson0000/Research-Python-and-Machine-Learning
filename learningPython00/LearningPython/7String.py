#    CHUỖI
#----------------------------------------------------------------------------------



# UPPER, LOWER
#-------------


name= input('Nhập tên mày= ')
print(name.upper())
print(name.lower())



#
# CĂN LỀ RJUST, LJUST, CENTER
# -------------

s1= "name"
s2="Khuat HUy Kien"
s3="kienkh99@gmail.com"

print(len(s3))

print(s1.rjust(18,))
print(s2.rjust(18,))
print(s3.rjust(18,'*'))



# strip
#-------------
s1="                      Hello Long gà         "
print(s1,len(s1))
s2=s1.strip()
print(s2, len(s2))
s3="##   #TRUMP### ##"
s4=s3.strip('#')
print(s4)


# startswith, endswith
#-------------

s="c:/music/bolero/longme.mp3"

if s.endswith(".mp3"):
    print('bai hat định dạng mp3')
else:
    print('bai hat định dạng mp3')

s2="***obama###"

print(s2.startswith("***"))

# loc toàn bộ sđt
def loctoanbophone(dauso):
    dsArr=["0963477226","0901245689","09478555221",
           "0910256389","0947532565"]
    dsfound=[]
    for phone in dsArr:
        if phone.startswith(dauso):
            dsfound.append(phone)
    return dsfound
dauso= input("Nhập đàu sô: ")
print(loctoanbophone(dauso))


# hàm find, rfind và count
#-------------

s="khuất huy kiên đẹp trai"

p1=s.find("k")
p2=s.rfind('k')

print(p1)
print(p2)

p3=s.count("u")
print("u xuất hiên", p3)
p4=s.count("u",4)
print("u xuất hiên", p4, "từ vị trí thứ 4")
p4=s.count("u",4,6)
print("u xuất hiên", p4, "từ vị trí thứ 4 -> 6")



# hàm format, hàm substring
#-------------

s="D:/tailieu/python/lamchupython.pdf"

s1=s.rfind("/")
print(s[s1+1:])
s2=s.rfind(("."))
print(s[s1+1:s2])



# tách chuỗi
#-------------
#
s="sv007;Khuất Huy Kiên;4.7.1999"
arr= s.split(';')
print(len(arr))
for i in arr:
    print(i)



s1="""Obama
    hahaha
    longka
    """
arr=s1.splitlines()
for i in arr:
    print(i,i.count('a'))

s3="""sv007;Khuất Huy Kiên;4.7.1999
      sv006;Nguyễn HẢI LONG;6.6.1999
      sv005;Dương Văn Dũng;4.4.1999
      sv006;Dương Văn Dũng
    """
arr=s3.splitlines()
for line in arr:
    arr2=line.strip().split(";")
    if len(arr2) ==3:
        print(arr2)

s="sv001;KHUẤT HUY KIÊN;04/07/1999"
arr=s.split(";")
print(arr)
for line in arr:
    print(line.strip())
s2=","
s2=s2.join(arr)
print(s2)


a="Kim chung"
b="Trump"
c= a+b
print(c)



#    ÔN TẬP CHUỖI
#----------------------------------------------------------------------------------

def checkdoixung(arr):
    flat= True
    for i in range(len(arr)):
        if arr[i] != arr[len(arr)-i-1]:
                flat =False
                break
    return flat

while True:
    def main():
        arr = input("Nhập vào 1 chuỗi= ")
        if checkdoixung(arr):
            print("Là chuỗi đối xứng")
        else:
            print("KHÔNG LÀ chuỗi đối xứng")
    main()
    hoi = input("M có tiếp tục không?(c/k)")
    if hoi =='k':
        break
print("BYE BYE EM NHÉ")




#toi uu chuoi
#--------------------------

def toiuuchuoi(arr):
    s2=arr
    s2=s2.strip()
    s2=s2.split(' ')
    print("aaa",s2)
    s3=""
    for i in s2:
        if len(i.strip()) !=0:  # (hoac) i != ''
            s3 = s3 + i +" "
    return s3.strip()

arr="       KHUẤT   HUY    KIEN        "
print(arr,len(arr))
print(toiuuchuoi(arr),len(toiuuchuoi(arr)))




#--------------------------

arr="5,7,8,-2,8,11,-13,9,10"

def xuat(arr):
    arr=arr.split(",")
    for i in arr:
        print(int(i))

print(xuat(arr))


def sochan(arr):
    dem=0
    arr = arr.split(",")
    for i in arr:
        print(i)
        if int(i)%2==0:
            dem+=1
    return dem

print("so chẵn= ",sochan(arr))


def soam(arr):
    dem=0
    arr = arr.split(",")
    for i in arr:
        if int(i)< 0:
            dem+=1
    return dem

print("so âm= ",soam(arr))


def checksongto(n):
    dem=0
    for i in range(1,n+1):
        if n%i ==0:
            dem+=1

    return dem==2

def demsongto(arr):
    dems=0
    arr = arr.split(",")
    for i in arr:
        x= int(i)
        if checksongto(i):
            dems+=1
    return dems
print('songto',demsongto(arr))



def sumtb(arr):
    sumtb=0
    sum=0
    arr = arr.split(",")
    for i in arr:
        print(i)
        x= int(i)
        sum+=x
    sumtb=sum/len(arr)
    return sumtb

print('diemtb= ',sumtb(arr))





#    BÀI TẬP TỰ RÈN LUYỆN
#----------------------------------------------------------------------------------


arr=input("Nhập vào một chuỗi= ")

deminhoa=0
deminthuong=0
demcs=0
demktdb=0
demkt=0
demna=0
dempa=0
arr1=arr.upper()
arr2=arr.lower()
for i in arr:
    if i==" ":
        demkt+=1
    elif i in arr1 :
        deminhoa+=1
    elif i in arr2:
        deminthuong+=1

ngam="a,ă,â,e,ê,i,o,ô,ơ,u,ư,y"
ngam=ngam+ngam.upper()
for i in arr:
    if i in ngam:
        demna+=1
    else:
        dempa+=1

print("dem khoang trang",demkt)
print("Đếm in hoa",deminhoa)
print("Đém in thường",deminthuong)
print("Nguyên âm= ",demna)
print("Phụ âm= ",demna)


# tuong tu dem: chu so, ky tu dac biet

