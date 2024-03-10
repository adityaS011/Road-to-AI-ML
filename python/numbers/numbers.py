
x = 2

y = 3

z = 4

# Bodmas
print(x+y)
print((x+y)*z)
print(x**y) # raise to the power of second var

# Comparisions
print(x>4)
print(x!=4)

# Logical Operators
print(x<y and y<z)
print(x<y or y<z)

# ??Maths

import math

print(math.floor(3.5))
print(math.ceil(3.5))
print(math.trunc(-3.5)) # Towards 0
print(math.trunc(3.5)) # Towards 0




print((2+ 1j)*3) # Complex Numbers in Python

print(0o20) #Octal umbers 
print(0x20) #HexaDecimal numbers 
print(0b10000) #Binary numbers 
# or
print(int('64', 8)) # Convert String to int with base
print(int('64', 16)) # Convert String to int with base
print(int('10000', 2)) # Convert String to int with base

# Bitwise Operations
print(x>>2)
print(x<<2)

# Random

import random

print(random.random())
print(random.randint(1,20))

arr=['apple','banana','cherry']
print(random.choice(arr))

import datetime
# Time 
date =  datetime.datetime.now()
print(date) 

timestamp = date.timestamp() 
print(timestamp)

# Set

set1={1,9,2}
set2={1,2,3,4,5,6}

print(set1 | set2) # union
print(set1 & set2) # intersection
print(set1 - set2) # diff
# empty{} are dict in python by default so empty set are declared as set()

