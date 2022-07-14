# Global and local variable
y=6
def printx():
    global  x,y
    y=y+1
    x=10
    print(x,y)
printx()
print(x)
print(y)

def printx2():
    print(x)
printx2()

