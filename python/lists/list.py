
li = [0,1,2,3,4,5]

l2 = li  # gives refrence of li to l2 of the same memory space where list is stored

l3 = l2[:] # creates a copy of li and then is refered by l3 so both are not refering to same memory sapce
print(l3,"\n") 

# copy and deepcopy is used to copy by importing (import copy) module in python


# iterating a list
for i in range(len(l3)):
    l3[i] = l3[i] + 1
    print( "Value after increment: ", l3[i])

# Delete last Element
l2.pop()
print('\nPoped last element: ',l2)


print(l2)
# Reverse List using slicing 
li_rev = li[::-1]    
print("\nReversed List :", li_rev)    

# Splitting List into two parts
first_half = li[:len(li)//2]    
second_half = li[len(li)//2:]         

print("First half of list:", first_half)          
print("Second half of list:", second_half)  


# Check if element present in list or not
if 2 in li:
    print('Yes 2 is present\n')
else:   
    print('No 2 is not present')

# Removing all occurrences of an element from the list
li.remove(4)
print("Removed last Element: ",li)

# Push element at end  of list
li.append(4)
   

# Reverse sorting the list
li.sort(reverse=True)          
print("Reversed List: ",li)              

# Sorting the list
li.sort()     
print("Sorted List: ",li) 

# Joining elements of a list to form a string
str_join = ' | '.join([str(i) for i in li])               
print("\nJoined String: ", str_join)                                               

# Summation of all elements in the list
sum_of_list = sum(li)                         
print("Sum of List Elements: ", sum_of_list) 

# Product of all elements in the list 
li.remove(0)
product_of_list = 1
for i in li:
    product_of_list *= i
print("Product of List Elements: ", product_of_list) 

# Finding index of an element in a list
index = li.index(3)             
print("Index of 3 is: ",index)                                             

# Insertion of elements in list
li.insert(0, 'Zebra')  # Inserting at beginning
li.append('Dolphin')   # Inserting at last position
print('Inserted list: ',li)