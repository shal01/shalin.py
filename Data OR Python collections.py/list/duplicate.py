l=[1,2,3,4,5,6,1,2,3,4]
dupl=[]
for i in l:
    if i not in dupl:
        dupl.append(i)
    else:
        print(i)