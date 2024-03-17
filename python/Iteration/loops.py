import time

print("Hello Worl")

username = "Aditya"
print(username)

f = open('loops.py')
contents = f.readline() 
print(f)
iteration = f.__next__()
print(f) 

for line in open('loops.py'):
    print(line)