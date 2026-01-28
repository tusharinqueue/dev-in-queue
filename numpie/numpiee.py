import numpy as np


arr1 = np.array([1,2,3,4])
# THIS IS 1D ARRAY
arr2 = np.array([[1,2,3],[4,5,6]])
#this is a 2d array

#beyond this 2d+ array is called tensor
arr3 = np.array([[[1,2,3],[4,5,6]],
                 [[12,23,34],[56,67,78]]])

#1d=vector
#2d=matrix
#3d+ = tensor

#-------------------------------------------------------------------------------

#numpy array vs normal python array or why does numpy actually exist
py_list = [1, 2, 3]
print("Python list multiplication ", py_list * 2)

np_array = np.array([1, 2, 3]) #element wise multiplication
print("Python array multiplication ", np_array * 2)
#1st reason to do maths in python ^^^^^^^^^

import time
start = time.time()
py_list = [i*2 for i in range(1000000)]
print("\n List operation time: ", time.time() - start)

start = time.time()
np_array = np.arange(1000000) * 2
print("\n Numpy operation time: ", time.time() - start)
#2nd reason , its wayy faster than traditional python list^^^

#----------------------------------------------------------------------------------

#creating array from scratch

zero_arr = np.zeros((2,4))
print(zero_arr)

ones_arr= np.ones((3,4))
print(ones_arr)

full_arr = np.full((3,4),9)
print(full_arr)

random_arr = np.random.random((3,4))
print(random_arr)
#random values are between 0and 1

sequence_arr = np.arange(0,10,2)
print(sequence_arr)
#IF WE ENTERED (0,11,2) RESULT WOULD BE SAME

#----------------------------------------------------------
#Array properties

print("Shape ", arr2.shape)  #gives no of rows and columns
print("Dimension ", arr2.ndim) #give no of dimensions
print("Size ", arr2.size) #no of elements
print("DType ", arr2.dtype) #data type in arrays

#NOTE-- numpy is most efficient in only one datatype array
#if its mixed of two dta types it will not be that efficient as its not build that way

#------------------------------------------------------------
#Array Reshaping

arri = np.arange(12)
print("Original array ", arri)

reshaped = arri.reshape((3, 4))
print("\n Reshaped array ", reshaped)

flattened = reshaped.flatten()
print("\n Flattened array ", flattened)

# ravel (returns view, instead of copy)
raveled = reshaped.ravel()
print("\n raveled array ", raveled)

# Transpose
transpose = reshaped.T
print("\n Transposed array ", transpose)
