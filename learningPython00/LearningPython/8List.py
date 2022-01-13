

# # #    khai báo list
# # #----------------------------------------------------------------------------------
# lst =[]

# print(len(lst))
# lst = [3,-9,8,2]

# print(lst)
# for i in lst:
#     print(i)

# print(lst[0])

# lst=[0]*10
# print(lst)
# lst=[3,'obama']
# print(lst)




# #    duyệt list
# #----------------------------------------------------------------------------------
# from random import randrange

# n= int(input("Số ptu list: "))
# lst=[0]*n
# for i in range(n):
#     lst[i]= randrange(-100,100)
# print(lst)
# print("*"*10)
# for i in lst:
#     print(i, end='\t')
# print()
# print("*"*10)
# for i in range(len(lst)):
#     print(lst[i],end='\t')
# print()
# print("*"*10)
# for i in range(len(lst)-1,-1,-1):
#     print(lst[i], end='\t')




# #    GÁN GIÁ TRỊ
# #----------------------------------------------------------------------------------

# a=[0,1,2,3,4]
# b=[0,1,2,3,4]
# b[2]=35
# print("a[2]=",a[2])
# print("b[2]=",b[2])

# b=a
# b[2]=10
# print("a[2]=",a[2])
# print("b[2]=",b[2])

# c=b
# c[3]=[200]
# print("a[3]=",a[3],"b[3]",b[3])
# """alias"""




# #    CÁC PHƯƠNG THỨC THƯỜNG DÙNG
# #----------------------------------------------------------------------------------

# lst=[1,2,3]
# lst.insert(0,100)
# print(lst)
# lst.insert(2,99)
# print(lst)



# #-------------------------
# #chèn cuối danh sách

# lst=[10,20,30]
# lst.append(700)
# print(lst)
# lst.append([200,300])
# print(lst)



# #-------------------------
# #xóa phân tử

# lst=[0,1,2,3,4,5,6,7,8,9,10,20,30]
# lst.remove(4)
# print(lst)
# lst.remove(6)
# print(lst)
# del lst[10]
# print(lst)
# del lst[4:7]
# print(lst)
# del lst[1],lst[4]
# print(lst)



# #-------------------------
# # reverse: Dao ds

# lst=[10,20,30,40]
# print(lst)
# lst.reverse()
# print(lst)
# print()
# print("*"*10)
# lst=[1,2,3,4,5,6,7]
# lst2=reversed(lst)
# for i in lst2:
#     print(i,end=' ')
# print()
# print(lst)




# #-------------------------
# # # sort ~ sắp xếp

# from random import randrange

# lst=[0]*10
# for i in range(len(lst)):
#     lst[i]= randrange(-100,100)
# print(lst)
# lst.sort()
# print(lst)
# print('*'*10)
# lst=[100,2,34,11,1,9]
# print(lst)
# lst2=sorted(lst)
# print(lst2)
# print(lst)
# print('$'*10)
# lst=[2,4,1,9,10]
# print(lst)
# lst.sort(reverse=True)
# print(lst)

# #-------------------------
# # slicing


# lst=[1,2,3,4,5,6,7,8,9,10,20,30,40]
# print(lst)
# print(lst[0:3])


# #-------------------------
# # # LIST ĐA CHIỀU
from random import randrange

# lst= [
#     [2,3,4],
#     [5,6,7],
#     [9,10,12]
# ]
# print(lst)
# # cách 1:
# for row in lst:
#     for col in row:
#         print(col,end='\t')
#     print()
# print("*"*10)

# # cách 2:
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         print(lst[i][j],end='\t')
#     print()

# #khởi tạo list tự động
arr2=[]
rowsize= int(input("Nhập vào số dòng"))
columesize= int(input("Nhập vào số cột"))
for i in range(rowsize):
    onerow=[]
    for j in range(columesize):
        onerow.append(randrange(-100,100))
    arr2.append(onerow)
print("ma trận máy nhập")


