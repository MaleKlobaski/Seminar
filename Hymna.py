def rozsekaj(text, sirka):
    i = 0
    while i <= len(text):
        i += sirka
        text = text[:i] + "\n" + text[i:]
        i += 1
    return text

c = int(input("šírka riadku:"))
hymna = "Nad Tatrou sa blýska, hromy divo bijú."

print(rozsekaj(hymna,c))