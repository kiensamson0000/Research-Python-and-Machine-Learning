# #Nhập một số n tối đa 2 chữ số, in ra cách đọc chữ số đó
# #---------------------------------------------------------------------

# n = int(input('Nhập vào số n= '))

# if (99 < n  < 0):
#     print('Không hợp lệ. Mời bạn nhập lại!')
# else:
#     chuc= n//10
#     dvi= n%10
#     if chuc == 0:
#         chuc1 = ''
#     elif chuc == 1:
#         chuc1 = 'Mười'
#     elif chuc == 2:
#         chuc1 = 'Hai Mươi'
#     elif chuc == 3:
#         chuc1 = 'Ba Mươi'
#     elif chuc == 4:
#         chuc1 = 'Bốn Mươi'
#     elif chuc == 5:
#         chuc1 = 'Năm Mươi'
#     elif chuc == 6:
#         chuc1 = 'Sáu Mươi'
#     elif chuc == 7:
#         chuc1 = 'Bảy Mươi'
#     elif chuc == 8:
#         chuc1 = 'Tám Mươi'
#     elif chuc == 9:
#         chuc1 = 'Chin Mươi'

#     if dvi == 1:
#         dvi1 = 'Một'
#     elif dvi == 2:
#         dvi1 = 'Hai'
#     elif dvi == 3:
#         dvi1 = 'Ba'
#     elif dvi == 4:
#         dvi1 = 'Bon'
#     elif dvi == 5:
#         dvi1 = 'Nam'
#     elif dvi == 6:
#         dvi1 = 'Sau'
#     elif dvi == 7:
#         dvi1 = 'Bay'
#     elif dvi == 8:
#         dvi1 = 'Tam'
#     elif dvi == 9:
#         dvi1 = 'Chin'
    
#     print("Cach doc so {0} la:{1} {2}".format(n,chuc1,dvi1))


# #Nhập vào 1 ngày(ngày,tháng,năm). Tìm ngày kế sau ngày vừa nhập
# #---------------------------------------------------------------------

# d = int(input('Nhập ngày= '))
# m = int(input('Nhập tháng= '))
# y = int(input('Nhập năm= '))

# if m in (4,6,9):
#     if (1<d<30):
#         print('Ngày hôm nay: ',d+1,'/',m,'/',y)
#     elif d ==30:
#         print('Ngày hôm nay: ', 1, '/', m+1, '/', y)
# elif m in (1,3,5,7,8,10,12):
#     if (1 < d < 31):
#         print('Ngày hôm nay: ', d + 1, '/', m, '/', y)
#     elif d == 31 and m < 12:
#         print('Ngày hôm nay: ', 1, '/', m + 1, '/', y)
#     elif d == 31 and m == 12:
#         print('Ngày hôm nay: ', 1, '/', 1, '/', y + 1)
# elif m ==2:
#     if (y%4==0 and y%100 !=0) or y%400==0:
#         if (1 < d < 29):
#             print('Ngày hôm nay: ', d + 1, '/', m, '/', y)
#         elif d == 29:
#             print('Ngày hôm nay: ', 1, '/', m + 1, '/', y)
#     else:
#         if (1 < d < 28):
#             print('Ngày hôm nay: ', d + 1, '/', m, '/', y)
#         elif d == 28:
#             print('Ngày hôm nay: ', 1, '/', m + 1, '/', y)



# #Nhập vào a,b và phép toán +, -, *, /. Hãy xuất kết quả theo đúng phép toán đã nhập
# #---------------------------------------------------------------------

# a= float(input('Nhập a= '))
# b= float(input('Nhap b= '))
# c= input('Nhập phép toán(+,-,*,/): ')

# if c=='+':
#     print('Tổng',a ,c,b, 'là:', a+b )
# elif c=='-':
#     print('Hiệu', a, c, b, 'là:', a - b)
# elif c=='*':
#     print('Tích', a, c, b, 'là:', a * b)
# elif c=='/':
#     try:
#         print('Thương', a, c, b, 'là:', a / b)
#     except:
#         print('Lỗi rồi b ê!')


# #Nhập vào 1 tháng và cho biết tháng đó thuộc quý mấy trong năm
# #---------------------------------------------------------------------


# #3 tháng 1 quý, 1 năm 4 quý
# m = int(input('Nhập tháng= '))

# if m in (1,2,3):
#     print('Tháng',m ,'là quý: 1')
# elif m in (4,5,6):
#     print('Tháng',m ,'là quý: 2')
# elif m in (7,8,9):
#     print('Tháng',m ,'là quý: 3')
# elif m in (10,11,12):
#     print('Tháng',m ,'là quý: 4')