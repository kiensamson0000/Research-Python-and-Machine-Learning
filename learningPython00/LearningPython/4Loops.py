
# HỌC WHILE
#---------------------------------------------------------------------

print('Nhập một số [1...10]')
x= -1

while x<1 or x>10:
    x= int(input('Nhập giá trị [1..10]: '))
print('Giá trị là: ',pow(x,2))


# cộng dãy số: S= 1+2+3+4+....+N
#---------------------------------------------------------------------
n = int(input('Nhập vào N= '))
s=0;
i=1;
while i<=n:
    s+=i
    i+=1
print('Tổng: ',s)



# HỌC FOR
#---------------------------------------------------------------------

for m in range(10):
    print('In= ',m, end= ' ')



#nhập vào 1 số nếu số đó là lẻ thị tính tổng lẻ, nếu chẵn thì tính tổng chẵn
#S= 1+2+...+n
#---------------------------------------------------------------------

n= int(input('Nhập vào số n= '))
s=0;
if n%2==0:
    for x in range(2, n+1,2):
        s +=x
else:
    for x in range(1,n+1,2):
        s+=x
print('Tổng', s)


#---------------------------------------------------------------------

print ("chao may nhe")
a = ['hello manh', 'long', 'kien']
for inhobo in a:
    print ("day la: ", inhobo)

for line in 'python':
    print ("Text in: ", line)
c = 1
if  c> 3:
    print ("con meo dang yeu")
elif c<2:
    print ("tao yeu may")
d = 2
f = c+d
print("{0} + {1} ={2}".format(c,d,f))



# câu lệnh break trong while
#---------------------------------------------------------------------
while True:
    x =int(input('Nhập vào x= '))
    print(x, 'là số chẵn' if x%2==0 else 'là số lẻ')
    hoi= input('Bạn có muốn tiếp tục không? (c/k)?: ')
    if hoi =='c':
        break
print('bye, cút đi')




# câu lệnh break trong for
#---------------------------------------------------------------------
"""n= int(input('Nhập vào n= '))
s=0;
for x in range(1,n+1,1):
    s +=x
    if x>15:
        break
print('Tổng: ',s)"""




# câu lệnh continue
#---------------------------------------------------------------------

n=15
s=0

for x in range(1,n+1,2):
    if x == 3 or x == 11:
        continue
    s+= x
print('s: ', s)




# câu lệnh while / else
#---------------------------------------------------------------------

count = s = 0
while count < 5:
    val= int(input('Nhập giá trị: '))
    if val <0:
        print('Nhập sai quy tắc!')
        break
    s+=val
    count +=1
else:
    print('Trung bình', s/count)



# câu lệnh for / else
#---------------------------------------------------------------------
#
a= int(input('Nhập số nguyên: '))
s=0

for n in range(5,10):
    if 4 % a is 1:
        print('ngừng for')
        break
    s+=n
else:
    print('sum= ',s)





# VÒNG LẶP LỒNG NHAU
# ---------------------------------------------------------------------

n= int(input('Nhập chiều sao n= '))
for i in range(n):
    for j in range(n):
        if j==0 or i==j or j==n-1:
            print("*", end='')
        else:
            print(' ', end= '')
    print()

# --------------------
n= int(input('Nhập chiều cao= '))
i= 0
while i < n:
    j=0
    while j < n:
        if j is 0 or j is i or j is n-1:
            print("*", end='')
        else:
            print(" ",end='')
        j+=1
    i+=1
    print()



# ÔN TẬP
# ---------------------------------------------------------------------


#TÍNH DÃY SỐ
# ---------------
x= int(input('Nhập vào x= '))
n= int(input('Nhập vào n='))
s=0
def giaithua(n):
    if n ==0:
        return 1
    return n*giaithua(n-1)
for n in range(1,n+1):
    s+= (x**n)/giaithua(n)
print('kết quả', s)

### CÁCH 2: dùng 2 vòng for

x= int(input('Nhập vào x= '))
n= int(input('Nhập vào n='))
s=0
for i in range(1,n+1):
    tu = x **i
    mau = 1
    for j in range(1,i+1):
        mau *= j
    s+= (tu/mau)
print("Tổng S({0},{1})={2}".format(x,n,s))


### KIỂM TRA SỐ NGUYÊN TỐ
# ---------------
while True:
    n= int(input('Nhập vào 1 số nguyên dương: '))
    dem =0
    for i in range(1,n+1):
        if n % i ==0:
            dem +=1
    if dem ==2:
        print('Sô đó là sô nguyên tố')
    else:
        print('Không là số nguyen tố')
    hoi = input('Bạn có muốn tiếp tục k?(c/k)=')
    if hoi =='k':
        break


### XUẤT BẢNG CỬA CHƯƠNG
# ---------------

for i in range(1,11):
    t=1
    for j in range(2,10):
        t=j*i
        print('{0:>1}*{1:>2}={2:>2}'.format(j,i,t), end='\t\t')
    print()



#           ÔN TẬP2
# ---------------------------------------------------------------------



# vẽ hình
# --------------------------------------

n= int(input('Nhập chiều sao n= '))
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==n-1 or j==n-1:
            print("*", end=' ')
        else:
            print(' ', end= ' ')
    print()
#-----------
n= int(input('Nhập chiều sao n= '))
for i in range(n):
    for j in range(n):
        if i==n-1-j or i==n-1 or j==n-1 or i==n-j or i==n+1-j or i==n+2-j or i ==n+3-j:  # chưa làm đc vs while
            print("*", end=' ')
        else:
            print(' ', end= ' ')


    print()

    # tính S(x,n)
    # --------------------------------------
x= int(input('Nhập x= '))
n= int(input('Nhập n= '))
s=0
def giaithua(x):
    if x==0:
        return 1
    return x*giaithua(x-1)

for i in range(n+1):
    s+= (x**(2*i+1))/giaithua(2*i+1)
print('Tổng S({0},{1})={2} '.format(x,n,s))


