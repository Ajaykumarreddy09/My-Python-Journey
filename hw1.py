#1. ASSIGNMENT QN-1

# 13. What are decorators in Python? 
# Decorators in Python are a design pattern that allows you to add new functionality to an existing object
#  without modifying its structure. They are commonly used to extend the behavior of functions or methods.

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.


#write a python program to find out the price based on items purchased with discount by using elif ladder.
#  if its <10 items then 5% discount and if items <=30 then 10% discount and if its <=50 items then 20% discount 

# no_of_items=int(input("Enter the number of items:"))
# total_price=int(input("Enter the total price:"))
# if no_of_items<=10 and no_of_items>0:
#     dis_price=total_price*0.05
#     final_price=total_price-dis_price
#     print("final discounted price is: {}".format(final_price))
# elif no_of_items>10 and no_of_items<=30:
#     dis_price=total_price*0.10
#     final_price=total_price-dis_price
#     print("final discounted price is: {}".format(final_price))
# elif no_of_items>30 and no_of_items<=50:                          
#     dis_price=total_price*0.20
#     final_price=total_price-dis_price
#     print("final discounted price is: {}".format(final_price))
# else:
#     print("enter valid no_of_items")



# import math

# a = int(input("enter a value: "))
# b = int(input("enter b value: "))
# c = int(input("enter c value: "))

# discriminant = b**2 - 4*a*c
# root1 = (-b + math.sqrt(discriminant)) / (2*a)
# root2 = (-b - math.sqrt(discriminant)) / (2*a)
# print("Root 1:", root1)
# print("Root 2:", root2)

# PATTERN 
# 1 
# 1 0
# 1 0 1
# 1 0 1 0
# 1 0 1 0 1


# for i in range(5):
#     for j in range(i+1):
#         if j%2==0:
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()


#     *
#    **
#   ***
#  ****

# n=int(input("Enter no.of rows: "))
# for i in range(n):
#     print(" "*(n-i),end="")
#     print("*"*(i+1))

#pattern 

# *
# **
# ***
# ****
# ***
# **
# *

# n=int(input("Enter no.of rows: "))
# for i in range(n):
#     print("*"*(i+1),end="")
#     print()
# for j in range(n):
#     print("*"*(n-j-1),end="")
#     print()

#7.squares of nums from 1 to n and adding 

# n=int(input("Enter a range of nums:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i*i
# print(sum)


# n=int(input("Enter range of numbers:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i**2
# print(sum)

#8.1+(1+2)+(1+2+3)+(1+2+3+4)+(1+2+3+4+5)...

# n=int(input("Enter the range of nums: "))
# sum=0
# term_sum=0
# for i in range(1,n+1):
#     term_sum=term_sum+i
#     sum=sum+term_sum
# print(sum)

# n=int(input("Enter a number: "))
# t_sum=0
# for i in range(1,n+1):
#     term_sum=0
#     for j in range(1,i+1):
#         term_sum=term_sum+j
#     t_sum=t_sum+term_sum
# print(t_sum)


#9 .1 pattern

#     *
#    * *
#   * * *
#  * * * *

# n = int(input("Enter the number of rows: "))
# for i in range(0,n):
#     for j in range(0,n-i+1):
#         print(" ",end="")
#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()
              

#9.2 pattern
# ****
# ***
# **
# *

# n=int(input("Enter a value:"))
# for i in range(n):
#     print("*"*(n-i),end="")
#     print()


#10 sum of the factorial 1!+2!+3!+......


# n=int(input("enter a number: "))
# sum=0
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
#     sum=sum+fact
# print(sum)

#11. Happy Number: recursively finding the sum of squares of individual digits until the sum becomes 
# single digit and if the single digit sum==1 then we call it as happy number.

# n=int(input("enter a number: "))
# x=n
# while(n>=10):
#     sum=0
#     while(n>0):
#         r=n%10
#         sum=sum+(r**2)
#         n=n//10
#     print(sum)
#     n=sum
# if sum==1:
#     print(x,"is a happy number")
# else:
#     print(x,"is not a happy number")

#12:

#     *
#    **
#   ***
#  ****
#   ***
#    **
#     *

# n=int(input("Enter no.of rows: "))
# x=n
# for i in range(n):
#     print(" "*(n-i),end="")
#     print("*"*(i+1),end="")
#     print()
# for j in range(1,x):
#     print(" "*j,end=" ")
#     print("*"*(n-j),end="")
#     print()

#13. fibonacii series     a,b,c  0,1,1,2,3,5

# n=int(input("Enter a number: "))
# a=0
# b=1
# if n<=0:
#     print("enter a valid number")
# elif n==1:
#     print(a)
# elif n==2:
#     print(a)
#     print(b)
# elif n>2:
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c=a+b
#         print(c)
#         a=b
#         b=c

#program to swap two variables using the third variable

# x=int(input("Enter 1st number: "))
# y=int(input("Enter the 2nd number: "))
# temp=x
# x=y
# y=temp
# print(x)
# print(y)

#without using third variable 

# x=int(input("Enter 1st number: "))
# y=int(input("enter 2nd number: "))
# x,y=y,x
# print(x,'\n',y)

