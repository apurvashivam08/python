def decrese(l):
    a=sorted(l, reverse=True)
    return a



inp=int(input("Enter no of elements: "))
l=[]
for i in range(0,inp):
    b=int(input(f"Enter num {i+1}: "))
    l.append(b)
print(f"Original list{l}")
print(f"Reversed List{decrese(l)}")