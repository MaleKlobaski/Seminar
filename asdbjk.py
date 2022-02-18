import random
text = "ferdinand"
list=list(text)
pocet = len(list)
x=random.randint(1,pocet-1)
y=random.randint(1,pocet-1)
print(x)
list[x], list[y]=list[y],list[x]
print(list)
