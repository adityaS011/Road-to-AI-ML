
li = [10,20,30,40,50]

l2 = li  # gives refrence of li to l2 of the same memory space where list is stored

l3 = l2[:] # creates a copy of li and then is refered by l3 so both are not refering to same memory sapce
print(l3,"\n") 

# copy and deepcopy is used to copy by importing (import copy) module in python


# iterating a list
for i in range(len(li)):
    li[i] = li[i] + 1
    print( "Value after increment: ", li[i])



