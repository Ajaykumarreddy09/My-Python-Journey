#fibonacci series
""" def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(n):
        c=a+b
        print(c)
        a=b
        b=c

fib(int(input("Enter a number"))) """

#if we want only one number and if n is invalid 
""" def fib(n):
    a=0
    b=1
    if n<0:
        print("enter a valid number")
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(n):
            c=a+b
            print(c)
            a=b
            b=c
           

fib(int(input("Enter a number:"))) """

#pattern
""" for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print() """

#o/p:
""" 
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5 """


# for i in range(1,6):
#     for j in range(i):
#         print(i,end=" ")
#     print()



# #o/p:
# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


# for i in range(6):
#     for j in range(i):
#         print("*",end="")
#     print()

#o/p:
# *
# **
# ***
# ****
# *****

""" for i in range(6):
    for j in range(j):
        print("*",end=" ")
    print() """

#functions

# def odd_no(a):
#     for i in range(1,a,2):
#         print(i,end=" ")

# odd_no(10)
# odd_no(99)

# for i in range(65,91):
#     print(chr(i),end=" ")

# for i in range(97,123):
#     print(chr(i),end=" ")

# max_num=lambda a,b: a if a>b else b
# result=max_num(8,5)
# print(result)

# nums=[1,2,3,4,5,6,7,8,9]
# even_nums=list(filter(lambda x: x%2==0,nums))
# print(even_nums)

# nums=[1,2,3,4,5,6,7,8,9]
# squre_nums=list(map(lambda x: pow(x,2),nums))
# print(squre_nums)


#lambda function for square of a num
# square=lambda a: a*a
# print(square(5))

# c_t_f=lambda c: (c*9/5)+35
# print(c_t_f(50))

# t=[(1,2),(3,1),(5,4),(2,3)]
# sorted_t=sorted(t,key=lambda x:x[1])
# print(sorted_t)

#program to write if the num is palindrome or not

# def palindrome(num):
#     rev=""
#     n2=str(num)
#     for i in n2:
#         rev=i+rev
#     n3=int(rev)
#     print(n3)
#     if num==n3:
#         print("its a palindrome") 
#     else:
#         print("its not a palindrome")
    
# num=int(input())
# palindrome(num)


#methods
# append() Method
# a=[]
# for i in range(1,100,2):
#     a.append(i)
# print(a)

# Extend() method...we can append any no.of items at a time
# fruits=['apple','banana','garape']
# fruits.extend(['jackfruit','pineapple','kiwi'])
# print(fruits)

# #clear()
# a=[1,2,3,4,5]
# a.clear()
# print(a)

#copy()
# a=[1,2,3,4]
# b=a.copy()
# print(b)

#count()

# a=[1,2,3,4,4,4,2]
# count=a.count(2)
# print(count)

#index()...returns the index
# a=[1,2,3,4,5]
# i=a.index(2)
# print(i)

#insert

# l=[1,2,3,4,5]
# l.insert(1,6)
# print(l)

#pop()
# l=[1,2,3,4,5]
# l.pop()
# print(l)
# l.pop(1)#index is specified
# print(l)

# #remove
# l=[1,2,3,4,5,1]
# l.remove(1)#only the first occurence is removed
# print(l)

#reverse()
# l=[1,2,3,4,5]
# l.reverse()
# print(l)

# #sort()
# l=[1,2,6,3,4,5]
# l.sort()
# print(l)

#tuples methods
# t=(1,2,3,4,5,2)
# c=t.count(2)
# print(c)

#dictionary methods
#clear(),copy(),get(),items(),pair(),keys(),pop(),popitem(),updatepairs(),values()

# d={1:'a',2:'b',3:'c',4:'d'}
# d.clear()
# print(d)

#copy()
# d={1:'a',2:'b',3:'c',4:'d'}
# c=d.copy()
# print(c)

#get()
# d={1:'a',2:'b',3:'c',4:'d'}
# c=d.get(1)
# print(c)

# #items()
# d={1:'a',2:'b',3:'c',4:'d'}
# c=d.items()# we will get the items in the form of tuple
# print(c)

#key()
# d={1:'a',2:'b',3:'c',4:'d'}
# k=d.keys()#only gives keys
# print(k)

# #pop()
# d={1:'a',2:'b',3:'c',4:'d'}
# p=d.pop(1)
# print(p)
# print(d)

# #popitem()
# d={1:'a',2:'b',3:'c',4:'d'}
# p=d.popitem()
# print(d)

