a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
print("Before swapping the number a: ",a,"b: ",b)
temp = a
a = b
b = temp
print("After swapping the number a: ",a,"b: ",b)


swapping without using third variable
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
print("Before swapping the number a: ",a,"b: ",b)
a,b = b,a
print("After swapping the number a: ",a,"b: ",b)