# x=int(input("Enter 1st number: "))
# y=int(input("enter 2nd number: "))
# x=x+y
# y=x-y
# x=x-y
# print(x,'\n',y)

#       1
#     1 2 3
#   1 2 3 4 5 
# 1 2 3 4 5 6 7

# n=int(input("Enter no.of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end='')
#     for j in range(1,2*i):
#         print(j,end='')
#     print()

# n=int(input("Enter a no.of rows: "))
# for i in range(1,n+1):
#     for j in range(1,2*n):
#         if (i==n and j%2!=0) or i+j==n+1 or j-i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# pattern

# * * * *
#   *   *
#     * *
#       *

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==n or i==j or i==1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#pattern

# n=int(input("enter no.of rows: "))
# for i in range(1,n+5,2):
#     print(str(i)*(i),end=" ")
#     print()

# n=int(input("Enter no.of rows: "))
# for i in range(1,n+5,2):
#     print(" ".join(str(i)*i))

# 1
# 121
# 12321
# 1234321

# n=int(input("Enter no.of rows: "))
# for i in range(0,n):
#     for j  in range(1,i+2):
#         print(j,end=" ")
#     for k in range(j-1,0,-1):
#         print(k,end=" ")
#     print()

#python program for horizontal table pyramid
#0
#0 1 
#0 2 4 
#0 3 6 9
#0 4 8 12 16

# n=int(input("Enter no.of rows: "))
# for i in range(n):
#     for j in range(i+1):
#         print(i*j,end=" ")
#     print()


# Function to add two matrices
# def add_matrices(matrix1, matrix2):
#     result = []  # Initialize the result matrix
    
#     # Iterate through rows
#     for i in range(len(matrix1)):
#         row = []  # Initialize a row for the result
#         # Iterate through columns
#         for j in range(len(matrix1[0])):
#             # Add corresponding elements from both matrices
#             row.append(matrix1[i][j] + matrix2[i][j])
#         # Add the row to the result matrix
#         result.append(row)
    
#     return result

# # Example matrices
# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]

# # Add the matrices
# result_matrix = add_matrices(matrix1, matrix2)

# # Print the result
# print("Resultant Matrix:")
# for row in result_matrix:
#     print(row)

# import numpy as np

# # Example matrices
# matrix1 = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# matrix2 = np.array([
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ])

# # Add the matrices using numpy's addition
# result_matrix = np.add(matrix1, matrix2)

# # Print the result
# print("Resultant Matrix:")
# print(result_matrix)


#leap year or not 

# y=int(input("Enter the year: "))
# if (y%400==0):
#     print(y,"is a leap year")
# elif (y%4==0 and y%100!=0):
#     print(y,"is leap year")
# else:
#     print(y,"is not a leap year")


# array=[1,34,52,5,6,2,3,63]
# print(array)
# array.sort()
# print(array)


# array=[1,34,52,5,6,2,3,63]
# print(array)
# array.sort(reverse=True)
# print(array)



# array=['ajy','vijay','ajay','mahesh']
# print(array)
# array.sort()
# print(array)


# array=['ajy','vijay','ajay','mahesh']
# print(array)
# array.sort(reverse=True)
# print(array)

# arr=[23,34,45,56,99,35,46,223,78,67,78,89]
# res1=[]
# res2=[]
# for i in range(0,len(arr),2):
#     res1.append(arr[i])
# for i in range(1,len(arr),2):
#     res2.append(arr[i])
# print(res1)
# print(res2)

# arr = [23, 34, 45, 56, 67, 78, 89]
# res1 = []  # To store elements whose first digit is even
# res2 = []  # To store elements whose first digit is odd

# # Iterate through each element in the array
# for num in arr:
#     first_digit = int(str(num)[0])  # Get the first digit of the number
#     if first_digit % 2 == 0:
#         res1.append(num)  # Append to res1 if the first digit is even
#     else:
#         res2.append(num)  # Append to res2 if the first digit is odd

# # Print the results
# print("Numbers with even first digit:", res1)
# print("Numbers with odd first digit:", res2)

# *  * *  *         
#  *  *  *   
#   *   *
#     *
#   *   *
#  *  *  *
# *  * *  *  

#program to rotate first 3 elements in array to the right side and vice versa

# def rotate(arr,n):
#     if len(arr)<n or n==0:
#         print(arr)
#     else:
#         rotation= arr[n:]+arr[:n]
#         print(rotation)

# arr=[12,23,34,45,56,67,78]
# n=3
# r=rotate(arr,n)    

#write a python program to remove duplicate elements in an array

# def remove_duplicate(arr):
#     unique_arr=[]
#     for i in arr:
#         if i not in unique_arr:
#             unique_arr.append(i)
    
#     print(unique_arr)

# arr=[12,12,34,34,56,55,56]
# r=remove_duplicate(arr)
# i/p
# [1 2 3]
# [4 5 6]
# [7 8 9]

# o/p:
# [1 2 3]
# [4   6]
# [7 8 9]

# def remove_inner_boundary(matrix):
#     # Set the inner boundary value to a space or None
#     matrix[1][1] = ' '  # Only applicable for a 3x3 matrix
#     return matrix

