inp=int(input("Enter a number: "))
rev=0
while(inp>0):    #153
    r=inp%10     #3,5,1
    rev=rev*10+r #3,35,351
    inp//=10    
print(rev)