def sum(num):
    s=0
    for i in num:
        s+=i
    return s


a=int(input("Enter no of element:"))
b=[]
for n in range(1,a+1):
    b.append(n)
print(sum(b))