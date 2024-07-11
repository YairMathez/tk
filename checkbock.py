from tkinter import *

root = Tk()
root.title ('Hola mundo: checkbox')
root.geometry('500x500')
var = StringVar()
var.set('Chanchito feliz')

def mostrar():
    l= Label(root, text=var.get())
    l.pack()
    
c = Checkbutton(root, text='Soy un checkbock', variable=var, onvalue= 'si', offvalue='chanchito feliz')
c.pack()

btn = Button(root, text='Click', command=mostrar)
btn.pack()
root.mainloop()