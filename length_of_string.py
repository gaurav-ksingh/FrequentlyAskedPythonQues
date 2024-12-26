#method 1: using for loop
str="welcome"
counter=0
for i in str:
    counter=counter+1
print(counter)

#method2:using while loop along with slicing
str="welcome"
counter=0
while str[counter:]:
    counter=counter+1
print(counter)


#method3: using builtin method function len()
str="welcome"
print(len(str))
