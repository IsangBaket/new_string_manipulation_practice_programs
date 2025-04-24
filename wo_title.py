# Prog10. title() makes all first letter of each word in the string, capital letter. 
# And all other letter in small case. Create a program that do the same functionality without using title() function.

def max_title(string):
    string = string.split()
    first_char = chr(ord(string[0]) - 32)

    following_char = ''
    for char in string[1:]:
        if 'A' <= char <= 'Z':
            following_char += chr(ord(char) + 32)
        else: 
            following_char += char
    return first_char + following_char

    

string = input("Input a phrase or sentence to capitalize: ")  # asks user for a string

result = max_title(string)   # calls function

print(result)   # prints result of function