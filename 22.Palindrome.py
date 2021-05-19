inp=int(input("Enter a number: "))
temp=inp
rev=0
while(temp>0):
    r=temp%10
    rev=rev*10+r
    temp//=10
if (inp==rev):
    print("Palindrome Number")
else:
    print("Not Palindrome Number")