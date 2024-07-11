from tkinter import *

root = Tk()
root.title('Hopla mundo ')
root.geometry('500x500')

e = Entry(root, width=40)
e.pack()
e.insert(0, "Ingresa Texto")

def click():
    texto = e.get()
    textvariable.set(texto)
    valor = textvariable.get()
    print(valor)
    #l.configure(text=texto)
    #l.pack()
    e.delete(0, END)   

btn = Button(root, text='click', command=click)
btn.pack()

textvariable = StringVar()
l = Label(root, textvariable=textvariable)
#l.pack()


root.mainloop()
