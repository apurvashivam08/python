a=int(input("Enter the order of matrix: "))
for i in range(0,a):
    for j in range(0,a):
        if(i==j):
            print("1 ",end=" ")
        else:
            print("0 ",end=" ")
    print()