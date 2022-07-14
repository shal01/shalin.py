# Same method name and Arguments

# child class method override parent class method

class Parent:
    def selectmobile(self):
        print("take samsung a11")
class Child:
    def selectmobile(self):
        print("take iphone 13")
class Secondchild:
    def selectmobile(self):
        print("take pixel")
c=Secondchild()
c.selectmobile()


# example
# class A:
#     def select(self):
#         print(1)
# class B:
#     def select(self):
#         print(3)
# class C:
#     def select(self):
#         print(4)
# class D:
#     def select(self):
#         print(4)
# c=D()
# c.select()