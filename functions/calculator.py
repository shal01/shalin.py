def add(x,y):
    return x+y
def subt(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y
while True:
    options=(input("select option  \n1.add \n2.subs \n3.mult \n4.div \n5.stop "))
    if options=='5':
        break
    else:
        if options in "1234":
            num1=int(input("enter num1="))
            num2=int(input("enter num2="))
            if options=='1':
                print(add(num1,num2))
            elif options=='2':
                print(subt(num1,num2))
            elif options=='3':
                print(mult(num1,num2))
            elif options=='4':
                print(div(num1,num2))
        else:
            print("invalid options")

