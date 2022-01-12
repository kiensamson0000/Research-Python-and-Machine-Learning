# BÀI HỌC BOOLEAN
#--------------------------------------------------------------------------
x= True
y= False

print(x==y)
print(3<5 or 10>20)



# IF .. ELSE
# ..........................................................................
dtb = float(input('Mời bạn nhập vào dtb= '))
if dtb >= 5:
    print('bạn đã đậu')
    print('hú hồn chim én')
else:
    print('ở nhà lấy vợ')
    print('đi phụ hồ nhé!')



# IF ... ELSE LỒNG NHAU
# ----------------------------------------------------------------------------

dtb = float(input('Nhập điểm dtb= '))

if dtb>=9:
    print('Xếp laoij giỏi')
elif dtb>=7:
    print('Xếp loại khá')
elif dtb>=5:
    print('xẾP LOẠI TB')
else:
    print('KHông xếp loại')

# PASS
# ----------------------------------------------------------------------------

a= int(input('mNhập số a '))
b= int(input('Nhập số b'))
if a==0:
    pass
else:
    x= -b/a
    print('no x= ',x)

# so sánh số thực  => sai số khi quá nhỏ 
# với int, kiểu float cần ngưỡng sai số khi ss, cho sai số=0.0000001
# ----------------------------------------------------------------------------

d1 = 1.11 - 1.10
d2 = 2.11 - 2.10
print('d1= ',d1)
print('d2= ',d2)
diff = d2-d1
if diff <0:
    diff = -diff
if diff < 0.0000001:   
    print('d1=d2')
else:
    print('d1!=d2')


# use if..else như phép gán
# ----------------------------------------------------------------------------
#
a= 5
b= 5

c= 113 if a == b else 225
print(c)


x= int(input('Nhập 1 số= '))
print("Số đó là= ", "chẵn" if x%2 ==0 else "lẻ")


print("So do la:", "chan" if x%2==0 else "le")



# kiểm tra năm nhuần
# ----------------------------------------------------------------------------
print('KIỂM TRA NĂM NHUẦN ???')

year = int(input('nhập vào năm= '))
if (year%4 ==0 and year %100 != 0) or year%400 ==0:
           print('Năm nhuần= ', year)
else:
    print('năm không nhuần= ', year)



# đém số ngày trong tháng
# ----------------------------------------------------------------------------

month = int(input('Nhập tháng= '))
if month in (1,3,5,7,8,10,12):
    print("Tháng", month, "có 31 ngày")
elif month in (4,6,9,11):
    print("Tháng", month, "có 30 ngày")
elif month ==2:
    year = int(input('Mời bạn nhập năm= '))
    if (year%4==0 and year%100!=0) or year%400 ==0:
        print("tháng", month,"có 29 ngày")
    else:
        print("tháng", month, "có 28 ngày")
else:
    print('Không hợp lệ, mời bạn nhập lại!  1 < tháng > 12')


# BÀI HỌC GIAI PHUONG TRINH BAC 2
# ----------------------------------------------------------------------------
# a^2+bx+c=0

import math

a= float(input('Nhập số a= '))
b= float(input('Nhập số b= '))
c= float(input('Nhập số c= '))

if a == 0:
    #bx+c
    if b==0 and c == 0:
        print('PT VÔ SỐ NGHIỆM')
    elif b ==0 and c !=0:
        print('PT VÔ NGHIỆM')
    else:
        print('Nghiệm x= ',-c/b)
else:
    #ax2+bx+c=0
    deta= b*b - 4*a*c
    if deta <0:
        print('PT VÔ NGHIỆM')
    elif deta ==0:
        print('PT có nghiệm kép= ',-b/(2*a))
    else:
        print('PT có nghiêm x1= ',(-b+math.sqrt(deta))/2*a)
        print('PT có nghiêm x2= ',(-b-math.sqrt(deta))/2*a)