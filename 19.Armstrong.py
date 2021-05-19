inp=int(input("Enter a number: "))
sum=0
temp=inp
while (temp>0):
    r=temp%10 #takes out digits from r to l
    # print(r)
    sum+=(r*r*r)
    temp//=10 #floor div of inp
    print(temp)
if inp==sum:
    print("No is armstrong")
else:
    print("No is not armstrong")
