meno = input("Zadaj meno:")

c = len(meno)
for i in range (c):
    print(meno,end=" ")
print(" ")

for i in range (c):
    print(meno)

print("*" * (c + 4))
print(f"* {meno} *")
print("*" * (c + 4))

for i in range (c):
    print(meno[i] * (i+1))


for i in range (c):
    print(" " * (c-1 -i) + meno[i] * (i+1))

for i in range(c):
    print(meno[:i+1])

for i in range(c):
    print(" "*(c-i),meno[:i+1])

print(meno[::-1])