def merge(m,n):
    s=m+n
    s.sort()
    return s

a=int(input("Enter range of list 1: "))
l1=[]
for i in range(0,a):
    b=int(input(f"Enter element {i+1}: "))
    l1.append(b)
c=int(input("Enter range of list 2: "))
l2=[]
for i in range(0,c):
    d=int(input(f"Enter element {i+1}: "))
    l2.append(d)
print(f"Original List1: {l1}")
print(f"Original List2: {l2}")
print(f"Sorted list :{merge(l1,l2)}")