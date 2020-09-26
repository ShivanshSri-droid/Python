x = int(input("Enter a decimal number "))
list1 = []
str1 = " "
while x >= 8:
    y = x % 8
    list1.append(y)
    x = int((x-y)/8)
list1.append(x)
list2 = list1[::-1]    
print("The Octal number is :")
str1 = ' '.join(str(e) for e in list2)
print(str1)    