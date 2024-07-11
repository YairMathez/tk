from tkinter import *

root = Tk()

root.title('Hola mundo')

r= IntVar()
r.set('2')

CHANCHITOS = [
    ('Feliz', 'Feliz'),
    ('Triste', ' Triste'),
    ('Amargado', 'Amargado')
]


chanchito = StringVar()
chanchito = set('Amargado')

for text, chancho in CHANCHITOS:
    Radiobutton(root, text=text, variable=chanchito, value=chancho).pack()


l = Label(root, textvariable=chanchito)
l.pack()

root.mainloop()