#For a given number, find all the numbers smaller than the number. Numbers should be divisible by 3 and also by 5.
def div(num):
    result=[]
    for i in range(1,num):
        if i%3==0 and i%5==0:
            result.append(i)
    return result
    
a=int(input("Enter a number:"))
result = div(a)
print(result)