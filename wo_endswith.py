# Prog05. endswith() check if the string end part matches the function parameter. 
# Create a program that do the same functionality without using endswith() function.

def max_endswith():
    user_input = input("Input a string: ")
    user_suffix = input("Input a suffix: ")
    
    string = len(user_input)
    suffix = len(user_suffix)

    ends_with = str[string - suffix]
    
    
    if user_suffix == ends_with:
        print("True")
    else: 
        print("False")


max_endswith()
