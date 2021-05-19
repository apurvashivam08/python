def sum(n):
    sum=0
    for i in range(1,n+1):
        sqr=(i**2)
        sum+=sqr
    return sum
a=int(input("Enter a number"))
s=sum(a)
print(s)