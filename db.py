from math import e
from tkinter import Frame, Tk, Label, Entry, Button, Checkbutton, END
import sqlite3

# Crear la ventana principal
root = Tk()
root.title('Hola mundo: todo list')
root.geometry('500x500')

# Conectar a la base de datos
conn = sqlite3.connect('todo.db')
c = conn.cursor()

# Crear la tabla si no existe
c.execute("""
    CREATE TABLE if not exists todo(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL
    );
""")
conn.commit()

# Función para eliminar una tarea


def remove(id):
    def _remove():
        c.execute("DELETE FROM todo WHERE id = ?", (id,))
        conn.commit()
        render_todos()
    return _remove

# Función para completar una tarea


def complete(id):
    def _complete():
        todo = c.execute("SELECT * FROM todo WHERE id = ?", (id,)).fetchone()
        c.execute("UPDATE todo SET completed = ? WHERE id = ?",
                (not todo[3], id))
        conn.commit()
        render_todos()
    return _complete


# Crear un marco dentro de la ventana principal
frame = Frame(root)
frame.grid(row=1, column=0, columnspan=3, sticky='nswe', padx=5)

# Función para renderizar las tareas


def render_todos():
    for widget in frame.winfo_children():
        widget.destroy()

    rows = c.execute("SELECT * FROM todo").fetchall()
    for i, row in enumerate(rows):
        id, created_at, description, completed = row
        check = Checkbutton(frame, text=description, width=42,
                            anchor='w', command=complete(id))
        check.grid(row=i, column=0, sticky='w')
        check.select() if completed else check.deselect()
        btn = Button(frame, text="Eliminar", command=remove(id))
        btn.grid(row=i, column=1)

# Función para agregar una tarea


def add_todo():
    todo = e.get()
    if todo:
        c.execute(
            "INSERT INTO todo (description, completed) VALUES (?, ?)", (todo, False))
        conn.commit()
        e.delete(0, END)
        render_todos()


# Elementos de la interfaz
l = Label(root, text='Tarea')
l.grid(row=0, column=0)

e = Entry(root, width=40)
e.grid(row=0, column=1)

btn = Button(root, text='Agregar', padx=5, pady=5, command=add_todo)
btn.grid(row=0, column=2)

e.focus()

root.bind('<Return>', lambda event: add_todo())

render_todos()

root.mainloop()
