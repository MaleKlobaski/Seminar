samohlasky = "aáeéiíoóôuúyý"
riekanka = "sedí mucha na stene sedí a spí"
print(riekanka)
def zmena(text,samohlaska):
    for znak in samohlasky:
        text = text.replace(znak,samohlaska)
    print(text)

zmena(riekanka,"b")