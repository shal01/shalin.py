# def prime():
#      num = int(input("enter a number:="))
#      for i in range(2,num):
#          if num%2==0:
#             print("not prime")
#             break
#      else:
#             print("prime")
# prime()

# def prime():
#     initial=int(input("enter a initial value:"))
#     final=int(input("enter a final value:"))
#     # num = int(input("enter a number:="))
#     for n in range(initial,final+1):
#         for i in range(2,n):
#             if n%2==0:
#                 break
#         else:
#             print(n)
# prime()

#function with arguments and return type

def prime(initial,final):
    # num = int(input("enter a number:="))
    for n in range(initial,final+1):
        for i in range(2,n):
            if n%2==0:
                break
        else:
            print(n) 
print(prime(12,43))