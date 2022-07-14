#0 1 1 2 3
def recfib(n):
    if n<=1:     #0 1
        return n
    else:
        return recfib(n-1)+recfib(n-2)
            #recfib(2-1)+recfib(2-2)  =1+0
            #recfib(2)+recfib(1)      =1+1=2
            # recfib(3)+recfib(2)     =2+1=3

for i in range(10):       #0 1 2
    print(recfib(i))
# recfib(0)=0
# recfib(1)=1
# recfib(2)=1
# recfib(3)=2
# recfib(4)=