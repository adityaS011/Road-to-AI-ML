def printing(n):
    print ("This is the number",n)

def func(n):
    printing(n)

func(4)

# To check memory refrence is same or not in python is done by is keyword
a=[1,2]
b=[1,2]

print(a==b) # to check values
print(b is a) # same value but diff refrence

c= a
print(c is a) # same refrence

