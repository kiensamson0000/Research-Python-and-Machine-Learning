


#               HÀM
# ----------------------------------------------------------------------------------

def ptb1(a,b):
    if a==0 and b==0:
        return "Vô sô nghiệm"
    elif a==0 and b!=0:
        return "vô nghiệm"
    else:
        return "x={0}".format(-b/a)


def xuatdulieu(data):
    print(data)


kq=ptb1(3,4)
print('kết quả',kq)

kq2=ptb1(5,8)
xuatdulieu(kq2)
q = xuatdulieu(kq2)

print(q) #=> none vi ko co return




#    VIẾT TÀI LIỆU CHO HÀM
# ----------------------------------------------------------------------------------
#
def USCLN(a,b):
    """
    hàm tìm ước số chung lớn nhất của 2 số a,b.
    vi dụ: USCLN của 6 và 9 là: 3
    """
    min= a if a<b else b
    for i in range(min,0,-1):
        if a%i==0 and b%i==0:
            return i
    return 1

uoc= USCLN(6,9)
print('USCLN của 6 và 9 là:',uoc)



#    GLOBAL VARIABLE: biến toàn cục
# ----------------------------------------------------------------------------------

'''
    g khai báo ngoài hàm tong(): biến global, toàn cục
    g trong hàm tong() là biến local, biến cục bộ
'''
g=5
def tong():
    g=2
    g=g+1
tong()
print(g) #=> g = 5

'''
    g khai báo ngoài hàm tong(): biến global, toàn cục
    g trong hàm tong() là tham chieu den bien g (global), biến toàn cục
'''
g=5
def tong():
    global g
    # g=2
    g=g+1
tong()
print(g) # => g = 3

'''
    có thể dùng global luôn không cần khai báo trc.
    g trong hàm tong() là biến global, biến toàn cục
'''
def tong():
    global g
    g=2
    g=g+1
tong()
print(g) # g = 3


'''
'''
g=5
def tong():
    g=g+1
tong()
print(g) #=> erorr dong g=g+1(g trong hàm(cục bộ) => ko khai báo ko hiểu (ko lấy g dòng 1 đc))






#    PARAMETER MẶC ĐỊNH
# - khi print() => **end** xuất 1 dòng => print("aaa", end='')
# -** \t** => xuất cách 1 tab or** \n** => xuất xuống dòng
# ----------------------------------------------------------------------------------
#
#
def tong(n,m=0):
    s=0
    for i in range(1,m+n):
        s+=i
    return s
print(tong(5))
print(tong(5,1), end='\t')
print(tong(m=1,n=5))




#    LAMBDA EXPRESSION
# # ----------------------------------------------------------------------------------
#
def handle(f,x):
    return f(x)
kq1=handle(lambda x:x**2,9)
print(kq1)

kq2= handle(lambda x:x%2==0,4)
print(kq2)


def sochan(x):
    return x%2==0

kq3= handle(lambda x:sochan(x),2)
print(kq3)

kq4= handle(lambda x:sochan(x),5)
print(kq4)

kq5= handle(sochan,2)
print(kq5)





#    HÀM ĐỆ QUY
# # ----------------------------------------------------------------------------------

#
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(3))



#    VIẾT HÀM TÍNH BMI
# # ----------------------------------------------------------------------------------
print('CHƯƠNG TRÌNH TÍNH CHỈ SỐ CÂN ĐỐI CƠ THỂ')

def BMI(high,weight):
    return weight/(high*high)

def phanloai(bmi):
    if bmi < 18.5:
        return 'Bạn gầy!'
    elif bmi <24.9:
        return ('Bạn bình thường!')
    elif bmi <29.9:
        return('Bạn hơi béo!')
    elif bmi <34.9:
        return('Bạn béo cấp 1')
    elif bmi<39.9:
        return('Bạn béo cấp 2')
    else:
        return('Bnạ béo cấp 3!')
def nguyco(bmi):
    if bmi < 18.5:
        return('Bạn thấp!')
    elif bmi < 24.9:
        return('Bạn cao TB!')
    elif bmi < 29.9:
        return('Bạn cao')
    elif bmi < 34.9:
        return('Bạn cao')
    elif bmi < 39.9:
        return('Bạn rất cao')
    else:
        return('Bạn nguy hiểm')

weight= float(input('Bạn cân nặng= '))
high= float(input('Bạn cao= '))

bmi= BMI(weight,high)
print('Chỉ số BMI= ',bmi)
print('Phân loại của bạn= ',phanloai(bmi))
print('Nguy cơ của bạn= ',nguyco(bmi))






#    HÀM TÍNH ROI
#----------------------------------------------------------------------------------


def tinhroi(doanhthu,chiphi):
    return (doanhthu-chiphi)/chiphi
def goiy(roi):
    if roi>0.75:
        return ('nên đầu tư')
    else:
        return ('KO nên đầu tư')
doanhthu= int(input('Nhập doanh thu= '))
chiphi= int(input('chi phi= '))
roi= tinhroi(doanhthu,chiphi)
print('ROI= ',roi)
print('Có nên đầu tư không: ',goiy(roi))


#    HÀM TÍNH SỐ FIBONACCI
#----------------------------------------------------------------------------------

def fibonacci(n):
    if n <=2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)


print('số fibonacci tại n là: ',fibonacci(8))

def listfibo(n):
    for i in range(1,n+1):
        print(fibonacci(i),end='\t')

listfibo(8)



#    BÀI TẬP TỰ LUYỆN
#----------------------------------------------------------------------------------

def sum1(n):
    s=0
    while n>0:
        s+=1
        n-=1
    return s

def sum2():
    global val
    s=0
    while val>0:
        s+=1
        val-=1
    return s
def sum3():
    s=0
    for i in range(val,0-1):
        s+=1
    return s

def main():
    global val
    val=5
    print(sum2())
    print(sum1(5))
    print(sum3()) #=> ko tham so val ra bien golbal
main()

#----------------------
#
def tinh():
    for i in range(-3,5):
        if i%2!=0:
            print(i, -i,end=' ')

        else:
            print(i,-i,end=' ')
tinh()

#----------------------

def sumusc(a):
    s=0
    for i in range(1,a):
        if a%i==0:
            s +=i
    return s

def check(n):
    if sumusc(n) == n:
        return 'Số đó là số hoàn thiện'
    elif sumusc(n)  > n:
        return 'Số thịnh vượng'
    else:
        return 'Số bình thường'
print(check(100))






