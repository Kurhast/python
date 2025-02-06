import matplotlib.pyplot as plt

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def analyse(texte):
    texte = texte.upper()
    frequence = {}
    for i in alphabet:
        frequence[i] = 0
    for i in texte:
        if i in alphabet:
            frequence[i] += 1
    return frequence

def afficher_graphique(frequence):
    lettres = list(frequence.keys())
    valeurs = list(frequence.values())

    plt.figure(figsize=(10, 5))
    plt.bar(lettres, valeurs, color='blue')
    plt.xlabel('Lettres')
    plt.ylabel('Fréquence')
    plt.title('Fréquence des lettres dans le texte')
    plt.show()

texte = 'ZRSCRSXQDBSMUCFSMDSWCSXDYQSFSXQYFOBMBONOXDSKVCPYBKVVCYBDCYPCOXCSDSFOKMMYEXDCCEMRKCOWKSVMYBZYBKDOSXDBKXODCKXNWYBOOFOXPYBMKEDSYECECOBCSDCCYWODSWOCNSPPSMEVDDYNODOMDKZRSCRSXQKDDKMUDROCOKDDKMUCLOMYWOWYBOCYZRSCDSMKDONYFOBDSWOKXNRKMUOBCPSXNGKICDYDKSVYBDROSBCMKWCKXNQSFOFOBIMYXFSXMSXQWOCCKQOCDRKDMKXOKCSVIDBSZZOYZVOEZDROPSBCDDRSXQIYEMKXNYDYZBYDOMDIYEBCOVPGROXECSXQDROSXDOBXODSCDYOWZVYIMYWWYXCOXCOLOPYBORKXNSXQYFOBCOXCSDSFOSXPYBWKDSYXGROXIYEQODKXKVOBDPBYWIYEBLKXUYBYDROBWKTYBSXCDSDEDSYXXOFOBMVSMUDROVSXUSXDROOWKSVSXCDOKNYZOXIYEBLBYGCOBGSXNYGKXNDIZODROKNNBOCCNSBOMDVISXDYDROEBVPSOVNCYIYEMKXWKUOCEBODROCSDOSCBOKV'
frequence = analyse(texte)
print(frequence)
afficher_graphique(frequence)

def cesar_crack_cle(texte):
    freq = analyse(texte)
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print(freq)
    cle_possible = alphabet.find(freq[0][0]) - alphabet.find('E')
    print(f'Clé possible: {cle_possible}')

cesar_crack_cle(texte)