# Prog08. swapcase() reverse the casing of each of the character of the string. 
# Create a program that do the same functionality without using swapcase() function.

def max_swapcase(string):
    result = ''     # this is where the transformed characters are stored
    for char in string:
        if "A" <= char <= "Z":      # this transforms every upper case to lower case
            result += chr(ord(char) + 32)
        elif "a" <= char <= "z":    # transforms every lower case to upper case
            result += chr(ord(char) - 32)
    return result
    

string = input("Input a string with an upper case and a lower case: ")  # asks user for a string

result = max_swapcase(string)   # calls function

print(result)   # prints result of function