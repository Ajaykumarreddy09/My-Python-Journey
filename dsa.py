#Data structure?
# A data structure is a way to organize, manage, and store data in a computer so it can be used efficiently.
# it enables better performance for the tasks like searching, sorting or modifying the data.
# Ex: Arrays, Linked lists, Stacks, Queues, Trees, Graphs, Hashtables.
# or data structures help organize data in a way that makes it easy to access, modify, and
#  process efficiently for various algorithms

# Algorithm?
#  An algorithm is a step-by-step set of instructions to solve a problem or perform a task.
#common types of algorithms: 
# 1. sorting algs: bubble,quick,merge sort
#2.searching algs: linear search, Binary search
#3.Graph Algorithms: Dijkstra's alg,Deapth-First search, Breadth-first search
#4.Divide and conquer alg: quick and merge sort
#5.Backtracking algs: sudoku, maze

#Back tracking: Back tracking is a method to solve problems by trying all possible options step by step.
#if a choice doesn't work you go back and try another one.
#Ex: you pick a path and follow it, if you hit a dead end, you go back to the last decision point
# and try a different path.
 

#Time Complexity: Time complexity is the measure of the computational complexity of an algorithm.
# it describes the amount of time taken by the algorithm increases as the size of input increases/grows.

#space complexity: Space complexity is the amount of memory an algorithm needs to run.
#it includes :1. Input space: memory to store the input
#Auxiliary space: Extra memory used for calculations, variables, or temporary storage.


# #linked lists
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# #creating nodes
# node1=Node(10)
# node2=Node(20)
# node3=Node(30)
# node4=Node(40)

# # connecting nodes to form a linked list

# node1.next=node2
# node2.next=node3
# node3.next=node4
# node4.next=None

# # printing the lined lists
# head=node1
# current=head
# while current is not None:
#     print(current.data,end="->")
#     current=current.next
# print("None")


# # inserting in the begining of the lined list

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# #creating nodes
# node1=Node(10)
# node2=Node(20)
# node3=Node(30)
# node4=Node(40)
# # connecting the nodes to form a lined list
# node1.next=node2
# node2.next=node3
# node3.next=node4
# node4.next=None
# # Adding an element at the begining of the linked list
# head=node1
# new_node=Node(50)
# new_node.next=head
# head=new_node
# # printing the elemnts in lined list
# head=new_node
# currrent=head
# while currrent is not None:
#     print(currrent.data,end="->")
#     currrent=currrent.next
# print("None")



#inserting at the end in a linked list

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# #creating nodes
# node1=Node(10)
# node2=Node(20)
# node3=Node(30)
# node4=Node(40)

# #connecting the nodes
# node1.next=node2
# node2.next=node3
# node3.next=node4
# node4.next=None
# # inserting a new node at the end
# new_node=Node(50)
# head=node1
# current=head
# while current.next is not None:
#     current=current.next
# current.next=new_node

# #printing 
# current=head
# while current is not None:
#     print(current.data,end="->")
#     current=current.next
# print("None")


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# # creating Nodes
# node1=Node(10)
# node2=Node(20)
# node3=Node(30)
# node4=Node(40)
# #connecting the nodes 
# node1.next=node2
# node2.next=node3
# node3.next=node4
# #Inserting at specified position
# newnode=Node(50)
# current=node1
# while current.next is not None and current.data!=20:
#     current=current.next
# newnode.next=current.next
# current.next=newnode

# #printing the list

# head=node1
# while head is not None:
#     print(head.data,end="->")
#     head=head.next
# print("None")


#deleting at the begining of the linked list

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# #creating the nodes
# node1=Node(10)
# node2=Node(20)
# node3=Node(30)
# node4=Node(40)
# #connecting the nodes
# node1.next=node2
# node2.next=node3
# node3.next=node4
# #deleting the node at begining
# head=node1
# if head is not None:
#     head=head.next
# #printing
# current=head
# while current is not None:
#     print(current.data,end="->")
#     current=current.next
# print("None")



#deleting a node at the end of the linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# #creating nodes
# node1=Node(10)
# node2=Node(20)
# node3=Node(30)
# node4=Node(40)
# #connecting the nodes
# node1.next=node2
# node2.next=node3
# node3.next=node4
# #deleting the node in the last
# current=node1
# while current.next.next is not None:
#     current=current.next
# current.next=None
# #printing the list
# current=node1
# while current is not None:
#     print(current.data,end="->")
#     current=current.next
# print("None")



