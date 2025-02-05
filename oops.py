# class student:
#     name="Ajay"
# s1=student()    #creation of object
# print(s1.name)
# s2=student()
# print(s2.name)

# class car:
#     color="red"
#     brand="BMW"
# ob1=car()
# print(ob1.color)
# print(ob1.brand)


#Constructor---  __init__() method
#All class have a function called __init__() constructor
#It gets executed every time the object is being initiated
#the self parameter is a reference of the current invoking object
#it is used to access the attributes which belongs to the class


# class student:
#     def __init__(self):
#         print(self)
#         print("adding new statement")

# o1=student()
# print(o1)

# class student:
#     def __init__(self,firstname,lastname):
#         self.fname=firstname
#         self.lname=lastname

# o1=student("ajay","Reddy")
# print(o1.fname,o1.lname)
# o2=student("vijay","kumar")
# print(o2.fname,o2.lname)

# class student:
#     def __init__(self,name,marks):
#         self.nm=name
#         self.mr=marks
#     def get_avg(self):
#         sum=0
#         for i in self.mr:
#             sum=sum+i
#         print("Hello",self.nm,"ypur average marks is :",sum/3)

# s1=student("Ajay",[10,20,30])
# s1.get_avg()






































































































