import random
text = "Na základe výskumu vedcov na Univerzite v Cambridgi ľudský mozog zvládne porozumieť písanému textu aj v prípade ak v slovách poprehadzujeme písmená a ponecháme na svojich miestach len prvé a posledné písmeno v každom slove, teda napríklad dokážeme prečítať tento text"
zoznam= text.split()


fero=[]
auto=[]
dno=[]
for slovo in zoznam:
    x=1
    auto=list(slovo)
    pocet=len(slovo)
    if pocet>3:
        for i in range(len(auto)-2):
            f=auto[x]
            fero.append(f)
            x+=1
    random.shuffle(fero)
    zoznam= auto[0]+"".join(fero) +auto[-1]
    fero=[]
    dno.append(zoznam)
text1= " ".join(dno)
print(dno)
print(text1)