#duyệt mảng
for i in range(len(arr2)):
    for j in range(len(arr2[i])):
        print(arr2[i][j],end='\t')
    print()


# #-------------------------
# # # Xử lý list phần 1

# from random import randrange

# print("Chương trình xử lý list: ")
# n= int(input("Nhập vào số ptu: "))
# lst=[0]*n
# for i in range(n):
#     lst[i]=randrange(-100,100)
# print("List ngẫu nhiên")
# print(lst)


# #them ptu
# print("thêm phân tử")
# lst.insert(4,100)
# lst.insert(5,200)
# print(lst)
# value= int(input("nhập ptu muôn thêm:"))
# lst.append(value)
# print(lst)

# #kiểm tra số lần xuất hiện

# k=int(input("Số bạn muốn đếm: "))
# dem= lst.count(k)
# print(k ,"xuất hiện", dem,"trong lsit")

# #tổng số ngto trong list

# def ngto(n):
#     dem=0
#     for i in range(1,n+1):
#         if n%i==0:
#             dem+=1
#     if dem == 2:
#         return dem

# demnt=0
# tongnt=0
# for x in lst:
#      if ngto(x):
#         demnt+=1
#         tongnt+=x
# print("Có",demnt,"số ngto trong list")
# print("Tông ngto",tongnt)

# # sap xep
# list2=sorted(lst)
# print("SX tăng dần klo làm thay đổi lst: ")
# print(list2)

# lst.sort(reverse=True)
# print("List sau khi sắp xếp giảm dan: ")
# print(lst)


# #xóa list
# del lst
# print("danh sách list sau khi xóa là: ")
# print(lst)



# #-------------------------
# # # Xử lý list phần 2

# from random import randrange

# #khơi tạo
# lst=[]
# n= int(input("Nhập n ptu cho list: "))
# for i in range(n):
#     lst.append(randrange(-100,100))
# print("List ngẫu nhiên là:")
# print(lst)

# #nhập k, xóa tất cả gái trị k trong list

# x=int(input("Nhập số muốn chèn"))
# lst.append(x)
# print(lst)
# k=int(input("Nhap ptu k muốn xóa: "))

# while lst.count(k) >0:
#     lst.remove(k)
# print("List sau khi xóa",k,"là:",lst)

# # đói xứng
# def checkdx(lst):
#     for i in range(len(lst)):
#         if lst[i] != lst[len(lst)-i-1]:
#             return False
#     return True

# check=checkdx(lst)
# if check==True:
#     print("List đối xứng")
# else:
#     print("List ko đối xứng")


# #-------------------------
# # # Xử lý list đa chiều
# from random import randrange


# def taomaxtri(m,n):
#     maxtri=[]
#     for i in range(m):
#         maxtri2=[]
#         for j in range(n):
#             maxtri2.append(randrange(-100,100))
#         maxtri.append(maxtri2)
#         print()
#     return maxtri

# def xuatmaxtri(maxtriD):
#     for i in maxtriD:
#         for j in i:
#             print(j,end='\t')
#         print()

# m=int(input("Nhập vào số dòng: "))
# n= int(input("Nhập vào số cột: "))
# maxtriD=taomaxtri(m,n)
# xuatmaxtri(maxtriD)

# def xuatdong(k):
#     for j in range(len(maxtriD[k])):
#         print(maxtriD[k][j],end='\t')

# k= int(input("Nhập dòng muốn xuất"))
# D= xuatdong(k)

# def xuatcot(k):
#     for i in range(len(maxtriD)):
#         print(maxtriD[i][k], end='\t')

# k= int(input("\nNhập cột muốn xuất"))
# E= xuatcot(k)

# def Maxmaxtri(maxtriD):
#     max=maxtriD[0][0]
#     for i in range(len(maxtriD)):
#         for j in range(len(maxtriD[i])):
#             if max < maxtriD[i][j]:
#                 max=maxtriD[i][j]
#     return max
# max= Maxmaxtri(maxtriD)
# print("\nSố lớn nhất trong maxtri là: ",max)



# #-------------------------
# # # list