# Example usage:
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# result = remove_inner_boundary(matrix)

# print("Original matrix:")
# for row in matrix:
#     print(row)

# print("\nMatrix with inner boundary values removed:")
# for row in result:
#     print(row)


#write a program to find common elements blw 2 arrays
# i/p: arr1=['apple','grape','mango']
    #  arr2=['grape','kiwi','mango','guava']
# o/p:  arr=['grape','mango']

# def common(arr1,arr2):
#     arr=set(arr1) &set(arr2)
#     print(list(arr))

# arr1=['apple','grape','mango']
# arr2=['grape','kiwi','mango','guava','apple']
# common(arr1,arr2)

# def common(arr1,arr2):
#     arr=[]
#     for i in arr1:
#         if i in arr2:
#             arr.append(i)
#     print(arr)
# arr1=['apple','grape','mango']
# arr2=['grape','kiwi','mango','guava','apple']
# common(arr1,arr2)

# arr1=[12,2,34,56,778,89]
# arr2=[1,3,9,5,]
# arr=arr1+arr2
# print(arr)


# import numpy as np
# arr=np.array([1,2,3,4,5])
# print(type(arr))
# print(arr[1])
# print(len(arr))
# del arr

# import numpy as np
# arr1=np.array([1,2,3,4])
# arr2=np.array([12,34,45,56,67,78])
# arr=np.concatenate(arr1,arr2)
# print(arr)

# import numpy as np 
# arr1=np.array([1,2,3,4])
# arr2=np.array([5,6,7,8])
# arr=[]
# for i in arr1:
#     arr.append(i)
# for i in arr2:
#     arr.append(i)

# print(arr)

# import numpy as np

# def concatenate_arrays(arr1, arr2):
#   """Concatenates two NumPy arrays without using built-in functions.

#   Args:
#     arr1: The first NumPy array.
#     arr2: The second NumPy array.

#   Returns:
#     A new NumPy array that is the concatenation of arr1 and arr2.
#   """

#   # Calculate the total length of the concatenated array
#   total_length = len(arr1) + len(arr2)

#   # Create a new NumPy array with the appropriate size
#   result = np.empty(total_length, dtype=arr1.dtype)

#   # Copy the elements from arr1 to the beginning of the result array
#   for i in range(len(arr1)):
#     result[i] = arr1[i]

#   # Copy the elements from arr2 to the end of the result array
#   for i in range(len(arr2)):
#     result[i + len(arr1)] = arr2[i]

#   return result

# # Example usage
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6, 7])

# result = concatenate_arrays(arr1, arr2)
# print(result)

# def even_odd(arr):
#     even=[]
#     odd=[]
#     for i in arr:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     print("even: ",even)
#     print("odd: ",odd)
# arr=[1,2,3,4,5,6,7,8,9,23,45,56,78]
# even_odd(arr)



# def copy(arr):
#     arr1=[]
#     print(arr)
#     for i in arr:
#         arr1.append(i)
#     print(arr1)
# arr=[1,2,3,4,5,6]
# copy(arr)



# def min_max(arr):
#     min=arr[0]
#     max=arr[0]
#     for i in range(len(arr)):
#         if arr[i]<min:
#             min=arr[i]
#         if arr[i]>max:
#             max=arr[i]
#     print("maximum element in array is:", max)
#     print("minimum element in array is: ",min)
# arr=[1,2,3,4,-5,-6,234]
# min_max(arr)



# def sorted_arr(arr):
#     arr1=sorted(arr)
#     print(arr1)
#     print(arr1[1])
#     print(arr1[-2])
# arr=[1,6,3,4,9,11,5]
# sorted_arr(arr)


# arr=[5,1,2,99,111,45,8,3]
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]>arr[j]:
#             temp=arr[i]
#             arr[i]=arr[j]
#             arr[j]=temp
# print('The sorted array is :', arr )
# print("the second largest ele is:", arr[-2])
# print("the second smallest element is: ",arr[1])

#spy number or not 

# num=int(input("Enter a number:"))
# temp=num
# temp1=num
# sum=0
# prod=1
# while(num!=0):
#     d=num%10
#     sum=sum+d
#     prod=prod*d
#     num=num//10
# print(sum)
# print(prod)
# if sum==prod:
#     print("It is a spy number")
# else:
#     print("its not a spy number")

#1.Write a python program to print duplicate charecters in a string
#input: str="madam"
#output: str=m,a

# def duplicate(str):
#     duplicate_ele=[]
#     for i in range(len(str)):
#         for j in range(i+1,len(str)):
#             if str[i]==str[j]:
#                 duplicate_ele.append(str[i])
#     print(duplicate_ele)
# str="madam"
# duplicate(str)

#2.Write a program to check whether 2 strings are anagram or not?

# def anagram(str1,str2):
#     if len(str1)!=len(str2):
#         print("given string is not an anagram")

#     a=sorted(str1)
#     b=sorted(str2)
#     if a==b:
#         print("given strings are an anagram")
#     else:
#         print("not anagram")
# # anagram("god","dog")
# anagram("madam","damna")

