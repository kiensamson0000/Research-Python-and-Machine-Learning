
#   Operators
#----------------------------------------
import sys

x = 5
y = x **2
print (x)
print (y)
print("{0}+{1}".format(x,y))
print("vung du lieu: ", sys.int_info)

year = 2018
t = year % 2 == 0 and year % 3 >1
print (t)


t = year % 2 == 0 or year % 3 > 5
print (t)

print ("*"*20)

print (9/2)
print(9//2)
print(9%2)


#   OUTPUT
#----------------------------------------


print('Nhap dữ liệu vào:')
x= input()
print('Bạn đã nhập:', x)
print('thông tin kiểu dl:', type(x))

print('*'*20)

# muốn chuyển str về kiểu int
print('Mời nhập:')
x = int(input())
print('bạn đã nhập:',x)
print('thông tin kiểu dl:', type(x))

print('*'*20)

# hàm input() có thể nhập tiêu đề
x = int(input('Nhap dữ liệu vào:'))
print('bạn đã nhập:',x)
print('thông tin kiểu dl:', type(x))

print('*'*20)

# muốn chuyển str về kiểu bool
def strtobool(s):
    return s.lower() in ('yes', 'true','is','1')

x= strtobool(input('Mời bạn nhập dữ liệu:'))
print('giá trị bool: ',x)


# INPUT
#----------------------------------------

print('x'*20)
print('{0}*x^2+{1}*x+{0}'.format(5,2))

print('x'*20) 

# Output căn phải
print('{0:>11}'.format('Hello world'))
print('{0:>11}'.format('Nam'))
print('{0:>11}'.format('Kien'))

# Output căn phải
print('{0:>2} {1:>11}'. format(1, 'hello world'))
print('{0:>2} {1:>11}'. format(2, 'nam'))
print('{0:>2} {1:>11}'. format(3, 'dũng'))
print('{0:>2} {1:>11}'. format(10, 'kiên'))


# COMMENT
#----------------------------------------

x = 5
print(type(x))

x = 'obama'
print(type(x))

# comment 1 dong

"""
day la comment n` dong
"""

x= True
print(type(x))

x = complex(2,3)
print(type(x))
print('thuc', x.real, 'ao',x.imag)

i1 = 2
i2 = 5
i3 = -3

c= i1/(i2+i3)
print('d=',c)
f= 3+4+6//3
print('f=',f)




# ERROR
#----------------------------------------

'''
    # error syntax
    y=2
    x=y+2
    y+2=x // sai
'''

'''
    # error runtime
    x=5
    y=0
    z=x/y
    print(z)
'''

try:
    x=5
    y=0
    z=x/y
    print(z)
except:
    print('Bị lỗi rồi')
print('cảm ơn bạn')

try:
    x =9 
    y =0
    z =2
    print("thuong: ", x/y)
except:
    print("truogn hop nay bi loi!")


# BAI LUYEN TAP
#------------

import math

try:
    r = float(input('Nhập bán kính= '))
    cv = 2 * math.pi * r
    dt = math.pi * r**2

    print('chu vi= ', cv)
    print('diện tích =', dt)
except:
    print('lỗi rồi!')


x = int(input('Nhập số giây= '))
# hours = (x//3600)%24   => ko can %24
hours = (x//3600) 
minute = (x%3600)//60  #=> (x%3600) => so giay
second = (x%3600)%60
print('Dạng giờ phút giây là:',hours,':',minute,':', second)


toan = float(input('Nhập điểm toán: '))
ly = float(input('Nhập điểm lý: '))
hoa = float(input('Nhập điểm hóa: '))
dtb= (toan+ly+hoa)/3

print('Điểm TB: ',dtb)
print('điểm tb=',round(dtb,2))
print('điểmtb= ', round(dtb,3))




