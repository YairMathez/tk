from tkinter import *

from tkinter import messagebox

root=Tk()
root.title('Hola mundo')

#def click():
    #messagebox.showwarning('Popup', 'Hola mundo')
    

#def click():
    #messagebox.showinfo('Popup', 'Hola mundo')
    

#def click():
    #messagebox.showerror('Popup', 'Hola mundo :(')


# def click():
#     respuesta= messagebox.askquestion('Popup', 'Hola mundo')
#     if respuesta == 'yes':
#         messagebox.showinfo('Respuesta', 'la respuesta fue ' + respuesta)
#     else:
#         messagebox.showinfo('Respuesta', 'la respuesta fue'+ respuesta)
        
# def click():
#     respuesta = messagebox.askokcancel('Hola mundo', 'Desea realizar la accion')
#     if respuesta:
#         messagebox.showinfo('Hola mundo', 'La respuesta fue ok')
#     else:
#         messagebox.showinfo('Hola mundo', 'La respuesta fue cancelada')
        

def click():
    respuesta = messagebox.askokcancel('Hola mundo', 'Desea realizar la accion')
    print(respuesta)
    if respuesta:
        messagebox.askyesno('Hola mundo', 'La respuesta fue ok')
    else:
        messagebox.askyesno('Hola mundo', 'La respuesta fue cancelada')

btn = Button(root,text='PRESIONAME', command=click)
btn.pack()

root.mainloop()