#3.Write a program to check that given string is palindrome or not?

# def palindrome(str):
#     x=str
#     rev=""
#     for i in str:
#         rev=i+rev
#     print(rev)
#     if rev==x:
#         print("its a palindrome")
#     else:
#         print("its not a palindrome")
# palindrome("mom")
# palindrome("madam")
# palindrome("sir")



#4.Write a python program to remove duplicate charecters in a string?
#input:"madam"
#output: mad

# def duplicate(str):
#     chars=""
#     for i in str:
#         if i not in chars:
#             chars=chars+i
#     print(chars)
# duplicate("madam")
# duplicate("ajay")    

#5.Write a python program to remove spaces in a string
#input: i love my family
#output: ilovemyfamily

# def rem_sp(str):
#     str1=str.replace(" ","")
#     print(str1)
# rem_sp("i love my family")

# def rem_sp(str):
#     res=""
#     for i in str:
#         if i!=" ":
#             res=res+i
#     print(res)
# rem_sp("i love my family")

#6. Write a program to print vowels and consonants in a given string ?

# str=input("Enter a string: ")
# vowels=[]
# cons=[]
# for i in str:
#     if i in ['a','e','i','o','u']:
#         vowels.append(i)
#     elif i==" ":
#         pass
#     else:
#         cons.append(i)
# print(vowels)
# print(cons)

#7.Write a python program to reverse a string without using any predefined methods?
#i/p: str="country"
#o/p: str="yrtnuoc"

# def reverse_str(str):
#     rev=""
#     for i in str:
#         rev=i+rev
#     print(rev)
# str="hello"
# reverse_str(str)

#8. Write a program to find all the permutatios of a string

# def find_permutations(s, answer=""):
#     if len(s) == 0:
#         print(answer)
#         return

#     for i in range(len(s)):
#         ch = s[i]  # Choose one character
#         left_substr = s[:i]  # All characters to the left
#         right_substr = s[i+1:]  # All characters to the right
#         rest = left_substr + right_substr  # Remaining characters
#         find_permutations(rest, answer + ch)

# # Example usage
# input_string = "ABC"
# print("All permutations:")
# find_permutations(input_string)

# find the factorial of a number?
# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# n=int(input("Enter a number:"))
# r=fact(n)
# print(r)


#GCD of 2 nums
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# # Example usage
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# result = gcd(num1, num2)
# print(f"The GCD of {num1} and {num2} is {result}.")


#9. write a python program to find all subsets of the string ?

# def subset(str):
#     subset1=[""]
#     for i in range(0,len(str)):
#         for j in range(i,len(str)):
#             subset1.append(str[i:(j+1)])
#     for i in subset1:
#         print(i)
# subset("fun") 

# 10.Write a python program to count no.of words in a given string?
# str="today we are discussing string concepts"
#o/p=n=6

# def words(str):
#     words=1
#     for i in str:
#         if i==" ":
#             words=words+1
#     print("no.of words:",words)
# words("we are learning python")

#1. write a python program to print matched chars in the given two strings 
# def matched(str1,str2):
#     matched_chars=[]
#     for i in str1:
#         if i in str2:
#             if i not in matched_chars:
#                 matched_chars.append(i)
#     print(matched_chars)
# str1="india"
# str2="indonesia"
# matched(str1,str2)

#2.write a python program to find out even and odd length words in strings

# def even_odd(str):
#     even_words=[]
#     odd_words=[]
#     sp=str.split()
#     for words in sp:
#         if len(words)%2==0:
#             even_words.append(words)
#         else:
#             odd_words.append(words)
#     print("even length words :",even_words)
#     print("odd length wor:",odd_words)
# str=input("Enter a string: ")
# even_odd(str)

#1. write a program to check string contains special chars or not?

# def contains_special_characters(input_string):
#     for char in input_string:
#         if not char.isalnum():  
#             print("Contains special characters")
#             return

#     print("Does not contain special characters")  
# input_string = input("Enter a string: ")
# contains_special_characters(input_string)

# def contains_special_characters(input_string):
#     for char in input_string:
#         # Check if char is not in the ranges of '0'-'9', 'A'-'Z', or 'a'-'z'
#         if not ('A' <= char <= 'Z' or 'a' <= char <= 'z' or '0' <= char <= '9'):
#             return True  # Special character found
#     return False  # No special characters found

# # Test the function
# input_string = input("Enter a string: ")
# if contains_special_characters(input_string):
#     print("The string contains special characters.")
# else:
#     print("The string does not contain any special characters.")

#qn. write a program to findout the words whichh are greater than the given length k?

# def words(str,k):
#     sp=str.split()
#     for i in sp:
#         if len(i)>k:
#             print(i)
# str=input("enter the string: ")
# k=int(input("Enter the length: "))
# words(str,k)

#move all negative elements to one side of the array

# def move(a):
#     pl=[]
#     nl=[]
#     for i in a:
#         if i<0:
#             nl.append(i)
#         else:
#             pl.append(i)
#     print(pl+nl)
# a=[1,-2,-3,4,5,-4]
# move(a)

