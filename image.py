from tkinter import *
from PIL import ImageTk, Image


root= Tk()
root.tittle('Hola mundo')


# imagen = Image.open('cascada.png')
# imagen.show()


img = ImageTk.PhotoImage(Image.open('fruit-1234657_1280.png'))
l = Label(image=img)
l.pack()

root.mainloop()

