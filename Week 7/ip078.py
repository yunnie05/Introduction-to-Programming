import string

def caesar_cipher(text, k):
    new=""
    for i in text:
        if i== " ":
            new+= " "
            continue
        if i in string.punctuation:
            new += i
            continue
        aux= ord(i) - ord("a")
        aux= ((aux + k) % 26)
        new += chr(ord("a") + aux)
    return new