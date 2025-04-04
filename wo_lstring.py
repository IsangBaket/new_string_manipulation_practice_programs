# Prog01. lstrip() remove the space characters at the beginning of the string. 
# Create a program that do the same functionality without using lstrip() function.

name = input("Input your name with spaces in the front: ")

index = 0

while index < len(name) and name[index] == " ":
    index += 1

print(name[index:])