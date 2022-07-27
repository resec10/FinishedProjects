def encoder(word):
    #word = input()
    man = []
    for jh in str.lower(word):
        man.append(jh)

    ae = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', " ", '?', ".", "!", ',', '\n', ':', "'", '(', ')']
    letter = ['#', '~', 'd', '(', '&', '%', 'a', '+', 'k', 'ș', '^', '*', 'l', 'z', '/', '@', 'x', ']', '`', 't', 'e', 'ă', 'b', '$', 'n', '>', " ", '?', '.', '!', ',', '\n', ':', "o", 'j', 'y']
    damn = []
    for gh in man:
        dudd = ae.index(gh)
        damn.append(letter[dudd])
    answer = "".join(damn)
    print(answer)

encoder('''Would you rather be murdered with a knife or a hammer? Just want to know for future reference.''')