#deleting at a particular position in a linked list

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# #creating nodes
# node1=Node(10)
# node2=Node(20)
# node3=Node(30)
# node4=Node(40)
# #connecting the nodes 
# node1.next=node2
# node2.next=node3
# node3.next=node4
# #deleting at paraticular position
# current=node1
# while current.next.data !=30:
#     current=current.next
# current.next=current.next.next
# #printing
# current=node1
# while current is not None:
#     print(current.data,end="->")
#     current=current.next
# print("None")


#Double linked list

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# class Dll:
#     def __init__(self):
#         self.head=None
#     def display(self):
#         if self.head is None:
#             print("List is empty")
#         else:
#           temp=self.head
#           while(temp):
#             print(temp.data,end="->")
#             temp=temp.next
#         print("None")  

# l=Dll()
# n1=Node(10)
# l.head=n1
# n2=Node(20)
# n1.next=n2
# n2.prev=n1
# n3=Node(30)
# n2.next=n3
# n3.prev=n2
# n4=Node(40)
# n3.next=n4
# n4.prev=n3
# n4.next=None
# l.display()


# #Inserting in the beging of the double linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None
# #creating nodes
# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# n4=Node(40)
# #connectinng the nodes 
# n1.next=n2
# n2.prev=n1
# n2.next=n3
# n3.prev=n2
# n3.next=n4
# n4.prev=n3
# n4.next=None
# #inserting at the begining
# n5=Node(50)
# temp=n1
# temp.prev=n5
# n5.next=temp
# head=n5

# while head is not None:
#     print(head.data,end="->")
#     head=head.next
# print(None)

#insering at the begining, end, at any position of the list

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# class Dll:
#     def __init__(self):
#         self.head=None
#     def display(self):
#         if self.head is None:
#             print("List is Empty")
#         else:
#             temp=self.head
#             while temp:
#                 print(temp.data,end="->")
#                 temp=temp.next
#             print("None")
#     def insert_at_begin(self,data):
#         n=Node(data)
#         temp=self.head
#         temp.prev=n
#         n.next=temp
#         self.head=n
#     def insert_at_end(self,data):
#         n=Node(data)
#         temp=self.head
#         while temp.next is not None:
#             temp=temp.next
#         temp.next=n 
#         n.prev=temp
#     def insert_pos(self,pos,data):
#         if pos<=0:
#             print("Invalid position")
#             return
#         n=Node(data)
#         if pos==1:
#             self.insert_at_begin(data)
#             return
#         temp=self.head
#         for i in range(1,pos-1):
#             if temp is None:
#                 print("Position out of bounds")
#                 return
#             temp=temp.next
#         if temp.next is None:
#             self.insert_at_end(data)
#         else:
#             n.next=temp.next
#             n.prev=temp
#             temp.next.prev=n
#             temp.next=n

# L=Dll()
# n1=Node(10)
# L.head=n1
# n2=Node(20)
# n1.next=n2
# n2.prev=n1
# n3=Node(30)
# n2.next=n3
# n4=Node(40)
# n3.next=n4
# n4.prev=n3
#n4.next=None
# L.insert_at_begin(5)
# L.insert_at_begin(4)
# L.insert_at_end(60)
# L.insert_at_end(70)
# L.insert_pos(3,25)
# L.display()


#Deleting in double linked list

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# class Dll:
#     def __init__(self):
#         self.head=None

#     def display(self):
#         temp=self.head
#         if temp is None:
#             print("List is Empty")
#         else:
#             while temp is not None:
#                 print(temp.data,end="->")
#                 temp=temp.next   
#             print("None")
#     def del_beg(self):
#         if self.head is None:
#             print("List is already empty")
#             return
#         temp=self.head
#         self.head=temp.next
#         if self.head:
#             self.head.prev=None
#         temp.next=None
#     def del_end(self):
#         if self.head is None:
#             print("list is empty")
#             return
#         if self.head.next is None:
#             self.head=None
#             return
#         temp=self.head
#         while temp.next.next is not None:
#             temp=temp.next
#         temp.next=None
#     def del_pos(self,pos):
#         if self.head is None:
#             print("list is empty")
#             return
#         if pos<=0:
#             print("Invalid position")
#             return
#         if pos==1:
#             self.del_beg()
#             return
#         temp=self.head
#         for i in range(1,pos-1):
#             temp=temp.next
#         temp.next=temp.next.next