#find the row with maximum no.of 1's
#i/p: l=[[1,0,0,1],[1,1,1,1],[0,0,0,0],[1,0,1,0]]
#o/p: l=1

# def max_ones(a):
#     max_1s=0
#     row_index=0
#     for i in range(len(a)):
#         ones_count=a[i].count(1)
#         if ones_count>max_1s:
#             max_1s=ones_count
#             row_index=i
#     print(row_index)
# a=[[1,0,1,0],[0,0,0,1],[1,1,1,0],[1,1,1,1]]
# max_ones(a)


#python program for wave array
# i/p: [1,2,3,4,5]
# o/p: [2,1,4,3,5] 

# def wave(a):
#     for i in range(0,len(a)-1,2):
#         a[i],a[i+1]=a[i+1],a[i]
#     print(a)
# a=[1,2,3,4,5]
# wave(a)

# python prog for factorial of large numbers
# i/p: 5
# o/p:[1,2,0]

# def fac(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(f"the factorial of {n} is:{fact}")
#     ds=[]
#     while(fact>0):
#         l=fact%10
#         ds.append(l)
#         fact=fact//10
#     ds.reverse()
#     print(f"the individual digits are:{ds}")
#     for digit in ds:
#         df=1
#         for i in range(1,digit+1):
#             df=df*i
#         print(f"the factorial of {i} digit is:{df}")
# n=5
# fac(5)

#find if an array is subset of another array
# i/p: a=[1,2,3,4,5,6,7]
# i/p: b=[1,2,3,7]
# o/p:yes 

# def subs(a,b):
#         for i in b:
#             if i not in a:
#                 print("NO")
#                 return
#         print("YES")

# a=[1,2,3,4,5,6,7]
# b=[1,2,3,4,7]
# subs(a,b)


# import random
# import time

# def generate_otp(length=6):
#     """Generates a numeric OTP of given length."""
#     otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
#     return otp

# def otp_verification_system():
#     """Implements the OTP verification system."""
#     # Generate an OTP
#     otp = generate_otp()
#     print(f"Your OTP is: {otp}")
    
#     # Start timer
#     timeout = 30  # OTP valid for 30 seconds
#     print("The OTP is valid for 30 seconds.")

#     # Capture time when OTP is generated
#     start_time = time.time()

#     while True:
#         # Check if the time limit has expired
#         elapsed_time = time.time() - start_time
#         if elapsed_time > timeout:
#             print("OTP has expired.")
#             return
        
#         # Ask user to input the OTP
#         user_input = input("Enter the OTP: ")
#         if user_input == otp:
#             print("OTP verified successfully!")
#             return
#         else:
#             print("Invalid OTP. Try again.")

# # Run the OTP verification system
# otp_verification_system()


# You are given a string str of length n. You have to find and print the most frequent vowel in the string str
# Note: You may assume that str will always have a unique most frequent vowel
# Input Format:
# The input consists of two lines:
# The first line contains an integer, i.e. n.
# The second line contains a string str of length n. The input will be read from the STDIN by the candidate
# Output Format:
# Print a single character which represents the most frequent vowel in the given string.
# The output will be matched to the candidate's output printed on the STDOUT

# def vcount(st):
#     acount=0
#     ecount=0
#     icount=0
#     ocount=0
#     ucount=0
#     for i in st:
#         if i=='a':
#             acount=acount+1
#         elif i=='e':
#             ecount=ecount+1
#         elif i=='i':
#             icount=icount+1
#         elif i=='o':
#             ocount=ocount+1
#         elif i=='u':
#             ucount=ucount+1
    
#     maxcount=max(acount,ecount,icount,ocount,ucount)
#     if maxcount==acount:
#         print('a')
#     elif maxcount==ecount:
#         print('e')
#     elif maxcount==icount:
#         print('i')
#     elif maxcount==ocount:
#         print('o')
#     elif maxcount==ucount:
#         print('u')

# st=input()
# vcount(st)

# def count1(n):
#     br=bin(n)[2:]
#     countones=br.count('1')
#     return countones
# n=5
# print(f"The sum of 1s in binary representation of {n} is:{count1(n)}")

# 2️ Find the Second Smallest Element in an Array: A key problem for mastering array manipulation.
# def secondl(a):
#     for i in range(len(a)-1):
#         for j in range(i+1,len(a)):
#             if a[i]>a[j]:
#                 temp=a[i]
#                 a[i]=a[j]
#                 a[j]=temp
#     smallest=a[0]
#     for i in a:
#         if i>smallest:
#             print(f"the second smallest of {a} is: {i}")
#             return
# a=[67,2,4,6,2,1,4,7,1]
# secondl(a)

# def secondl(a):
#     sr=sorted(set(a))
#     if len(sr)<2:
#         print("there is no second largest as array is small")
#         return
#     else:
#         print(f"the second largest number in the array{a} is:{sr[-2]}")
#         return
# a=list(map(int,input().split()))
# secondl(a)


# 3️ Shorten Words with Middle Character Count: A fun string problem that enhances logical thinking.
# def ce(sentence):
#     words=sentence.split()
#     sws=[]
#     for word in words:
#         if len(word)>2:
#             mc=len(word)-2
#             sw=f"{word[0]}{mc}{word[-1]}"
#             sws.append(sw)
#         else:
#             sws.append(word)
#     print(" ".join(sws))

