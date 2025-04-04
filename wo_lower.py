# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.
def max_lower():
    string = input("Enter a word, phrase, or sentence: ")
    result = ""
    for char in string:
        if "A" <= char <= "Z":
            result += chr(ord(char) + 32)
        else:
            result += char

    print(result)

max_lower()



