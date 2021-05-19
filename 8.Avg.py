a=int(input("Enter num of elements:"))
sum=0
avg=0
for n in range(1,a+1):
    b=int(input(f"Enter num {n}: "))
    sum=sum+b
    avg=sum/n
print(f"Avg is {avg}")