# sentence=input()
# ce(sentence)


# 4️ Prime Numbers Between 1 and N: Understand how to find prime numbers efficiently.
# def prime(n):
#     if n<2:
#         print("no prime numbers enter valid number")
#     else:
#         for num in range(2,n+1):
#             for i in range(2,num):
#                 if num%i==0:
#                     break
#             else:
#                 print(num)
# n=int(input("Enter a range of nums:"))
# prime(n)

# 5️ Print Floyd's Triangle: A classic problem to test your ability to handle nested loops and patterns.

# num=1
# n=int(input("Enter no.of rows:"))
# for i in range(1,n+1):
#     for  j in range(1,i+1):
#         print(num,end=" ")
#         num=num+1
#     print()

# The function accepts two positive integers ‘r’ and ‘unit’ and a positive integer array ‘arr’ of size ‘n’ as 
# its argument ‘r’ represents the number of rats present in an area, ‘unit’ is the amount of food each rat consumes 
# and each ith element of array ‘arr’ represents the amount of food present in ‘i+1’ house number, where 0 <= i

# Note:

# Return -1 if the array is null
# Return 0 if the total amount of food from all houses is not sufficient for all the rats.
# Computed values lie within the integer range.
# Example:

# Input:

# r: 7
# unit: 2
# n: 8
# arr: 2 8 3 5 7 4 1 2

#o/p: 4

# def mh(r,units,arr):

#     if len(arr)==0:
#         return -1

#     required_food=r*units
#     totalfood=sum(arr)
#     if totalfood<required_food:
#         return 0
    
#     accumulated_food=0
#     total_houses=0
#     for i in arr:
#         accumulated_food=accumulated_food+i
#         total_houses=total_houses+1
#         if accumulated_food>=required_food:
#             return total_houses
# r=int(input())
# units=int(input())
# arr=list(map(int,input().split()))
# result=mh(r,units,arr)
# print(result)



# The Binary number system only uses two digits, 0 and 1 and number system can be called binary string. 
# You are required to implement the following function:

# int OperationsBinaryString(char* str);

# The function accepts a string str as its argument. 
# The string str consists of binary digits eparated with an alphabet as follows:

# – A denotes AND operation
# – B denotes OR operation
# – C denotes XOR Operation
# You are required to calculate the result of the string str,
#  scanning the string to right taking one opearation at a time, and return the same.

# Note:

# No order of priorities of operations is required
# Length of str is odd
# If str is NULL or None (in case of Python), return -1
# Input:
# str: 1C0C1C1A0B1

# Output:
# 1

# Explanation:
# The alphabets in str when expanded becomes “1 XOR 0 XOR 1 XOR 1 AND 0 OR 1”, result of the expression becomes 1, hence 1 is returned.

# Sample Input:
# 0C1A1B1C1C1B0A0

# Output:
# 0

# def binarynum(binary_str):
#     if not binary_str:  # Check if the string is None or empty
#         return -1
    
#     a = int(binary_str[0])  # Convert the first character to an integer
#     i = 1
#     while i < len(binary_str):
#         if binary_str[i] == "A":  # AND operation
#             a &= int(binary_str[i+1])
#         elif binary_str[i] == "B":  # OR operation
#             a |= int(binary_str[i+1])
#         elif binary_str[i] == "C":  # XOR operation
#             a ^= int(binary_str[i+1])
#         i += 2
#     return a

# # Get input from user
# binary_str = "1C0C1C1A0B1"  # Accept the binary string input
# r = binarynum(binary_str)  # Call the function
# print(r)  # Output the result

# int CheckPassword(char str[], int n);
# The function accepts string str of size n as an argument. 
# Implement the function which returns 1 if given string str is valid password else 0.
# str is a valid password if it satisfies the below conditions.
# – At least 4 characters
# – At least one numeric digit
# – At Least one Capital Letter
# – Must not have space or slash (/)
# – Starting character must not be a number
# Assumption:
# Input string will not be empty.
# Example:
# Input 1:
# aA1_67
# Input 2:
# a987 abC012
# Output 1:
# 1
# Output 2:
# 0

# def valid(in_string):
#     if len(in_string)<4:
#         return 0
#     if in_string[0].isdigit():
#         return 0
#     dc=0
#     cl=0
#     for i in range(len(in_string)):
#         if in_string[i].isdigit():
#             dc=dc+1
#         if in_string[i]>= "A" and in_string[i]<="Z":
#             cl=cl+1
#         elif in_string[i]==" " or in_string[i]=="/":
#             return 0
#     if dc>0 and cl>0:
#         return 1
# in_string=input()
# r=valid(in_string) 
# print(r)

# def valid(in_string):
#     if len(in_string) < 4:
#         return 0
#     if in_string[0].isdigit():
#         return 0
    
#     digit_count = 0
#     capital_count = 0
    
#     for char in in_string:
#         if char.isdigit():
#             digit_count += 1
#         elif char.isupper():
#             capital_count += 1
#         elif char == " " or char == "/":
#             return 0
    
