# Function to calculate the square of a number
def square(x):
    """
    This function takes a number as an argument and returns the square of that number.
    """
    return x**2

print(square(2))

# Function to calculate the sum of two numbers
def multiparam(a, b):
    """
    This function takes two numbers as arguments and returns their sum.
    """
    return a+b

print(multiparam(5,10))

# Function to multiply two numbers or concatenate two strings
def multiply(p1, p2):
    """
    This function takes two parameters and multiplies them if they are numbers, or concatenates them if they are strings.
    """
    return p1 * p2

print(multiply('h',2))
print(multiply(8,9))

# Function to add three numbers with default parameter values
def add_numbers(a=0, b=0, c=0):
    """
    This function takes three numbers as arguments with default value 0 and returns their sum.
    """
    return a + b + c

print(add_numbers())
print(add_numbers(3,4))
print(add_numbers(3,4,6))

# Lambda function to double a number
double = lambda x: x*2 #  this is equivalent to def double(x): return x*2

print("Lambda Funtion: ",double(7))

# Recursive function to calculate the factorial of a number
def factorial(n):
    """
    This function takes a number as an argument and returns its factorial using recursion.
    """
    if n == 0 or n==1 :
        return 1
    else:
        return n * factorial(n-1)

print("Factorial", factorial(5))

# Function to print the sum of all positional arguments passed
def print_all(*args): #  args will contain all positional arguments as tuple.
    """
    This function takes any number of positional arguments and returns their sum.
    """
    return(sum(args))

print("*args method for sum:",print_all(1,2,3,4,5))

# Function to print key-value pairs passed as keyword arguments
def greet_me(**kwargs):
    """
    This function takes any number of keyword arguments and prints each key-value pair.
    """
    for key,value in kwargs.items():
        # format method takes two parameters, first one is string and second one is variable which we want to put
        print(f"{key} = {value}")

greet_me(first_name="John", last_name="Doe", caste="general")

# Function to generate a generator that counts down from a given number
def countdown(n):
    """
    This function takes a number as an argument and returns a generator that counts down from that number.
    """
    while n>0:
        yield n #  here instead of returning value, it yields it.
        n -= 1

for i in countdown(10):
    print(i)

print('Closure and Scope:')
# Function defined inside another function with access to variables from outer scope
outer_var=9
def inner_func():
    """
    This function has access to the variable `outer_var` from the outer scope.
    """
    inner_var=8
    def even_or_odd():
        """
        This function checks if the sum of `inner_var` and `outer_var` is even or odd.
        """
        global outer_var # this keyword allows us to access the variable from outside of current scope.
        nonlocal inner_var # this keyword  allows us to access the variable from inside of current scope.
        if (inner_var+outer_var)%2==0:
            return f"The number is {inner_var+outer_var}, It's Even."
        else:
            return f"The number is {inner_var+outer_var}, It's Odd."
    return even_or_odd()

print(inner_func())

# Closure Exapmle 2
def f1():
    x=88
    def f2():
        print(x)
    return f2 # returning the defination of f2 function

myResult =f1() # its also have access of x because of closure  property all associted ref are returned
myResult()  # execute def of f2 i.e executing the function 