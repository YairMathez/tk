from tkinter import *
root = Tk()
root.title('Vale te quiero mucho , no quiero peleear con vos, queiro darte besos y abrazos')
root.geometry('500x500')

l1 = Label(root, text='hola mundo mi primera etiqueta')
l2 = Label(root, text='hola mundo!')
l3 = Label(root, text='')
l1.grid(row=0, column=0)
l2.grid(row=1, column=1)
l3.grid(row=10, column=10)



root.mainloop()