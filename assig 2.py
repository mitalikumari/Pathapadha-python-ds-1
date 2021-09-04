# WAP to find wheather a number is armstrong number or not.


num = int(input("Enter a number "))
sum = 0
temp = num
while temp>0:
  digit = temp%10
  sum+= digit**3
  temp//= 10
if(sum == num):
  print(num,"is an armstrong number")
else:
  print(num,"is not an armstrong number")


# WAP to print the sum of digits of a number

num = int(input("Enter a number "))
sum = 0
temp = num
while temp>0:
  digit = temp%10
  sum+= digit
  temp//= 10
print("sum of digits of",num,"is :",sum)
