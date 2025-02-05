#QN. Reversing a string

# s=input("Enter a string:")
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)


#check prime number or not

# The return statement inside the loop ensures that as soon as a divisor is found,
#  the function prints "It's not a prime number" and exits, avoiding any further checks.
# def is_prime(n):
#     if n==1:
#         print("its not a prime number")
#         return
#     if n==2:
#         print("its a prime number")
#         return
#     if n<=0:
#         print("its not a prime number")
#         return
#     for i in range(2,n):
#         if n%i==0:
#             print("Its not a prime number")
#             return
#     print("its a prime number")


# number=int(input("Enter a number:"))
# is_prime(number)

#factorial of a number

# def fact(n):
#     fact=1
#     if n<0:
#         print("give a valid number")
#         return
#     if n==0 or n==1:
#         print("factorial is:",n)
#         return
#     else:
#         for i in range(1,n+1):
#             fact=fact*i
#         print(fact)

# num=int(input("Enter a number:"))
# fact(num)


#FIBONACCI series 

# def fib(n):
#     a=0
#     b=1
#     if n<0:
#         print("Enter a valid number")
#     elif n==1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c=a+b
#             a=b
#             b=c
#             print(c)

# num=int(input("Enter a number:"))
# fib(num)


#count no of digits in a number

# n=int(input("Enter a number:"))
# count=0
# while(n>0):
#     r=n%10
#     count=count+1
#     n=n//10
# print(count)

#swaping of  a number using third variable

# def swap(a,b):
#     a,b=b,a
#     print(a)
#     print(b)
# swap(1,2)

# def swap(a,b):
#     temp=a
#     a=b
#     b=temp
#     print(a,"\n",b)
# swap(2,3)

# def swap(a,b):
#     a=a+b
#     b=a-b
#     a=a-b
#     print(a)
#     print(b)
# swap(2,3)

#Armstrong number -- if the sum of the powers of the individual digits count of a 
# number is equal to actual number then it is armstrong number

# def armstrong(n):
#     x=n
#     y=n
#     count=0
#     while(n>0):
#         ld=n%10
#         count=count+1
#         n=n//10
#     print(count)
#     sum=0
#     while(x>0):
#         r=x%10
#         sum=sum+(r**count)
#         x=x//10
#     print(sum)
#     if sum==y:
#      print(y,"Its an armstrong number")
#     else:
#      print(y,"Its not an armstrong number")

# n=int(input("enter a number:"))
# armstrong(n)


#Perfect number -- if the sum of the factors of the given number is equal to the given number then we call it as perfect number

# n=int(input("Enter a number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         print(i,end=" ")
#         sum=sum+i
# print("\n",sum)
# if sum==n:
#     print(n,"is a perfect number")
# else:
#     print(n,"is not a perfect number")

# def perfect_num(n):
#     sum=0
#     for i in range(1,n):
#         if n%i==0:
#             print(i,end=" ")
#             sum=sum+i
#     print("\n",sum)
#     if n==sum:
#         print("its a perfect number")
#     else:
#         print("its not a perfect number")

# perfect_num(int(input("Enter a number:")))


# STRONG NUMBER -- if the sum of the factorial of the individual digits of a given number is equal to yhe given number the it is strong number

# n=int(input("Enter a number:"))
# temp = n
# digit=0
# sum=0
# fact=1
# while(n>0):
#     fact=1
#     digit=n%10
#     print(digit)
#     for i in range(1,digit+1):
#         fact=fact*i
#     n=n//10
#     sum=sum+fact

# if sum==temp:
#     print(temp,"is a strong number")
# else:
#     print(temp,"is not a strong number")

# def strong_num(n):
#     temp=n
#     digit=0
#     sum=0
#     while(n>0):
#         digit=n%10
#         fact=1
#         for i in range(1,digit+1):
#             fact=fact*i
#         n=n//10
#         sum=sum+fact
#     if sum==temp:
#         print(temp,"is a strong number")
#     else:
#         print(temp,"is not a strong number")

# strong_num(int(input("Enter a number:")))

#PALINDROME NUMBER

# n=int(input("Enter a number:"))
# temp=n
# rev=0
# while(n>0):
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# print(rev)
# if rev==temp:
#     print(temp,"is a palindrome number")
# else:
#     print(temp,"is not a palindrome number")

# def palindrome(n):
#     temp=n
#     rev=0
#     while(n>0):
#         r=n%10
#         rev=rev*10+r
#         n=n//10
#     print(rev)
#     if temp==rev:
#         print(temp,"is a palindrome number")
#     else:
#         print(temp,"is not a palindrome number")

# palindrome(int(input("Enter a number:")))






































    
