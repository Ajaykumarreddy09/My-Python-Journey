#List Comprehension:
#List Comprehension is an easy to read,compact and elegant way of creating a list from  any existing iterable object.such as list, tuple, or range.
#Ex: squares=[x**2 for x in range(10)] print(squares)

# l=[x for x in range(1,102)]
# print(l)

# l=[x**2 for x in range(1,101)]
# print(l)

# l=[x**2 for x in range(1,101,2)]
# print(l)

# l=[x**2 for x in range(1,101) if x%2!=0]
# print(l)

# l=[x**2 for x in range(0,101) if x%2==0]
# print(l)

# a='12 13 14 1 2 3 4'.split()
# print(a)

# l=[int(x) for x in input("Enter multiple inputs:").split()]
# print(l)

# l=[]
# for i in range(1,10):
#     l.append(i)
# print(l)

# l=[]
# n=int(input())
# for i in range(n):
#     num=int(input())
#     l.append(num)
# print(l)

# l=[]
# for i in range(5):
#     l.append(int(input()))
# print(l)


#dictionary comprehension

# d={x: x**2 for x in range(5)}
# print(d)

# d={}
# for i in range(5):
#     d[i]=i**2
# print(d)

#String Slicing
# there are 2 ways to slice the string:1.slice constructor

s='ABCDEFGHIJ'
#print(s[1:5])
#print(s[-1:-4:-1])#when we are going from the backside we must mention the step length in negative number only.
#print(s[::-1])#For reversing the string
# print(s[::1])

 #module is a simple python file that contains collection of functions and global variables and with having  .py extension






































































