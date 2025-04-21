# Prog09. capitalize() makes the first letter of the string, capital letter.
# And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

def max_capitalize(string):
    first_char = chr(ord(string[0]) - 32)
    following_char = chr(ord(string[1:] + 32))
    return first_char + following_char
    

string = input("Input a word to capitalize: ")  # asks user for a string

result = max_capitalize(string)   # calls function

print(result)   # prints result of function