#     return 1 if digit_count > 0 and capital_count > 0 else 0

# in_string = input("Enter the password: ")
# result = valid(in_string)
# print(result)

# def des(n):
#     for i in range(-5,6,1):
#         print(i,end=" ")
# n=5
# des(n)

# def wc(in_st,word):
#     words=in_st.split(" ")
#     count=0
#     for i in words:
#         if i==word:
#             count=count+1
#     print(f"the count of word {word} is:{count}")

# in_st="i like the like who like the lake"
# # word="like"
# wc(in_st,word)


# n=list(map(int,input("Enter the list of nums").split(",")))
# print(n)

# n=[int(n) for n in input("enter vals:").split(",") ]
# print(n)




# def missing(a):
#     for i in range(1,len(a)+1):
#         if i not in a:
#             print(i)
#             return
#     print("nothing is missing")
# a=list(map(int,input().split(",")))
# missing(a)

# given an integer array nums and an integer k. return k most frequent elements. 
# you must return the answer in any order. 
# i/p:  nums=[1,1,1,2,2,3], k=2  o/p: [1,2]

# def frequency(arr, k):
#     count = {}
#     for i in arr:
#         if i in count:
#             count[i] += 1
#         else:
#             count[i] = 1
    
#     print("Frequency of elements:", count)
    
#     # Sort keys by frequency in descending order
#     sort_count = sorted(count, key=lambda x: count[x], reverse=True)
    
#     # Handle edge case where k exceeds the number of unique elements
#     k = min(k, len(sort_count))
    
#     print(f"Top {k} elements by frequency:", sort_count[:k])

# # Input handling
# arr = list(map(int, input("Enter the array elements (comma-separated): ").split(",")))
# k = int(input("Enter the number of top frequency elements needed: "))
# frequency(arr, k)

#insertion sort

# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key=arr[i]
#         j=i-1
#         while j>=0 and arr[j]>key:
#             arr[j+1]=arr[j]
#             j=j-1
#         arr[j+1]=key

# arr=list(map(int,input("Enter the elements of the array").split(",")))
# insertion_sort(arr)
# print(arr)

#merge sort

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr  
    
#     mid = len(arr) // 2
#     l_half = arr[:mid] 
#     r_half = arr[mid:]  

#     l_half = merge_sort(l_half)
#     r_half = merge_sort(r_half)
    
#     return merge(l_half, r_half)

# def merge(l_half, r_half):
#     new = []  
#     i, j = 0, 0    
#     while i < len(l_half) and j < len(r_half):
#         if l_half[i] < r_half[j]:
#             new.append(l_half[i])
#             i += 1
#         else:
#             new.append(r_half[j])
#             j += 1
    
#     new.extend(l_half[i:])
#     new.extend(r_half[j:])  
#     return new
# arr = list(map(int, input("Enter the elements").split(",")))
# sorted_arr = merge_sort(arr)
# print("Sorted array:", sorted_arr)

#Quick sort works on the divide and conquer rule and it divides the given array into partitions
# and sorts the array like inthe first partition it sorts the array in such a way that it considers a pivot element and
# then it sorts in such a way that the left side of pivot element is smaller than pivot and right side elements are greater than the pivot
# logic is that if i<j swap a[i],a[j] else if i>j swap a[j],pivot

#Alphabets pattern

# n=int(input("Enter no.of rows:"))
# num=65
# for i in range(n):
#     for j in range(i+1):
#         char=chr(num)
#         print(char,end=" ")
#         num=num+1
#     print( )

# n=int(input("Enter a number:"))
# num=65
# for i in range(n):
#     for j in range(i+1):
#         char=chr(num)
#         print(char,end=" ")
#     num=num+1
#     print()

#modifying a string in python

# string="Hello zorld"
# s=list(string)
# s[6]='w'
# print(s)
# sr=str(s)
# print(sr)
# print("".join(s))

# lambda function
# x=lambda a: a+10
# print(x(5))

#list comprehension example
# l=[i for i in range(1,11)]
# print(l)
#dictionary comprehension
# d={i:i**2 for i in range(1,11)}
# print(d)
#tuple comprehension
# t=(i for i in range(1,11))
# print(t)

#handling exceptions in dict

# dic={"KA":"BA","MH":"Mb","TN":"CH"}
# cap="Ap"
# try:
#     Value=dic[cap]
#     print(Value)
# except KeyError:
#     print(f"the key {cap} is not present in the dict ")

# s=input("Enter a string")
# r=input("Enter the word to replace space")
# print(s.replace(" ",r))

#check if it is the perfect square root
# import math
# def valid_square(num):
#     sqr=math.sqrt(num)
#     int_sqr=int(sqr)
#     org= int_sqr**2
#     if org==num:
#         return True
#     else:
#         return False
# v=valid_square(10)
# print(v)
# x=valid_square(36)
# print(x)

# def valid_square(num):
#     sqr=int(num**0.5)
#     org= sqr**2
#     if org==num:
#         return True
#     else:
#         return False
# v=valid_square(10)
# print(v)
# x=valid_square(36)
# print(x)

# def factorial_trailing_zeros(n):

