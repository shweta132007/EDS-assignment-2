#PRACTICAL 3

# Question 3.1.1.
#Numpy Array Operations
#code:
import numpy as np
import numpy as np

# Input rows and columns
r, c = map(int, input().split())

# Read elements
elements = []
for _ in range(r):
    elements.extend(map(int, input().split()))

# Create NumPy array and reshape
arr = np.array(elements).reshape(r, c)

# Output
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)




# Question 3.2.1.
#Numpy: Matrix Operations
#code:

import numpy as np

# Input matrices
print("Enter Matrix A:")
matrix_a = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Matrix B:")
matrix_b = np.array([list(map(int, input().split())) for i in range(3)])


# Addition
print("Addition (A + B):")
print(matrix_a + matrix_b)
# Subtraction
print("Subtraction (A - B):")
print(matrix_a - matrix_b)
# Multiplication (element-wise)
print("Element-wise Multiplication (A * B):")
print(matrix_a * matrix_b)
# Matrix multiplication (dot product)
print("A dot B:")
print(np.matmul(matrix_a,matrix_b))
# Transpose
print("Transpose of A:")
print(matrix_a.T)



# Question 
#3.2.2. Numpy: Horizontal and Vertical Stacking of Arrays
#code:
import numpy as np

# Input matrices
print("Enter Array1:")
arr1 = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Array2:")
arr2 = np.array([list(map(int, input().split())) for i in range(3)])

# Perform horizontal stacking (hstack)
h_stack=np.hstack((arr1,arr2))
print("Horizontal Stack:")
print(h_stack)


# Perform vertical stacking (vstack)
print("Vertical Stack:")
v_stack = np.vstack((arr1,arr2))
print(v_stack)



# Question 3.2.3. 
#Numpy: Custom Sequence Generation
#code:
import numpy as np

# Take user input for the start, stop, and step of the sequence
start = int(input())
stop = int(input())
step = int(input())

# Generate the sequence using np.arange()
seq= np.arange(start, stop, step)
# Print the generated sequence
print(seq)



# Question 3.2.4. 
#Numpy: Arithmetic and Statistical Operations, Mathematical Operations, Bitwise Operators
#code:
import numpy as np

def array_operations(A, B):

	# Convert A and B to NumPy arrays
	arr1=np.array(A)
	arr2=np.array(B)

	# Arithmetic Operations
	sum_result = arr1 + arr2
	diff_result = arr1 - arr2
	prod_result = arr1 * arr2

	# Statistical Operations
	mean_A = np.mean(arr1)
	median_A = np.median(arr1)
	std_dev_A = np.std(arr1)

	# Bitwise Operations
	and_result = arr1 & arr2
	or_result =  arr1 | arr2
	xor_result = arr1 ^ arr2

    # Output results with one space between each element
	print("Element-wise Sum:", ' '.join(map(str, sum_result)))
	print("Element-wise Difference:", ' '.join(map(str, diff_result)))
	print("Element-wise Product:", ' '.join(map(str, prod_result)))
    
	print(f"Mean of A: {mean_A}")
	print(f"Median of A: {median_A}")
	print(f"Standard Deviation of A: {std_dev_A}")
    
	print("Bitwise AND:", ' '.join(map(str, and_result)))
	print("Bitwise OR:", ' '.join(map(str, or_result)))
	print("Bitwise XOR:", ' '.join(map(str, xor_result)))

A = list(map(int, input().split()))  # Elements of array A
B = list(map(int, input().split()))  # Elements of array B
array_operations(A, B)




# Question 3.2.5. 
#Numpy: Copying and Viewing Arrays
#code:
import numpy as np

inputlist = list(map(int,input().split(" ")))

# Original array
original_array = np.array(inputlist)

# Create a view
view_array = original_array.view()


# Create a copy
copy_array = original_array.copy()

# Modify the view
view_array[0] = 99
print("Original array after modifying view:", original_array)
print("View array:", view_array)

# Modify the copy
copy_array[1] = 88
print("Original array after modifying copy:", original_array)
print("Copy array:", copy_array)



#3.2.6. 
#Numpy: Searching, Sorting, Counting, Broadcasting
#code:
import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

# Find indices where value matches in array1
indices = np.where(array1 == search_value)[0]
print(indices)
# Count occurrences in array1
count = np.count_nonzero(array1 == count_value)
print(count)
# Broadcasting addition
broadcasted_array = array1 + broadcast_value
print(broadcasted_array)
# Sort the first array
sorted_array=np.sort(array1)
print(sorted_array)




# Question 3.2.7
#Student Data Analysis and Operations
#code:
import numpy as np

a = np.loadtxt("Sample.csv", delimiter=',', skiprows=1)


# 1
print("All student Details:\n", a)

# 2
print("Total Students:", a.shape[0])

# 3
print("All Student Roll Nos", a[:, 0])

# 4
print("Subject 1 Marks", a[:, 1])

# 5
print("Min marks in Subject 2", np.min(a[:, 2]))

# 6
print("Max marks in Subject 3", np.max(a[:, 3]))

# 7
print("All subject marks:", a[:, 1:])

# 8
print("Total Marks", np.sum(a[:, 1:], axis=1))

# 9 (no label)
print(np.round(np.mean(a[:, 1:], axis=1), 1))

# 10
print("Average Marks of each subject", np.round(np.mean(a[:, 1:], axis=0), 1))

# 11
print("Average Marks of S1 and S2", np.round(np.mean(a[:, 1:3], axis=0), 1))

# 12
print("Average Marks of S1 and S3", np.round(np.mean(a[:, [1, 3]], axis=0), 1))

# 13
print("Roll no who got maximum marks in Subject 3", a[np.argmax(a[:, 3]), 0])

# 14
print("Roll no who got minimum marks in Subject 2", a[np.argmin(a[:, 2]), 0])

# 15
print("Roll no who got 24 marks in Subject 2", a[a[:, 2] == 24][:, [0]])

# 16
print("Count of students who got marks in Subject 1 < 40", np.sum(a[:, 1] < 40))

# 17
print("Count of students who got marks in Subject 2 > 90:", np.sum(a[:, 2] > 90))

# 18
print("Count of students in each subject who got marks >= 90:", np.sum(a[:, 1:] >= 90, axis=0))

# 19
print("Roll no:", a[:, 0])
print("Count of subjects in which student got marks >= 90:", np.sum(a[:, 1:] >= 90, axis=1))

# 20 (no label)
print(np.sort(a[:, 1]))

# 21 (no label)
print(a[(a[:, 1] >= 50) & (a[:, 1] <= 90)])

# IMPORTANT extra print (required by expected output)
print(a)

# 22
print(np.where(a[:, 1] == 79))


