from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('Hola mundo')

#Solucion 1
# def open():
#     img = ImageTk.PhotoImage(Image.open('cascada.png.webp'))
#     top = Toplevel()
#     top.title('hola mundo nueva ventana')
#     l = Label(top, text='Soy un texto en una nueva ventana')
#     l2 = Label(top, image=img)
#     l.pack()
#     l2.pack()
#     top.mainloop()

#Solucion 2
# def open():
#     global img
#     img = ImageTk.PhotoImage(Image.open('cascada.png.webp'))
#     top = Toplevel()
#     top.title('hola mundo nueva ventana')
#     l = Label(top, text='Soy un texto en una nueva ventana')
#     l2 = Label(top, image=img)
#     l.pack()
#     l2.pack()
#     top.mainloop()




#Solucion 3 

def open(img):
    img = ImageTk.PhotoImage(Image.open('cascada.png.webp'))
    top = Toplevel()
    top.title('hola mundo nueva ventana')
    l = Label(top, text='Soy un texto en una nueva ventana')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()
    top.mainloop()


img = ImageTk.PhotoImage(Image.open('cascada.png.webp'))
btn = Button(root, text='Click', command=lambda: open(img)).pack()
root.mainloop()
