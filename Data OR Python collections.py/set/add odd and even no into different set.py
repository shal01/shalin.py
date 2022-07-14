# s={1,2,44,55,66,8,9,22,43,67,89}
# odd=set()
# even=set()
# for i in s:
#     if i%2==0:
#         even.add(i)
#     else:
#         odd.add(i)
# print(even)
# print(odd)

set1={1,2,3,4,5,6}
cube=set()
sum=1
for i in set1:
    sum=i*i*i
    cube.add(sum)
print(cube)
