def encrypt(word, shift):
    new_word = ""
    for letter in word:
        if letter == " ":
            new_word += " "
        else:
            letter = ord(letter)
            letter += shift
            if letter > 122:
                letter -= 26
            letter = chr(letter)
            new_word += letter
    return new_word

def unencrypt(word, shift):
    new_word = ""
    for letter in word:
        if letter == " ":
            new_word += " "
        else:
            letter = ord(letter)
            letter -= shift
            if letter < 97:
                letter += 26
            letter = chr(letter)
            new_word += letter
    return new_word
