# Set of Key and value pairs are refered as Dictanary in python somewhat like a map

dict = {0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four"}  # Dictionary is declared by using {}
print(dict)

# for i in dict:
#     print(i,dict[i])

for key,values in dict.items():
    print(key,":",values)

dict[5]= "Five"
print(dict)

del dict[5] #or dict.pop(5)
print(dict)


value=dict.get(6,"Six does not exist")
print(value)

keys=dict.keys()   # returns list of keys present in the dictionary
print(keys)

values=dict.values()  # Returns List of values present in the dictionary
print(values)

key_value=dict.items()  #Returns List of tuples consist of key-value pair
print(key_value)

matrix= {
    "row": {1:"One",2:"Two"},
    "column": {3:"Three", 4:"Four"},
}

print(matrix["row"][1])

squared_num ={x:x**2 for x in range(6)}
print(squared_num)

# Copying Dictionary

new_dict = dict.fromkeys(dict.keys(), "example")
print(new_dict)