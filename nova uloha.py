import tkinter
import random
canvas = tkinter.Canvas(width="600", height="400")
canvas.pack()

def mozaika(sirka_platna, vyska_platna):
    x,y = 0,0
    a = random.randrange(1,51)
    while y < vyska_platna + a:
        while x < sirka_platna + a:
            farba = f"#{random.randrange(256):02x}{random.randrange(256):02x}{random.randrange(256):02x}"
            canvas.create_rectangle(x,y,x+a,y+a, fill=farba,outline= farba)
            x += a
        x=0
        y += a

mozaika(600,400)
canvas.mainloop()
