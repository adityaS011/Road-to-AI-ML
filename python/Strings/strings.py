# \ or r"" (raw string) is used to treat keyword as a text while printing
str = "0123456789"   
print(str)

# Slicing
print(str[2:8])
print(str[2:8:2]) # hooping 1 elements

# Methods
methods = "random, Text "
print('\n')
print(methods.capitalize())   # Capitalizes the first letter of a string
print(methods.lower())        # Converts all letters to lowercase   
print(methods.upper())        # Converts all letters to uppercase
print(methods.title())       # Converts the first letter of each word to Uppercase
print(len(methods))          # Returns the number of characters in a string
print(methods.split(','))     # Split a string into a list
print(methods.strip())        # Removes leading and trailing whitespaces
print(methods.find('Text'))   # Finds the position of a substring
#Extras
print(methods.isalpha())     # Check if the string contains only letters (no spaces or numbers).
print(methods.isdigit())     # Check if the string contains only digits (no letters or spaces).
print(methods.isalnum())     # Check if the string contains only alphanumeric characters (letters and numbers). No spaces
print(methods.isspace())     # Check if the string is empty or consists of whitespace

# String Lists

variety = ["Pasta","Noodles","Soup"]
print("\n")
print(" ".join(variety))      # Joins items in a list into one string with a specified separator
print(",".join(variety))         # Comma separated values
print("\n".join(variety))        # New line separated values

# Formatting Strings

name = input("Enter your name : ")
age = int(input("Enter your age : "))   
country = input("Enter your country : ")
language = input("What language do you speak? ")

print("\n\nHello {} , \nYou are {} years old , \nLive in {} \nAnd Speak {} .".format(name,age,country,language))
#OR
formatted_string = f"""\
Your Name : {name}
Age : {age}
Country : {country}
Language : {language}"""

print(formatted_string)
