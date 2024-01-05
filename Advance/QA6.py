# Create the custom python classes which has methods and attributes and implement single inheritance, multiple inheritance and multilevel inheritance

class A:
    def display(self):
        print("Display of A")

class B(A):
    def func1(self):
        print("func1 of B")

class C(B):
    def func2(self):
        print("func2 of B")

class D(A, B, C):
    def fun3(self):
        print('fun3 of B')

a = A()
b = B()
c = C()
c = D()

a.display()
b.display()
c.display()
d.display()
