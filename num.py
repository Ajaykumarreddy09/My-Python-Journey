# import numpy as np
# arr=np.array((1,2,3,4,5))
# print(arr)
# print(arr[2]+arr[3])

# import numpy as np
# a=np.array((4))
# b=np.array([1,2,3])

# d=np.array([[1,2],[3,4]])

# print(a.ndim)
# print(b.ndim)

# print(d.ndim)

# import numpy as np
# arr=np.array([1,2,3], ndmin=5)
# print(arr)
# print(arr.ndim)

import numpy as np
# arr=np.array([[1,2,3,4,5],[5,6,7,8,9]])
# print("output:", arr[0,2])
# print(arr[0,-4])

# arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(arr[0,1,2])

#array slicing

# arr=np.array([1,2,3,4,5,6,7])
# print(arr[1:5:2])
# print(arr[3:])
# arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr[0:3,2])

# arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr[0:,1:3])

# #data types in python
# integer,float,boolean,unsigned integer,complex float,
# datetime,obhect,string,unicode

# arr=np.array([1,2,3,4,5,6,7])
# print(type(arr))
# print(arr.dtype)

#type casting
# arr=np.array([1,2,3],dtype='S')
# print(arr)
# print(arr.dtype)

# arr=np.array(['a','b','c'])
# print(type(arr))
# print(arr.dtype)

# copy()--is the new array anny changes in the copy array will not affect the original array
#  view()-- is just a view of original array-- changes in original array will affect the view.

 #reshaping an array
# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# na=a.reshape(2,2,1,3) # the multiplication of these elements should be equal to total no of elements 
# print(na)
# print(na.ndim)

# a=np.array([1,2,3,4,5,6,7,8,9])
# n=a.reshape(1,3,-1)
# print(n)

# a=np.array([1,2,3])
# for i in a:
#     print(i)

# a=np.array([[1,2,3],[4,5,6]])
# for i in a:
#     print(i)

# a=np.array([[1,2,3],[4,5,6]])
# for x in a:
#     for i in x:  # if its 3 dimensional then it we should use 3 forloops..as dim increase we increase the loops too
#         print(i)

# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# na=np.concatenate((arr1,arr2))
# print(na)
import numpy as np

# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# a=np.hstack((arr1, arr2))
# a2=np.vstack((arr1, arr2))
# print(a)

# arr1=np.array([-1,-2,-3])
# arr2=np.array([4,5,6])
# a=np.stack((arr1, arr2),axis=1)
# a2=np.vstack((arr1, arr2))
# print(a)
# print(a2)

# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# a=np.hstack((arr1, arr2))
# a2=np.hstack((arr1, arr2))
# print(a2)

# a=np.array([1,2,3,4,5,6])
# n=np.array_split(a,5)
# print(n)

# a=np.array([1,2,3,4,5,6])
# n=np.array_split(a,3)
# print(n)

# a=np.array([1,2,3,4,5,6])
# n=np.array_split(a,5)
# print(n)
# print(n[1])

# a=np.array([1,2,3,4,5,6,7,8])
# n=np.where(a%2==0)
# print(n)

# a=np.array([1,2,3,4,10,45,5,6,7,8])
# n=np.sort(a)
# print(n)

# arr=np.array([41,42,43,44])
# filter_arr=[]
# for e in arr:
#     if e > 42:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
# na=arr[filter_arr]
# print(na)
# print(filter_arr)













































