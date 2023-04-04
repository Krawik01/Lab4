
# alphabet = {
#     "A": 1, "Ą": 2, "B": 3, "C": 4, "Ć": 5, "D": 6, "E": 7, "Ę": 8,
#     "F": 9, "G": 10, "H": 11, "I": 12, "J": 13, "K": 14, "L": 15,
#     "Ł": 16, "M": 17, "N": 18, "Ń": 19, "O": 20, "Ó": 21, "P": 22,
#     "R": 23, "S": 24, "Ś": 25, "T": 26, "U": 27, "W": 28, "Y": 29,
#     "Z": 30, "Ź": 31, "Ż": 32
# }
def caesar_cipher(message, key, alphabet=None):
    if alphabet is None:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    result = ""

    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            shifted_index = (index + key) % len(alphabet)
            shifted_letter = alphabet[shifted_index]
            result += shifted_letter
        else:
            result += letter

    return result

print(caesar_cipher("zozol", 3,"AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ"))
