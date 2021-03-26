from file import *

dssp=docfile("datatest.txt")
print(dssp)

def xuatsp(dssp):
    for row in dssp:
        for element in row:
            print(element,end='\t')
        print()
    print()
xuatsp(dssp)


def sapxepsp(dssp):
    for i in range(len(dssp)):
        for j in range(len(dssp)):
            a= dssp[i]
            b= dssp[j]
            if a[2] > b[2]:
                dssp[i] = b
                dssp[j] = a

sapxepsp(dssp)
print("sau khi săp: ")
xuatsp(dssp)