#method 1: using loop
mylist=[15,6,7,10,12,20,10,26,10]
x=10
count=0
for ele in mylist:
     if(ele==x):
         count=count+1
     print("{}has occured{} times".format(x,count))

#method2: using count()

mylist=[15,6,7,10,12,20,10,26,10]
x=10
print("{}has occured{} times".format(x,mylist.count(x)))

#method3
from collections import Counter
mylist=[15,6,7,10,12,20,10,26,10]
x=10
dic=Counter(mylist)
print(dic)