#update()#updates as well as appends the value
# d={1:'a',2:'b',3:'c',4:'d'}
# d.update({2:'c',5:'d'})
# print(d)

#values()
# d={1:'a',2:'b',3:'c',4:'d'}
# v=d.values()
# print(v)

#String Methods
#capitalize()-->first char to upper case
# endswith()-->returns true if it ends with the specified value
# count()-->no.of times specified val occurs in a String
# format()-->Formats specified valies in a string
# index()-->serches the string for a specified value and returns the position where it was found
# isalnum()-->returns true if all char in struiung r alphanumeric
# isalpha()-->returns true if all chars in string are in alphabets
# isdigit()-->returns true if all char in str are digit
# isidentifier()-->returns true if the string is identifier
# islower()--->returns true if all char of str are lower case
# istitle()-->returns true if the string follows the rules of a title
# isupper()-->returns true if all char in string are uppercase
# join()-->joins elements of an iterable to the end of the string
# lower()-->converts the string into lower case
# istrip()-->returns a left trim version of the string
# replace()-->returns a string where a specified value is replaced with specified value
#split()-->splits string at the specified spectator and returns a list 
#splitlines()-->splits the string at line breaks and returns a list.
#startswith()--> returns true if the string starts with specified value
# swapcase()--->lowercase becomes upper case and vice versa
# strip()-->returns a trimmed version of string.
# title()-->converts the first char of each word to upper case
# upperr()-->converts string into upper case. 


#join()
# l=['a','b','c']
# jl="".join(l)
# print(jl)

# l=['a','b','c']
# jl="-".join(l)#keeps the specified one in the middle
# print(jl)

#lstrip()
# my_string=['   hello']
# s=my_string.lstrip()
# print(s)

#replace()
# s="hello,world"
# r_s=s.replace('hello','hii')
# print(r_s)

#split()
# s="hello,world"
# ss=s.split(',')
# print(ss)

#splitlines()
# s="hello \n ,world \n AI"
# ssl=s.splitlines('\n')
# print(ssl)

#startswith()
# s="hello,world"
# sw=s.startswith('h')
# print(sw)

# s="hello,world"
# sw=s.startswith('hello')
# print(sw)

#Rstrip() ...removes staces in the right
# s="helloworld welcome"
# rs=s.rstrip()
# print(rs)

#swapcase()
# s="HellO"
# sc=s.swapcase()
# print(sc)

#Title()
# s="hello world"
# st=s.title()
# print(st)

#set methods
#add()-->adds an element to the set if the ele is present already then it wont add it again
#clear()==>removes all ele from set making it empty set 
#copy()-->returns a shallow copy of set
#difference()-->Returns new set containing ele present in 1 set but not in 2 set
#difference_update()->updates set removing ele taht are present in other specified set
#discard()-->removes specified ele from set if it is present
#intersection()-->returns a new set containing elements that are commonto both sets
#intersection_update()-->updates the set keeping only ele tat are presennt in other specified set
#isdisjoint()-->returns true if the sets have no element in common other wise false
#issuperset()-->returns true if the set contains all elements of specified set other wise false
#issubset()-->returns true if all ele of the set are present in the specified set.
#pop()-->removes and returns an arbitary ele from set if set is empty then it raises a key error
#remove()-->removes the specified ele from set. if the ele is not present, it raises a key error
#symmetric_difference_update()
#union()-->returns a new set containing all the unique ele from both sets.
#update()-->updates a set by adding ele from enother set or sets.if a
# set is provided it adds all ele from set to the current set if the multiple sets are provided it adds ele from each set to current set

# l=[]
# for i in range(1,101):
#     l.append(i)
# print(l)

# import datetime as d
# now = d.datetime.now()
# print(now)

# print(now.strftime("%a"))#%A for full day  # gives day
# print(now.strftime("%w"))# week day from 1 to 6
# print(now.strftime("%B"))#gives month
# print(now.strftime("%Y"))
# print(now.strftime("%H"))
# print(now.strftime("%I"))
# print(now.strftime("%S"))

# import math
# print(math.ceil(4.4))
# print(math.floor(4.4))
# print(math.fabs(-4.4))
# print(math.factorial(5))
# print(math.fmod(4,3))
# print(math.fsum([1,2,3]))
# print(math.gcd(24,45))
# print(math.log(10))
# print(math.degrees(math.pi/2))

