# L=Dll()
# n1=Node(10)
# L.head=n1
# n2=Node(20)
# n1.next=n2
# n2.prev=n1
# n3=Node(30)
# n3.prev=n2
# n2.next=n3
# n4=Node(40)
# n4.prev=n3
# n3.next=n4
# n4.next=None
# # L.display()
# # L.del_beg()
# #L.del_end()
# L.del_pos(2)
# L.display()


# circular linked lists

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Cll:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def display(self):
#         if self.head is None:
#             print("list is empty")
#             return
#         else:
#             temp=self.head
#             print(temp.data,end="=>")
#             while temp.next !=self.head:
#                 temp=temp.next
#                 print(temp.data,end="=>")
#             print(temp.next.data)
# L=Cll()
# n1=Node(10)
# L.head=n1
# L.tail=n1
# L.tail.next=L.head

# n2=Node(20)
# L.tail.next=n2
# L.tail=n2
# L.tail.next=L.head

# n3=Node(30)
# L.tail.next=n3
# L.tail=n3
# L.tail.next=L.head
# L.display()        

#Insertion in circular linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Cll:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def display(self):
#         if self.head is None:
#             print("List is empty")
#             return
#         else:
#             temp=self.head
#             print(temp.data,end="->")
#             while temp.next != self.head:
#                 temp=temp.next
#                 print(temp.data,end="->")
#             print(temp.next.data)
#     def insert_beg(self,data):
#         newnode=Node(data)
#         if self.head is None:
#             self.head=newnode
#             self.tail=newnode
#             self.tail.next=newnode
#         else:
#             newnode.next=self.head
#             self.tail.next=newnode
#             self.head=newnode
#     def insert_end(self,data):
#         newnode=Node(data)
#         if self.head is None:
#             self.head=newnode
#             self.tail=newnode
#             self.tail.next=newnode
#         else:
#             self.tail.next=newnode
#             self.tail=newnode
#             newnode.next=self.head
#     def insert_pos(self,data,pos):
#         newnode=Node(data)
#         if pos<=0:
#             print("enter valid position")
#             return
#         if self.head is None:
#             if pos>1:
#                 print("Position out of bounds")
#                 return
#             else:
#                 self.insert_beg(data)
#                 return
#         length=1
#         temp=self.head
#         while temp.next!=self.head:
#             length+=1
#             temp=temp.next
#         if pos==length+1:
#             self.insert_end(data)
#             return
#         if pos==1:
#             self.insert_beg(data)
#         temp=self.head
#         for i in range(1,pos-1):
#             temp=temp.next
#         newnode.next=temp.next
#         temp.next=newnode

# L=Cll()
# n1=Node(10)
# L.head=n1
# L.tail=n1
# L.tail.next=L.head

# n2=Node(20)
# L.tail.next=n2
# L.tail=n2
# L.tail.next=L.head

# n3=Node(30)
# L.tail.next=n3
# L.tail=n3
# L.tail.next=L.head
# #L.display()
# #L.insert_beg(5)
# #L.insert_end(40)
# L.insert_pos(25,3)
# L.display()

#deleting nodes in CLL

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Cll:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def display(self):
#             if self.head is None:
#                 print("List is empty")
#                 return
#             else:
#                 temp=self.head
#                 print(temp.data,end="->")
#                 while temp.next != self.head:
#                     temp=temp.next
#                     print(temp.data,end="->")
#                 print(temp.next.data)
#     def del_beg(self):
#         if self.head is None:
#             print("list is already empty")
#             return
#         if self.head==self.tail:
#             self.head=None
#             self.tail=None
#         else:
#             self.head=self.head.next
#             self.tail.next=self.head
#     def del_end(self):
#         if self.head is None:
#             print("list is empty")
#             return
#         temp=self.head
#         while temp.next!=self.tail:
#             temp=temp.next
#         temp.next=self.head
#         self.tail=temp
#     def del_pos(self,pos):
#         if self.head is None:
#             print("List is empty")
#             return
#         if pos<=0:
#             print("Enter a valid position")
#             return
#         if pos==1:
#             self.del_beg()
#             return
#         temp=self.head
#         length=1
#         while temp.next != self.head:
#             length=length+1
#             temp=temp.next
#         if pos>length:
#             print("position out of bounds")
#             return
#         if pos==length:
#             self.del_end()
#             return
#         temp=self.head
#         for i in range(1,pos-1):
#             temp=temp.next
#         to_del=temp.next
#         temp.next=temp.next.next
#         to_del.next=None

        
# L=Cll()
# n1=Node(10)
# L.head=n1
# L.tail=n1
# L.tail.next=L.head

