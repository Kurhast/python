alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cesar_chiffrement(message_clair,KEY):
    chiffre = ''
    message_clair=message_clair.upper()
    for i in message_clair:
        if i in alphabet:
            index = alphabet.find(i)
            index_decale = (index+KEY)%26
            chiffre = chiffre+alphabet[index_decale]
    return chiffre

def cesar_dechiffrement(message_chiffre, KEY):
    dechiffre = ''
    message_chiffre = message_chiffre.upper()
    for i in message_chiffre:
        if i in alphabet:
            index = alphabet.find(i)
            index_decale = (index - KEY) % 26
            dechiffre = dechiffre + alphabet[index_decale]
    return dechiffre

def attaque_force_brut(message_chiffre):
    for key in range(26):
        dechiffre = cesar_dechiffrement(message_chiffre, key)
        print(f'Clé {key}: {dechiffre}')

resultat = cesar_dechiffrement('NYMZFRRW', 10)
print(f'Message chiffré: {resultat}')

print('Resultat de l\'attaque par force brute:')
attaque_force_brut(resultat)