# Binary searching
#
# l=[6,1,7,4,5,5,6,7,8]
# n=int(input("enter a number to search")) #2
# l.sort()
# print(l)
# lower=0
# upper=len(l)-1
# flag=0
# while lower<=upper:
#     mid=(lower+upper)//2
#     if n<l[mid]:
#         upper=mid-1
#     elif n>l[mid]:
#         lower=mid+1
#     elif n==l[mid]:
#         flag=1
#         break
# if flag==0:
#     print("not present")
# else:
#     print("present")


    # CONVERTING INTO FUNCTION
def binarysearch(e):
    l=[6,1,7,4,5,5,6,7,8]
# n=int(input("enter a number to search")) #2
    l.sort()
    print(l)
    lower=0
    upper=len(l)-1
    flag=0
    while lower<=upper:
        mid=(lower+upper)//2
      if e<l[id]:
        upper=mid-1
    elif e>l[mid]:
        lower=mid+1
    elif e==l[mid]:
        flag=1
        break
if flag==0:
    print("not present")
else:
    print("present")








