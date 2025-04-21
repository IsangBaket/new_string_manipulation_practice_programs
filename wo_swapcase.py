# Prog08. swapcase() reverse the casing of each of the character of the string. 
# Create a program that do the same functionality without using swapcase() function.

def max_swapcase(string):
    while True
        for char in string:
            result = ''
            if "A" <= char <= "Z":
                result += chr(ord(char) + 32)
            if "a" <= char <= "z":
                result += chr(ord(char) - 32)
            return result
    

string = input("Input a string with an upper case and a lower case: ")  # asks user for a string

result = max_swapcase(string)   # calls function

print(result)   # prints result of function