from tkinter import *

root = Tk()
root.title('Hola mundo')

l = Label(root, text='Hola mundo')
def click():
    l.pack()
    
btn = Button(root, text="Clickeame", command=click, fg='red', bg='white')
btn.pack()
root.mainloop()
