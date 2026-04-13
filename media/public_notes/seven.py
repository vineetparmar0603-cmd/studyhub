# class Emp:

#     company = "IT"
#     name = "vinit"

#     def __init__(self):
#         print("this is for IT")

#     def show(self):

#         print(f"the name of the Employee is {self.name}")


# class Program(Emp):

#     company = "ITC"
#     # @classmethod
#     def showl(self):

#         super().__init__()
#         print(f"the name of the Emp is {self.name} ")
    


# a = Program()
# b = Emp()

# a.showl()
# print(a.company,b.company)

# class Employee :
#     a = 1

#     @property
#     def name(self) :
#         return self.ename
    
#     @name.setter
#     def name(self,value):
#         self.ename = value


# e = Employee()
# e.name = "vinit"
# print(e.name)

# PRACTICE SET :

# 1 .

# class TwoDVector :

#     def __init__(self,i,j):
        
#         self.i = i
#         self.j = j
    
#     def show(self):
#         print(f"the vator is {self.i}i + {self.j}j")

# class ThreeDVector(TwoDVector) :

#     def __init__(self,i,j,k):

#         super().__init__(i,j)
#         self.k =k

#     def show(self):
#         print(f"the vator is {self.i}i + {self.j}j + {self.k}k")


# a = TwoDVector(1, 2)
# a.show()
# b = ThreeDVector(1, 2, 3)
# b.show()

# 2 .

# class Animals :

#     pass

# class pets(Animals):

#     pass

# class dog(pets):

#     def bark(self):

#         print("bow bow!")

# d =dog()
# d.bark()

# 3 .

# class Employee :

#     salary = 2000
#     increment = 15

#     @property
#     def salaryafterincrement(self) :
#         return (self.salary + self.salary * (self.increment/100))

# e = Employee()
# print(e.salaryafterincrement)

# 4 .

# class Complex :

#     def __init__(self,r,i):
        
#         self.r =r
#         self.i =i

#     def __add__(self,c2):

#         return Complex(self.r + c2.r, self.i + c2.i)
    
#     def __str__(self):
#         return f"{self.r} + {self.i}i"

# c1 = Complex(1, 2)
# c2 = Complex(3, 4)

# print(c1 + c2)

 