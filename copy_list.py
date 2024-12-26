#method1:using slicing method
# mylist=[3,4,5,6,7,8]
# mylist_copy=mylist[:]
# print(mylist_copy)

#method2:using extend()method
mylist=[3,4,5,6,7,8]
mylist_copy=[]
mylist_copy.extend(mylist)
print(mylist_copy)

#method: using the list() method
mylist=[3,4,5,6,7,8]
mylist_copy=list(mylist)
print(mylist_copy)

#method4:using copy method

mylist=[3,4,5,6,7,8]
mylist_copy=mylist.copy()
print(mylist_copy)

#method5:comprehensive list approach

mylist=[3,4,5,6,7,8]
mylist_copy=[i for i in mylist]
print(mylist_copy)

















