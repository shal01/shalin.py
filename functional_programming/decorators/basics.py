
def swapvalue(func):
    def wrapper(a,b):
        if a<b:
            a,b=b,a
        else:
            return func(a,b)
    return wrapper
@swapvalue
def substract(num1,num2):
    return num1-num2
print(substract(4,8))
def div(num1,num2):
    return num1/num2
print(div(4,8))