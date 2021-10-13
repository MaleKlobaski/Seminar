import random
slova = ['slnko', 'vietor', 'oblak', 'sneh', 'voda', 'rieka']
rslovo = random.choice(slova)
pslovo = int(len(rslovo))
vslovo = rslovo[0] + (pslovo - 2) * "." + rslovo[pslovo - 1]
print("Hádaj slovo: " + vslovo)

slovo = list(rslovo)
uslovo = list(vslovo)
pokus = 0
while pokus < 11 and slovo != uslovo:
    d = input("Zadaj písmeno:")
    if d in slovo:
        e = slovo.index(d)
        uslovo[e] = d
    else:
        pokus += 1
    for i in range(pslovo):
        print(uslovo[i], end = "")
    print()

if slovo == uslovo:
    print("uhádol si! počet nesprávnych pokusov:", pokus)
else:
    print("Prehral si")