# n2=Node(20)
# L.tail.next=n2
# L.tail=n2
# L.tail.next=L.head

# n3=Node(30)
# L.tail.next=n3
# L.tail=n3
# L.tail.next=L.head
#L.display()
#L.del_beg()
#L.del_end()
# L.del_pos(2)
# L.display()


#stack:it is a data structure which follows LIFO principle  Last In First Out

# class stack:
#     def __init__(self):
#         self.values=[]
#     def push(self,x):
#         self.values=[x]+self.values
#     def pop(self):
#         return self.values.pop(0)

# s=stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.push(40)
# print(s.values)
# print(s.pop())
# print(s.values)

#stack using linked lists
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class stack:
#     def __init__(self):
#         self.top=None
#     def push(self):
#         x=int(input("enter the element to be pushed:"))
#         new=Node(x)
#         if self.top==None:
#             self.top=new
#             self.top.next=None
#         else:
#             temp=self.top
#             new.next=temp
#             self.top=new
#     def pop(self):
#         if self.top is None:
#             print("stack is empty")
#             return
#         if self.top.next==None:
#             print("the popped elememt is",self.top.data)
#             self.top=None
#         else:
#             print("the popped element is",self.top.data)
#             self.top=self.top.next
#     def display(self):
#         if self.top is None:
#             print("The list is Empty")
#             return
#         print("The elements of the list are:")
#         temp=self.top
#         while  temp:
#             print(temp.data,end="=>")
#             temp=temp.next
# s=stack()
# while(True):
#     print("Enter the option from below:")
#     print("1-for push operation")
#     print("2-for pop operation")
#     print("3-for display operation")
#     print("4-for exit")
#     option=int(input("Enter the option:"))
#     if option==1:
#         print("Push operation")
#         s.push()
#     elif option==2:
#         print("pop operataion")
#         s.pop()
#     elif option==3:
#         print("Display operation")
#         s.display()
#     elif option==4:
#         print("exit operation")
#         break
#     else:
#         print("enter a valid option")


#Queue: it is datastructure that follows FIFO (First In First Out) principle.

# class queue:
#     def __init__(self):
#         self.values=[]
#     def enqueue(self,x):
#         self.values.append(x) 
#     def dequeue(self):
#         front=self.values[0]
#         self.values=self.values[1:]
#         return front
# q=queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# print(q.values)
# print(q.dequeue())
# print(q.values)


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class queue:
#     def __init__(self):
#         self.front=None
#         self.rear=None
#     def enqueue(self):
#         x=int(input("Enter the element to be inserted"))
#         new=Node(x)
#         if self.front is None:
#             self.front=new
#             self.rear=new
#             print(f"the element {x} is inserted into the queue")
#         else:
#             self.rear.next=new
#             self.rear=new
#             print(f"the element {x} is inserted into queue")
#     def dequeue(self):
#         if self.front is None:
#             print("The queue is already empty")
#             return
#         if self.front==self.rear:
#             print(f"The element {self.front.data} is removed from queue")
#             self.front=None
#             self.rear=None
#         else:
#             print(f"the element {self.front.data} is removed from queue")
#             self.front=self.front.next
            
            
#     def display(self):
#         if self.front is None:
#             print("queue is empty")
#             return
#         temp=self.front
#         print("The queue elements are:",end=" ")
#         while temp:
#             print(temp.data,end="->")
#             temp=temp.next

# q=queue()
# while(True):

#     print("enter the options for the queue operations:")
#     print("1- for enque")
#     print("2-for deque")
#     print("3-for display")
#     print("4-for exit")
#     option=int(input("Enter your option:"))
#     if option==1:
#         q.enqueue()
#     elif option==2:
#         q.dequeue()
#     elif option==3:
#         q.display()
#     elif option==4:
#         break
#     else:
#         print("Enter a valid option")

#linear search

# def linearsearch(arr,t):
#     for i in range(len(arr)):
#         if arr[i]==t:
#             return i
#     return -1
# arr=list(map(int,input("Enter the elements of the array: ").split(",")))
# t=int(input("Enter the target"))
# r=linearsearch(arr,t)
# print(r)


