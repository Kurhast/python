alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere_chiffrement(message, key):
    message = message.upper()
    key = key.upper()
    message_chiffre = ''
    clef_index = 0
    for c in message:
        if c in alphabet:
            index = alphabet.find(c)
            index_key = alphabet.find(key[clef_index % len(key)])
            index_decale = (index + index_key) % 26
            message_chiffre += alphabet[index_decale]
            clef_index += 1
    return message_chiffre

print(vigenere_chiffrement('NYMZFRRW', 'ANSSI'))