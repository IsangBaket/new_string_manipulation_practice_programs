def max_lower():
    string = input("Enter a word, phrase, or sentence: ")
    result = ""
    for char in string:
        if "A" <= char <= "Z":
            result += chr(ord(char) + 32)
        else:
            result += char
                   
    print(result)

max_lower



