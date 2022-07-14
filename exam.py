# ini=int(input("enter initial range : "))
# final=int(input("enter final range : "))
#
# for i in range(1,6):
#     for j in range(i):
#         print(ini,end=" ")
#         print()
#     ini=ini+1
# for i in range(6,1):
#     for j in range(i):
#         print(ini,end=" ")
#         print()
#     ini=ini+1
# for i in range(1,6):
#     for j in range(i):
#         print(ini,end=" ")
#         print()
#     ini=ini+1
# for i in range(6,1):
#     for j in range(i):
#         print(ini,end=" ")
#         print()
#     ini=ini+1
# for i in range(1,6):
#     for j in range(i):
#         print(ini,end=" ")
#         print()


# a=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

# e=[3, 5, 7, 9, 0, 8, 55, 34, 23, 76, 4, 65, 12, 89, 56, 76, 34, 289, 49, 12, 63, 976]
# null = []
# while e:
#     min = e[0]
#     for i in e:
#         if i < min:
#             min = i
#     null.append(min)
#     e.remove(min)
# print(null)
# print(null[1])

#
# user=input("enter a word : ")
# l=[]
# e=['a']
# for i in user:
#     user=i.rstrip('\n').split(" ")
#     l.extend(user)
# count={}
# for i in l:
#     if i not in count:
#         count.update({i:1})
#     else:
#         val=count[i]
#         val+=1
#         count.update({i:val})
# print(l)
# print(count)
# for i in count:
#     if i in e:
#         print({i:val})



# e=input('enter word = ')
# c=0
# for i in e:
#     if i=='a':
#         c+=1
# print("count of a is =",c)

# b=[3,77,0,5,33,6,22,5,90,32,56,78,98,54,67,11,34,88]
# lastindex=len(b)-1
# mid=lastindex//2
# b.remove(b[mid])
# print(b)

def odd(e):
    initial=40