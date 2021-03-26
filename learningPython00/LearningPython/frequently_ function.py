# HÀM CƠ BẢN 1
# ----------------------------------------------------------------------------------
from math import *

x=2
y=5

print('Lũy thừa: ',pow(2,5))
print('Căn:',sqrt(x))
print('log10(100)',log10(100))
print('log(2)',log(2))
print('exp(2)',exp(2))
print('radians(30)',radians(30))
do = radians(30)
print(degrees(do))


# HÀM CƠ BẢN 2
# ----------------------------------------------------------------------------------
from math import *
goc = float(input('Nhập vào 1 góc= '))
t = radians(goc)
sinx = sin(t)
cosx= cos(t)
tanx= tan(t)
print('Sin của {0}là: {1}'.format(goc,sinx))
print('Cos của {0}là: {1}'.format(goc,cosx))
print('Tan của {0}là: {1}'.format(goc,tanx))


# HÀM TIME
# ----------------------------------------------------------------------------------
import time


#hàm time.perf_counter()

start = time.perf_counter()
print('Mời bạn nhập giá trị')
x = int(input('Nhập x= '))
print('In x= ', x)
end = time.perf_counter()
timecho = end - start
print('Time chờ= ', timecho )


start = time.perf_counter()
for i in range(10000):
    print('Xuất x= ',i,end='')
end = time.perf_counter()
thoigiancho = end - start
print('Time chờ= ', thoigiancho )



# hàm sleep:
# -----------------------------------

for i in range(1000):
    print(i)
    time.sleep(1)



# HÀM RANDOM
# ----------------------------------------------------------------------------------
from random import randrange

count=0
while True:
    x= randrange(-100,100)
    print('X=',x,end='')
    count+=1
    if x==50:
        break
print('\nSố 50 thấy ỏ lần thứ: ',count)
print('Bye')



# HÀM EXIT
# ----------------------------------------------------------------------------------

while True:
    print('Nhập 1 số: ')
    n=int(input('Nhập số: '))
    dem=0
    for i in range(1,n+1):
        if n%i==0:
            dem+=1
    if dem ==2:
        print('Số nguyên tố!')
    else:
        print('Ko là số mnguyeen tố!')
    hoi=input('Muốn tiếp ko?(c/k)')
    if hoi=='k':
        exit()
print('BYE')



# HÀM EVAL
# ----------------------------------------------------------------------------------

from math import *
s= "1+2+3+sin(0.5)+pow(2,3)"
print('giá trí= ',eval(s))

x1,x2 = eval(input('Nhập giá trị x1,x2:'))
print('x1',x1,'x2:',x2)


# ÔN TẬP LUYỆN
# ---------------------------------------------------------------------------------


#     GAME ĐOÁN SỐ
# -----------------
from random import randrange
print('WELCOME TO GAME ĐOÁN SỐ by kinn.khk')
while True:
    y = randrange(1,10)
    for i in range(1,8):
        x = int(input('Nhập số bạn đoán lần {0}= '.format(i)))
        if x < 1 or x > 100:
            print('Mời bạn nhập lại! ([1,100])')
        else:
            if x == y:
                print('Giỏi quá! bạn đã đoán đúng rồi!')
                break
            elif x>y:
                print('Oh, số bạn đoán lớn hơn rồi, đoán lại nhé')
            elif x<y:
                print('Oh, số bạn đoán nhỏ hơn rồi, đoán lại nhé')
    print('END GAME', 'Số máy là: ',y)
    hoi= input('Ban có muốn chơi tiếp ko?(c/k):')
    if hoi =='k':
        break


#     TÍNH dt tam giác
# -----------------

a= float(input('Nhập cạnh 1= '))
c= float(input('Nhập cạnh 2= '))
b= float(input('Nhập cạnh 3= '))
s=0;
p=(a+b+c)/2
if a+b>c and b+c>a and c+a>b and (a>0 and b>0 and c>0):
    print('3 cạnh a,b,c tạo thành 1 tam giác!')
    s= sqrt(p*(p-a)*(p-b)*(p-c))
    print('Diện tích= ',s)
else:
    print('3 cạnh không tạo 1 tam giác!')



#     TÍNH điểm TB
# -----------------

toan, ly, hoa =eval(input('Nhập điểm toán, lý, hóa='))

dtb= (toan+ly+hoa)/3

print('Diểm tb= ',round(dtb,2))



#     TÍNH căn
# -----------------

n= int(input('Nhập vào n= '))
s=0
for i in range(1,n+1):
    s = sqrt(2+s)
print('Tổng= ',s)