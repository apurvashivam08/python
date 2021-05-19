def OddEven(num):
    o=[]
    e=[]
    for i in num:
        if i%2==0:
            e.append(i)
        else:
            o.append(i)
    # print(f"Odd Number List: {o}")
    # print(f"Even Number List: {e}")
    return o, e
a=int(input("Enter range: "))
l=[]
for i in range(0,a):
    b=int(input(f"Enter element {i+1}: "))
    l.append(b)
print(f"Original List: {l}")
print(OddEven(l))