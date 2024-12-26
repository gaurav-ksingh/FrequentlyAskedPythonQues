#method1: using clear()method
mylist=[1,2,3,4,4]
print("mylist before clear:",mylist)
mylist.clear()
print("mylist after clear:",mylist)

#method2: initialize the list with no values
mylist=[1,2,3,4,4]
print("mylist before clear:",mylist)
mylist=[]
print("mylist after clear:",mylist)

#method3:using *=0 this method
mylist=[1,2,3,4,4]
print("mylist before clear:",mylist)
mylist *=0
print("mylist after clear:",mylist)

#method4:using del method
mylist=[1,2,3,4,4]
print("mylist before clear:",mylist)
del mylist[1:3]     #[:] it removes everything
print("mylist after clear:",mylist)






