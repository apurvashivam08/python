a=int(input("Enter a num to check whether it's prime or not: "))
flag=True
for i in range(2,a):
    if(a%i==0):
        flag=False
        break
if flag:
    print("Num is prime")
else:
    print("Num is not prime")