#     fact = 1
#     for i in range(1,n+1):
#         fact=fact*i

#     result = 0

#     for i in str(fact)[::-1]:
#         if i == "0":
#             result += 1
#         else:
#             break

#     return result


# r1=factorial_trailing_zeros(10)
# print(r1)
# # 2
# r2=factorial_trailing_zeros(18)
# print(r2)
# # 3
        
#removing duplicates and returning no.of unique elements

# def remove_dup(arr):
#     arr1 = set()
#     for i in arr:
#         arr1.add(i)
#     arr1 = list(arr1)  # Convert back to list if you want a list
#     print(arr1)
#     print(len(arr1))

# arr = [1, 1, 2, 2]
# remove_dup(arr)

# def sum_nums(nums,t):
#     for i in range(0,len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==t:
#                 return i,j
# nums=list(map(int,input().split(" ")))
# t=int(input())
# r=sum_nums(nums,t)
# print(r)

# def primenums(st, en):
#     primes = []
#     for num in range(st, en):
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             primes.append(num)  # Append the prime number, not i
#     return primes

# st = int(input("Enter the start range: "))
# en = int(input("Enter the last num: "))
# r = primenums(st, en)
# print(r)

#nth fibonacci number

# def fib(n):
#     a=0
#     b=1
#     if n<0:
#         return "Enter valid input"
#     elif n==0:
#         return a
#     elif n==1:
#         return b
#     else:
#         for i in range(2,n+1):
#             c=a+b
#             a=b
#             b=c
#         return c
# print(fib(int(input())))

# sum of fibbonacci nums in the given range
# def fib(m,n):
#     a=0
#     b=1
#     total=0
#     for i in range(n+1):
#         if i>=m:
#             total=total+a
#         a,b=b,a+b
#     return total
# m=int(input("Enter the starting num:"))
# n=int(input("Enter the ending num:"))
# print(fib(m,n))

#printing even fibonacci nums
# def fib(n):
#     a=0
#     b=1
#     while a<=n:
#         if a%2==0:
#             print(a)
#         a,b=b,a+b
# n=int(input("Enter the range"))
# fib(n)

# def fib(n):
#     a=0
#     b=1
#     while a<=n:
#         if a%2!=0:
#             print(a)
#         a,b=b,a+b
# n=int(input("Enter the range"))
# fib(n)

# def fib(n):
#     a,b=0,1
#     count=0
#     while count<n:
#         if a%2==0:
#             print(a)
#         a,b=b,a+b
#         n=
# n=int(input("Enter the num"))
# fib(n)

#printing ascii values of a character

# print(ord('c'))

# def asciword(sen):
#     for i in sen:
#         print(ord(i),end=" ")
# sen="Hello, world!"
# asciword(sen)

# def ascirange(sen,l,r):
#     count=0
#     not_in_range=[]
#     for i in sen:
#         if i.isalpha() and not(l<=ord(i)<=r):
#             not_in_range.append(i)
#             count=count+1
#     print(f"The alphabets that are not in range are{not_in_range}")
#     print(f"the count of alphabets that are not in range is {count}")
# sen="Hello, World"
# l,r=102,111
# ascirange(sen,l,r)


# def avgasci(sen):
#     word=""
#     sum=0
#     for i in range(len(sen)):
#         if sen[i]==" ":
#             avg=sum/len(word)
#             print(word,"-",avg)
#             word=""
#             sum=0
#         else:
#             word=word+sen[i]
#             sum=sum+ord(sen[i])
#     if len(word) > 0:
#         avg = sum / len(word)
#         print(f"{word} - {avg}")
# sen="learning a string algorithm"
# avgasci(sen)        

# def avgasci(sen):
#     sen += " "  # Add a space to ensure the last word is processed
#     word = ""
#     sum = 0
#     for char in sen:
#         if char == " ":
#             if word:  # Process the word if it's not empty
#                 avg = sum / len(word)
#                 print(f"{word} - {avg}")
#             word = ""
#             sum = 0
#         else:
#             word += char
#             sum += ord(char)

# # Example usage
# sen = "learning a string algorithm"
# avgasci(sen)

#largest num in an array
# def largest(arr):
#     max=arr[0]
#     for i in arr:
#         if i>max:
#             max=i
#     return max
# arr=list(map(int,input("Enter the elements of array").split(",")))
# r=largest(arr)
# print(r)

#rotate the array by d elements
# This means 12 rotations are effectively the same as 2 rotations, as the other 10 rotations (two full rotations) 
# simply cycle the array back to its original state.

# def left_rotate(arr,d):
#     if d>=len(arr):
#         d=d%len(arr)
#     res=arr[d:]+arr[:d]
#     return res
# arr=[1,2,3,4,5,6,7]
# d=2
# r=left_rotate(arr,d)
# print(r)

#sum of digits in a num
# def sum(num):
#     if num<0:
#         print("Invalid input")
#     else:
#        sum=0
#        for i in str(num):
#           sum=sum+int(i)
#     print(sum)
# num=1234
# sum(num)

#factorial 

def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
num=5
fact(num)















































































































































































































































































































































































































































































































































































































































































