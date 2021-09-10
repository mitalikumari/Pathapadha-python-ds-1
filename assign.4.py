def max_ele(lst):
  max = lst[0]

  for x in lst:
    if x > max:
      max = x
  return max

lst=[]
n = int(input("Enter number of elements in list : "))
for i in range(0,n):
  a = input("Enter element : ")
  lst.append(a)

largest = max_ele(lst)
print("Largest element in list : ",largest)


#2

def my_sort(lst):
  new_lst = []
  while lst:
    min = lst[0]  
    for x in lst: 
        if x < min:
            min = x
    new_lst.append(min)
    lst.remove(min) 
  return new_lst

lst=[]
n = int(input("Enter number of elements in list : "))
for i in range(0,n):
  a = input("Enter element : ")
  lst.append(a)

sorted_lst = my_sort(lst)
print("Sorted list is : ",end='')
for x in sorted_lst:
  print(x,end=' ')
