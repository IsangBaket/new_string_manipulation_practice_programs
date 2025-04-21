# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. 
# Create a program that do the same functionality without using ljust() function.

def max_ljust(word,padding,string): 
    padding = int(padding)   # transform user input to integer
    padding = padding - len(word)   
    return word + padding * string   # returns justified word


word = input("Input a word you want to format: ")   # asks user for what word to format
padding = input("Input how many paddings you want: ")   # asks user how much padding they want
string = input("Input padding string: ")    # asks what string they want to format the padding with

justified = max_ljust(word,padding,string)  # calls out the function

print(justified)    # prints out the result