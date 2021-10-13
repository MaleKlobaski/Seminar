import random

def nazov(n):
    samohlasky = "aäeiyou"
    spoluhlasky = "qwrtzpsdfghjklxcvbnm"
    sam = random.choice(samohlasky)
    meno = sam.upper() + random.choice(spoluhlasky)*n + sam
    return meno

def ulozenie():
    n = int(input("Zadaj počet samohlások: "))
    s = int(input("Zadaj pocet skupín: "))
    for i in range(s):
        subor = open("Rass.txt", "a", encoding="UTF-8")
        subor.write(nazov(n)+"\n")
        subor.close()
    subor = open("Rass.txt", "r", encoding="UTF-8")
    text = subor.read()
    pocet_skupin = text.split()
    print("Zoznam skupín:",pocet_skupin)
    print("Pocet skupín v súbore: ",len(pocet_skupin))
    subor.close()
    g = int(input("Pocet skupin na generáciu: "))
    for i in range(g):
        print(random.choice(pocet_skupin))
        subor = open("Rass.txt", "a", encoding="UTF-8")
        subor.write(random.choice(pocet_skupin) + "\n")
        subor.close()
    subor = open("Rass.txt", "r", encoding="UTF-8")
    text = subor.read()
    pocet_skupin = text.split()
    print("Pocet skupín po generovani: ", len(pocet_skupin))
ulozenie()
