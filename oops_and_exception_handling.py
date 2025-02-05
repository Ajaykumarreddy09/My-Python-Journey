#OOPS
#priciples:
# classes and objects , encapsulation, abstraction, polymorphism, Inheritance
#self parameter: it is a reference to the currect instance of a class and it is used to access the variables belongs to that class

# class Person:
#     def name(self):
#         print("my name is ajay")
#     def desg(self):
#         print("developer")
# p=Person()
# p.name()
# p.desg()

#constructor : constructor is a special type of method that is called instantiates an object using definition found in the class
# it is normally used to initialize instance variables
#default constructor:
#A constructor without parameters is called default constructor or zero parameterized constructor. Every object is initialized with same data.

# class Person:
#     def __init__(self):
#         self.name="Ajay"
#         self.age=21
#     def display(self):
#         print("name: ",self.name)
#         print("Age is:",self.age)
# p=Person()
# p.display()

#2.Parameterized constructor:
#A constructor with parameters is called parameterized constructor. here, every object is initialized with different data.

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("name:",self.name)
#         print("age:",self.age)
# p=Person("ajay",21)
# p1=Person("vijay",21)
# p.display()
# p1.display()

#Access modifiers:
#1.Public 
# class Employee:
#     def __init__(self,name,sal):
#         self.name=name
#         self.sal=sal
# E=Employee("ajay",12)
# print(E.name)
# print(E.sal)

#private
# class employee:
#     def __init__(self,name,sal):
#         self.__name=name 
#         self.__sal=sal
# e=employee("jhon",30000)
# print(e.__name)

#Protected
# class employee:
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
# class hr(employee):
#     def task(self):
#         print("assign work to employee")
# e=employee('aj',21)
# print(e._name)
# print(e._age)
# h=hr('ajay',21)
# print(h._name)
# print(h._age)
# h.task()


#inheritance
#1.single inheritance-->it enables a derived class to inherit properties from a single parent class
# class parent:
#     def display(self):
#         print("it is parent class")
# class child(parent):
#     def display1(self):
#         print("its a child class")
# c=child()
# c.display()
# c.display1()

#2.Multi-level inheritance-->you can inherit a derived class from another derived class.
# class person:
#     def display(self):
#         print("class person")
# class employee(person):
#     def printing(self):
#         print("derived class")
# class programmer(employee):
#     def show(self):
#         print("this is another derived class ")
# p=programmer()
# p.printing()
# p.display()
# p.show()

#Multiple inheritance: deriving a child class from more than one base class is called multiple inheritance

# class land_animal:
#     def printing(self):
#         print("this animal lives on land")
# class water_animal:
#     def display(self):
#         print("this animal lives in water")
# class frog(land_animal,water_animal):
#     pass
# class croc(land_animal,water_animal):
#     pass
# f=frog()
# f.printing()
# f.display()
# c=croc()
# c.display()
# c.printing()

#hierarchical inheritance: it involves multiple inheritance from the same base or parent class
# class details:
#     def __init__(self):
#         self.__id="<no id>"
#         self.__gender="<no gender>"
#     def setData(self,id,name,gender):
#         self.__id=id
#         self.__name=name
#         self.__gender=gender
#     def showdata(self):
#         print("id:",self.__id)
#         print("name:",self.__name)
#         print("gender:",self.__gender)
# class employee(details):
#     def __init__(self):
#         self.__company="<no company"
#         self.dept="<no dept>"
#     def setemployee(self,id,name,gender,company,dept):
#         self.setData(id,name,gender)
#         self.__company=company
#         self.dept=dept
#     def showEmployee(self):
#         self.showdata()
#         print("company:",self.__company)
#         print("department:",self.dept)
# class doctor(details):
#     def __init__(self):
#         self.__hospital="<no hsp>"
#         self.dept="<no dept>"
#     def setemployee(self,id,name,gender,hosp,dept):
#         self.setData(id,name,gender)
#         self.__hosp=hosp
#         self.dept=dept
#     def showemployee(self):
#         self.showdata()
#         print("hospital:",self.__hosp)
#         print("dep:",self.dept)
# def main():
#     print("Employee object")
#     e=employee()
#     e.setemployee(1,'aj','male','gmr','excavatiom')
#     e.showEmployee()
#     print("doctor object:")
#     d=doctor()
#     d.setemployee(2,'aja','male','aims','eyes')
#     d.showemployee()
# if __name__=="__main__":
#     main()

#str() and repr()
# s="india"
# print(str(s))
# print(repr(s))
# a=23.3
# print(str(a))
# print(repr(a))

#class attributes
# class sample:
#     count=0
#     def increase(self):
#         sample.count=sample.count+1
# s=sample()
# s.increase()
# print(s.count)
# s1=sample()
# s1.increase()
# print(s1.count)

#class methods: it recieves the class as implicit first argument just like an instance method receives the instance.
# class methods and static method
# from datetime import date

