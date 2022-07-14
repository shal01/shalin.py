l=[-1,2,-3,4,5,-9,-10,-16]
# even=[]
# for i in l:
#     if i>0:
#         if i%2==0:
#             print(i)
#             even.append(i)
poseven=[i for i in l if i>0 and i%2==0]
print(poseven)

