def duplicate(string):
    result=""
    for c in string:
        if c not in result:
            result+= c
    return result

a=input("Enter a string:")
print(duplicate(a)) 