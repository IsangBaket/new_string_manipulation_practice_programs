# Prog04. isupper() check if all characters of the string is on upper case. 
# Create a program that do the same functionality without using isupper() function.

def max_isupper():
    string = input("Enter a word, phrase, or sentence: ")

    for char in string:
        if "a" <= char <= "z":
            print("False")
        else: 
            print("True")

max_isupper()

