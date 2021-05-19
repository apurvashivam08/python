def num(a):
    if (a>0):
        num(a-1)
        print(a)
    

a=int(input("Enetr no upto you want to print:"))
num(a)