'''a=[15,58,96,12,45,65,98,78,25]
print(max(a))'''
def largest(num):
    largest=num[0]
    for n in num:
        if n>largest:
            largest=n
    return largest

a=[15,58,96,12,45,65,98,78,25]
l=largest(a)
print(l)