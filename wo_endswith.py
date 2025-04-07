# Prog05. endswith() check if the string end part matches the function parameter. 
# Create a program that do the same functionality without using endswith() function.

def max_endswith():
    string = input("Input a string: ")
    suffix = input("Input a suffix: ")
    
    for char in string:
        if char == suffix:
            print("True")
            return
        else: 
            print("False")


max_endswith()
