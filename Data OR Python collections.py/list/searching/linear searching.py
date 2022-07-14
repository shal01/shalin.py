# linear searching
# l=[1,2,3,4,99,65,6,7,55,44,33,22]
# e=int(input("enter element to search:"))
# if e in l:
#     print("present")
# else:
#     print("not present")

# for loop'

l=[1,2,3,4,99,65,6,7,55,44,33,22]
e=int(input("enter element to search:"))
# for i in l:
#     if e in l:
#         print("present")
#         break
# else:
#     print("not present")


# for i in l:
#     if i==e:
#        print("present")
#        break
# else:
#     print("not present")


for i in l:
    if i==e:
        f=1
        break
if f==0:
    print("not present")
else:
    print("present")