#Binary Search in arrays 
#cond: array should be sorted. and array should reduce the search space

# def binary_search(arr,t):
#     arr.sort()
#     low=0
#     high=len(arr)-1
#     mid=0
#     while(low<=high):
#         mid=(low+high)//2
#         if arr[mid]==t:
#             print("elemet found at index:",mid)
#             return
#         elif arr[mid]>t:
#             high=mid-1
#         elif arr[mid]<t:
#             low=mid+1
# arr=list(map(int,input("Enter the elements of the array: ").split(",")))
# t=int(input("Enter the element to be searched:"))
# binary_search(arr,t)


# def binary_search(arr,t):
#     arr.sort()
#     low=0
#     high=len(arr)-1
#     while(low<=high):
#         mid=(low+high)//2
#         if arr[mid]==t:
#             return mid
#         elif arr[mid]<t:
#             low=mid+1
#         elif arr[mid]>t:
#             high=mid-1
#     return -1

# arr=list(map(int,input("Enter the array of elements:").split(",")))
# t=int(input("Enter the target element:"))
# r=binary_search(arr,t)

# if r!=-1:
#     print(f"Element found at index:{r}")
# else:
#     print("element not found")

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

#space and time complexities:

# Time and space complexities is denoted by big O notation also know as order of 

#1.Bubble sort:
#Time complexity: worst case : O(n^2) , Best case: O(n) if list is already sorted
#space complexity: O(1) only a constant amount of extra soace is needed.

#Selection sort:
#Time complexity: Worst,average,best case is :O(n^2)
#space complexity:O(1) or constant

#Insertion sort:
# Time complexity: Worst,average case: O(n^2), best case: O(n) if its sorted
# space complexity: O(1) 

#Merge sort:
# Time complexity: worst,Avg,best case is : O(n log n)
# space complexity: O(n) 

#Quick sort:
#Time complexity: Worst: O(n^2), Avg: O(n log n), Best: O(n log n)
#space complexity: O(log n)

# Head sort:
# Time complexity: worst, Avg, Best: O(n log n)
#space complexity: O(1)


# Arrays and linked lists are linear data structures
#Traversal: Traversal refers to the process of visiting all the nodes in a data structure
# such as tree or graph in a systematic way.
# Tree:
# A Tree is a hierarchial data structure consisting of nodes, with a root node and child nodes
# connected by edges.Each node can have multiple child nodes but only one parent except root
# Node: A container for data
# Edge: The connection between two nodes
# Root: The Top node of the tree
# Leaf: A node with no children
# Height: The length of the longest path from the node to a leaf.
# Depth: The length of the path from the root to a node.
# Subtree: A tree consisting of a node and its descendants.

#Types of trees:
# 1.Binary tree: Each node has at most two children left and right
# 2.Binary search tree: A binary tree where left children are less 
# than the parent and right children are greater than the parent.
# 3.AVL Tree: A self balancing binary tree
# 4.Heap tree: A biary tree based structure where the value of the parent node is greater than 
# or equal to its children (max heap) or less than or equal to its children (min-heap).
# node consists of data, left, right   


#Graphs:
#A Graph is a collection of nodes(vertices) and edges (connection between the nodes). 
# Graphs can be directed or undirected and weighted or unweighted.
#Vertex(Node): A connection between two vertices.
#Degree: The Number of edges connected to a vertex
#Path: A sequence of edges connecting a set of vertices.
#Cycle: A path where the first and last vertices are the same.
#Directed Graph: Edges have a direction
#Undirected Graph: Edges have no direction.
# Weighted Graph: Edges have Weights(costs)

#Traversal Algorithms:
# 1.Tree Traversals:
# *Inorder: left, root, right
# *Preorder:Root,left,right
# *Postorder:Left,right,root

#Graph Traversals:
# * Breadth-First-Search(BFS): Uses Queue, Explores neighbors level by level.
# it explores all the neighbors of a node before moving on to their neighbors.
# BFS is often usd for finding the shortest path in an unweighted graph.

# * Depth-First-Search(DFS): Uses a stack, explores as far as possible along each branch before backtracking
#It explores one branch of the graph as far as it can go before exploring other branches
#DFS used for finding connected components, pathfinding or topological sorting













































































