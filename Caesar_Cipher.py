def encrypt(word):
    new_word = ""
    for letter in word:
        letter = ord(letter)
        letter += 3
        if letter > 122:
            letter -= 26
        letter = chr(letter)
        new_word += letter
    return new_word

def unencrypt(word):
    new_word = ""
    for letter in word:
        letter = ord(letter)
        letter -= 3
        print(letter)
        if letter < 97:
            letter += 26
        letter = chr(letter)
        new_word += letter
    return new_word
