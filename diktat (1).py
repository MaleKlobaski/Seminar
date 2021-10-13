import re

text = "Kobyla býva v modernom obydlí. Sestra je veľmi bystrá."

pocet_slov = len(text.split())
i = text.lower().count("i")+text.lower().count("í")
y = text.lower().count("y")+text.lower().count("ý")
obtiaznost = (i+y)/pocet_slov*100

print("pocet slov : ",pocet_slov,",i/í:",i,",y/ý:",y ,"obtiažnosť:",int(obtiaznost),"%")
print(re.sub("[iíIÍyýYÝ]","_",text))
