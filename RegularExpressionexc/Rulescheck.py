# BASIC RULES

# x='[abc]'
# import re
# count=0
# x='\w'
# matcher=re.finditer(x,"abc helllo hai ABC@123")
# for match in matcher:
#     print(match.start()) #to get index position of match
#     print(match.group()) #to check which element or group we find
#     count=count+1
# print("total count is",count)


# QUANTIFIERS

import re
count=0
x='abc+'
matcher=re.finditer(x,"aabbbbccccca aabab abc abdf")
for match in matcher:
    print(match.start()) #to get index position of match
    print(match.group()) #to check which element or group we find
    count=count+1
print("total count is",count)