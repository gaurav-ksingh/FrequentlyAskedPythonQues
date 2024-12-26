#1st method
mylist=[10,20,4,45,99]
mylist.sort()
print(mylist)

print("largest number is: ",mylist[-1])
print("second largest number is: ",mylist[-2])

#2nd method

mylist=[10,20,4,45,99]
new_list=set(mylist)
new_list.remove(max(new_list))
print(new_list)
