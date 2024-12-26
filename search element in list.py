mylist=[1,2,3,4,5,6,77,99]
ele=4
flag=0
for i in mylist:
    if(i==ele):
        print("element found")
        flag=1
        break
if(flag==0):
    print("element not found")

#method2:in operator
mylist=[1,2,3,4,5,6,77,99]
ele=4
if(ele in mylist):
    print("element found")
else:
    print("element not found")







