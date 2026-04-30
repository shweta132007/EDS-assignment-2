# Practical  1- 
#Question 1.1.1
# Calculate Momentum (p = m × v)
#code:
mass=float(input())
velocity=float(input())
momentum=mass*velocity
print(f"{momentum:.2f}kgm/s")



# Question 1.1.2. 
#Conditional Calculation Based on the Number of Digits
import math
n=int(input())
if 0<n<10:
	print(n**2)
elif 10<=n<100:
	print(f"{math.sqrt(n):.2f}")
elif 100<=n<1000:
	print(f"{n**(1/3):.2f}")
else:
	print("Invalid")



# Question 1.1.3. 
#Days between Two Dates
#code:
from datetime import date 
from datetime import datetime

date1 = input().strip()
date2 = input().strip()

d1 = datetime.strptime(date1, "%Y-%m-%d")
d2 = datetime.strptime(date2, "%Y-%m-%d")
difference = (d2 - d1).days
print(difference)



# Question 1.1.4.
#Reverse a Number
#code:
num=int(input())
text=str(num)
reversed_num=text[::-1]
print(reversed_num)



# Question 1.1.5.
#Multiplication Table
#code:
#write your code here...
n=int(input())
for i in range(1,11):
	print(f"{n} x {i} = {n*i}")



# Question 1.2.1. 
#Pass or Fail
#code:
n = int(input())
marks = list(map(int, input().split()))

# Check if any subject is failed
if any(m < 40 for m in marks):
    print("Fail")
else:
    aggregate = sum(marks) / n
    print(f"Aggregate Percentage: {aggregate:.2f}")
    
    if aggregate > 75:
        print("Grade: Distinction")
    elif aggregate >= 60:
        print("Grade: First Division")
    elif aggregate >= 50:
        print("Grade: Second Division")
    elif aggregate >= 40:
        print("Grade: Third Division")



# Question 1.2.2. 
#Fibonacci Series
#code:
def fibonacci(n):
	if n==1:
		return 0
	elif n==2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)


n = int(input())
for i in range(1, n + 1):
	print(fibonacci(i), end=" ")


# Question 1.2.3. 
#Pattern - 1
#code:
#Type Content here...
n=int(input())
for i in range(1,n+1):
	print('* '*i)

# Question 1.2.3. 
#Pattern - 1
#code:
# Type Content here...
n=int(input())
for i in range(1,n+1):
	for j in range(1,i+1):
		print(j ,end=' ')
	print()



