def decoder(word):
    #word = input()
    man = []
    for jh in str.lower(word):
        man.append(jh)

    ae = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', " ", '?', ".", "!", ',', '\n', ':', "'", '(', ')']
    letter = ['#', '~', 'd', '(', '&', '%', 'a', '+', 'k', 'ș', '^', '*', 'l', 'z', '/', '@', 'x', ']', '`', 't', 'e', 'ă', 'b', '$', 'n', '>', " ", '?', '.', '!', ',', '\n', ':', "o", 'j', 'y']
    damn = []

    for gh in man:
        dudd = letter.index(gh)
        damn.append(ae[dudd])

    answer = "".join(damn)
    print(answer)
