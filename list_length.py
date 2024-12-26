#approach1
myList=[1,4,6,7,8]
print(myList)
count=0
for i in myList:
    count=count+1
print("length of list is:",count)

#approach2
myList=[1,4,6,7,8,6,7,]
print(myList)
print("length of list is:",len(myList))