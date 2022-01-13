from file import *

dssp=docfile("testDB.txt")
print(dssp)

def xuatsp(dssp):
    for row in dssp:
        for element in row:
            print(element,end='\t')
        print()
    print()
xuatsp(dssp)

#sort 
def sapxepsp(dssp):
    for i in range(len(dssp)):
        for j in range(len(dssp)):
            a=dssp[i]
            b=dssp[j]
            if a[2] > b[2]: #=> vtri dongia = 2
                dssp[i] = b
                dssp[j] = a

sapxepsp(dssp)
print("sau khi săp: ")
xuatsp(dssp)