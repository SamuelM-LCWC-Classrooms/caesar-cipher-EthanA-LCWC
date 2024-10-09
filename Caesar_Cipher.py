def encrypt(word, shift):
    new_word = ""
    for letter in word:
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
        letter = ord(letter)
        letter -= shift
        print(letter)
        if letter < 97:
            letter += 26
        letter = chr(letter)
        new_word += letter
    return new_word
