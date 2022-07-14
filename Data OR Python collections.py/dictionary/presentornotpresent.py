d={1:'a',2:'b',3:'c',4:'d',5:1,6:2,7:3}
# e=int(input("enter a num"))
# d.keys()
# if e in d.keys():
#         print("present")
# else:
#     print("not present")

# if e in d:
#     print("present")
# else:
#     print("not present")


def keycheck(e):
    if e in d:
        print("present")
    else:
        print("not present")
e=int(input("enter a num"))

keycheck(e)
