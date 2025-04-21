# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. 
# Create a program that do the same functionality without using center() function.

def max_center(word,padding,string): 
    padding = int(padding) - len(word)  # calculates total padding
    left_padding = padding // 2   # calculate left and right padding
    right_padding = padding - left_padding
    return left_padding * string + word + string * right_padding    # returns centered word


word = input("Input a word you want to format: ")   # asks user for what word to format
padding = input("Input how many paddings you want: ")   # asks user how much padding they want
string = input("Input padding string: ")    # asks what string they want to format the padding with

centered = max_center(word,padding,string)  # calls out the function

print(centered)    # prints out the result