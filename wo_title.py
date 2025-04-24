# Prog10. title() makes all first letter of each word in the string, capital letter. 
# And all other letter in small case. Create a program that do the same functionality without using title() function.

def max_title(string):
    words = string.split()
    result = []

    for word in words:
        if word:  # check if word is not empty
            first_char = word[0]
            if 'a' <= first_char <= 'z':
                first_char = chr(ord(first_char) - 32)  # to uppercase
            new_word = first_char

            for char in word[1:]:
                if 'A' <= char <= 'Z':
                    char = chr(ord(char) + 32)  # to lowercase
                new_word += char

            result.append(new_word)
        else:
            result.append('')

    return ' '.join(result)

string = input("Input a phrase or sentence to capitalize: ")  # asks user for a string

result = max_title(string)   # calls function

print(result)   # prints result of function

