# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter.
# Create a program that do the same functionality without using removeprefix() function.

def max_removeprefix(str, prefix):
    if len(str) >= len(prefix) and str[:len(prefix)] == prefix:     #searches for the prefix
        return str[len(prefix):] 
    return str

str = input("Input any word, phrase, or sentence: ")
prefix = input("Input the prefix that you want to remove: ")

result = max_removeprefix(str, prefix)

print(result)