# from datetime import date

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birth_year(cls, name, birth_year):
#         return cls(name, date.today().year - birth_year)

#     @staticmethod
#     def is_adult(age):
#         return age >= 18

# # Example usage
# p = Person('John', 23)
# p2 = Person.from_birth_year('Richard', 1990)
# print(p.age)        # Prints: 23
# print(p2.age)       # Calculates age based on birth year and prints it
# print(Person.is_adult(23))  # Prints: True
# print(Person.is_adult(15))  # Prints: False

#polymorphism
# class tomato:
#     def type(self):
#         print("vegetables")
#     def color(self):
#         print("red")
# class Apple:
#     def type(self):
#         print("fruit")
#     def color(self):
#         print("green")
# def fun(obj):
#     obj.type()
#     obj.color()
# t=tomato()
# a=Apple()
# fun(t)
# fun(a)

# class india:
#     def cap(self):
#         print("delhi")
#     def lang(self):
#         print("telugu")
# class usa:
#     def cap(self):
#         print("newyork")
#     def lang(self):
#         print("english")
# i=india()
# u=usa()
# for country in (i,u):
#     country.cap()
#     country.lang()

#method overloading: writing one or more methods with same name but different in the arguments is called method overloading
#it is used in a single class
#it is used to write the code clearly and as well as reduce the complexity

# class Area:
#     def find_area(self,a=None,b=None):
#         if a !=None  and b!=None:
#             print("area of rectangle is:",(a*b))
#         elif a!=None:
#             print("area of square",(a*a))
#         else:
#             print("nothing found")
# obj1=Area()
# obj1.find_area()
# obj1.find_area(10)
# obj1.find_area(2,3)

#method overriding:
#writing one or more methods with the same arguments is called method overriding.
#implemented using inheritance and mostly used for memory reduction process
# class rectangle:
#     def __init__(self,l,b):
#         self.length=l
#         self.breath=b
#     def getArea(self):
#         print("area of rectangle is:",self.length*self.breath)
# class square(rectangle):
#     def __init__(self,s):
#         self.side=s
#         # rectangle.__init__(self,s,s)
#     def getArea(self):
#         print("are of square is:",self.side*self.side)
# sq=square(4)
# r=rectangle(2,4)
# sq.getArea()
# r.getArea()

#super()--> this function is used to givr access to the methods and properties of a parent class or sibling class.
#this function returns an object that represents parent class. super() is always written in the subclass only.
# class parent:
#     def __init__(self,txt):
#         self.message=txt
#     def printmessage(self):
#         print(self.message)
# class child(parent):
#     def __init__(self,txt):
#         super().__init__(txt)
# x=child("this is super() function")
# x.printmessage()

#exception handling:
#an exception is an event ,which occurs during the execution of a program that disrupts the normal flow of prg instructions.
#types:1.Exception,2.Arithmetic error,3.overflow error, 4.zero division error, 5.Assertion error, 6.Import error, 7. Index error
# ,key error, IO error, value error, type error, name error

# x=input("enter numberr1:")
# y=input("enter number 2:")
# try:
#     z=int(x)/int(y)
# except Exception as e:
#     print("exception occured:",e)
# # print(z)

#user defined exceptions

# import sys
# random_list=['a','%',5]
# for entry in random_list:
#     try:
#         print("entry is:",entry)
#         r=15/int(entry)
#         break
#     except:
#         print("oops!",sys.exc_info()[0],"occured")
#         print("next entry")
#         print()
# print("the reciprocal of",entry,"is",r)

# class Error(Exception):
#     "base class for other classes"
#     pass
# class valueToosmallError(Error):
#     "raised when the input value is too small"
#     pass
# class valueTooLargeError(Error):
#     "raised when the input value is too large"
#     pass
# number=10
# while True:
#     try:
#         i_num=int(input("Enter a number: "))
#         if i_num<number:
#             raise valueToosmallError
#         elif i_num>number:
#             raise valueTooLargeError
#         break
#     except valueToosmallError:
#         print("this value is too small try again")
#         print()
#     except valueTooLargeError:
#         print("this value is too large try again")
#         print()
# print("congractulations! you gussed it correctly")

#finally: In case if there is any code which the user want to execute irrespective of the exception

# def divide(x,y):
#     try:
#         res=x//y
#     except ZeroDivisionError:
#         print("sorry you divided by zero")
#     else:
#         print("your answer:",res)
#     finally:
#         print("finally block")
# divide(12,0)
# divide(1,2)

#code2:code raise error but we dont have any except clause to handle it. so clean up action is taken first and the error is raised by default by compiler

# def divide(x,y):
#     try:
#         res=x//y
#     except ZeroDivisionError:
#         print("sorry! you are divided by zero")
#     else:
#         print("your answer:",res)
#     finally:
#         print("finally block")
# divide(2,'a')





































































































