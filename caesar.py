def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    i = alphabet.index(letter)
    return i

def rotate_character(char, rot):
    r_alphabet = "abcdefghijklmnopqrstuvwxyz"
    if char.isupper() == True:
        char = char.lower()
        newpos = rot + alphabet_position(char)
        if newpos < 26:
            newchar = r_alphabet[newpos]
            newchar = newchar.upper()
        else:
            newchar = r_alphabet[newpos % 26]
            newchar = newchar.upper()
    elif char not in r_alphabet:
        return char
    else:
        newpos = rot + alphabet_position(char)
        if newpos < 26:
            newchar = r_alphabet[newpos]
        else:
            newchar = r_alphabet[newpos % 26]
    return newchar

def encrypt(text, rot):
    newtext = ""
    for char in list(text):
        newtext = newtext + rotate_character(char, rot)
    return newtext
