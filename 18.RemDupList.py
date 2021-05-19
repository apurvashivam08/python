def remove(l):
    a=[]
    for i in range(0,len(l)):
        if l[i] not in a:
            a.append(l[i])
    return a

inp=int(input("Enter no of elements: "))
l=[]
for i in range(0,inp):
    b=int(input(f"Enter num {i+1}: "))
    l.append(b)
print(remove(l))