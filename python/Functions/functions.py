
# Square of a number
def square(x):
    return x**2

print(square(2))

#Multiple Parameters in function

def multiparam(a,b):
    return a+b

print(multiparam(5,10))

# Polymorphism 
class Animal:                   #Parent Class/Super class
    def __init__(self,name):     #Constructor method
        self.name = name

    def speak(self):             #Method 
        print("I am an animal") 
        
class Dog(Animal):                       #Child or Sub class
    def speak(self):                      #Overriding the Method from Parent Class
        print("Woof Woof I am a dog")

d=Dog("Tommy")  
d.speak() 
# simpler example of Polymorphism
def multiply(p1,p2):
    return p1 * p2 # work for both string and number

print(multiply('h',2))
print(multiply(8,9))