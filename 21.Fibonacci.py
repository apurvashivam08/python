inp=int(input("Enter a range: "))
t1=0
t2=1
l=[]
for i in range(0,inp):
    l.append(t1)    #0,1,1,2,3
    NextTrm=t1+t2   #1,2,3,5
    t1=t2           #1,1,2,3
    t2=NextTrm      #1,2,3,5
print(l)