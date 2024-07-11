from tkinter import *

root = Tk()
root.title('hola mundo  : Option menu')
root.geometry('600x600')


def enviar():
    l = Label(root,text=value.get())
    l.pack()

lista = [
    'Chanchitos feliz', 
    'Chanchito triste',  
    'Chanchito emocionado',
]
value = StringVar()
value.set(lista[2])


drop = OptionMenu(root, value, *lista)
drop.pack()

btn = Button(root, text='Enviar', command=enviar)
btn.pack()
root.mainloop()
