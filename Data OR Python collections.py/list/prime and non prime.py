l=[1,2,3,4,5,6,7,8,9,10]
prime=[]
nonprime=[]
for i in l:
    for n in range(2,i):
        if i%2==0:
            nonprime.append(i)
            break
    else:
         prime.append(i)
print(prime)
print(nonprime)