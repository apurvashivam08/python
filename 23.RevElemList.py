def reverse(l):
    a=[]
    for i in range(0,len(l)):
        r=l.pop()
        a.append(r)
    return a

inp=int(input("Enter no of elements: "))
l=[]
for i in range(0,inp):
    b=int(input(f"Enter num {i+1}: "))
    l.append(b)
print(f"Original list{l}")
print(f"Reversed List{reverse(l)}")