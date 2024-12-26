mylist=[5,10,15,20]
total=1
for i in range(0,len(mylist)):
    total=total*mylist[i]
print("multiply all elements in given list: ",total)

#method2
mylist=[2,3,4]
result = 1
for x in mylist:
    result=result*x
print(result)

#method3
import numpy
mylist=[3,2,4]
result=numpy.prod(mylist)