# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.
def max_lower():
    string = input("Enter a word, phrase, or sentence: ")
    result = ""
    for char in string:
        if "A" <= char <= "Z":
            result += chr(ord(char) + 32) # link to ascii value chart: https://www.w3resource.com/w3r_images/java-basic-image-exercise-41.png
        else:
            result += char

    print(result)

max_lower()



