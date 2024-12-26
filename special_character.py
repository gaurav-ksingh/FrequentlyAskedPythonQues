import re
str = "welcome@@2to%%python**programming!!%^@$"

regex=re.compile('[%@*!^$)<>?/\|}{~:]')
if(regex.search(str)==None):
    print("no special characters present in a string")

else:
    print("string contains special characters")