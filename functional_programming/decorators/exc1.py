# def eligible(funcion):
#     def wrapper(a,b):
#         if b>=18:
#             return funcion(a,b)
#         else:
#             raise Exception("not elligible")
#     return wrapper
# @eligible
# def vaccinecheck(name,age):
#     return "you can vaccinate"
# print(vaccinecheck("anu",14))


def username(fnc):
    def wrapper(a,b):
        if a=="admin":
            return fnc(a,b)
        else:
            raise Exception("not allowed")
    return wrapper
@username
def change_pin(name,pin):
    mypin=pin
    return pin
print(change_pin("hilal",9139))