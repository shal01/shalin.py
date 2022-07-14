# n=5
# fact = 1
# for i in range(1, n + 1):
#     fact = fact * i
# print(fact)

#1,2,3,4,5
#       n-1 n

def recfact(n):   #1
    if n==1:
        return 1
    else:
        return n*recfact(n-1)         #5*recfact(4)
                                       # 4*recfact(3)
                                       #      3*recfact(2)
                                        # 2*recfact(1)
                                            #  1
print(recfact(5))

