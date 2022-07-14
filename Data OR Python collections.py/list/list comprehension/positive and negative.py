# l=[-1,2,-3,4,5,-9,-10,-16]
# neg=[]
# pos=[]
# for i in l:
#     if i<0:
#         neg.append(i)
#     else:
#         pos.append(i)
# print(neg,pos)


l=[-1,2,-3,4,5,-9,-10,-16]
neg=[i for i in l if i<0]
pos=[i for i in l if i>0]
print(neg,pos)