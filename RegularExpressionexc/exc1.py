import re
count=0
matcher=re.finditer("ab","aabbaab")
for match in matcher:
    print(match.start()) #to get index position of match
    print(match.group())# #to check which element or group we have find
    count=count+1
    print("total count is",count)