import tkinter as tk
from tkinter import messagebox, Listbox, END

class ListaDeTareas:
    def __init__(self, master):
        self.master = master
        self.master.title("Lista de Tareas")
        self.master.geometry("400x400")

        # Campo de entrada
        self.entry = tk.Entry(master, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.anadir_tarea)

        # Botones
        self.btn_anadir = tk.Button(master, text="Añadir Tarea", command=self.anadir_tarea)
        self.btn_anadir.pack(pady=5)

        self.btn_completar = tk.Button(master, text="Marcar como Completada", command=self.marcar_completada)
        self.btn_completar.pack(pady=5)

        self.btn_eliminar = tk.Button(master, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.pack(pady=5)

        # Lista de tareas
        self.lista_tareas = Listbox(master, width=50, height=15)
        self.lista_tareas.pack(pady=10)

    def anadir_tarea(self, event=None):
        tarea = self.entry.get()
        if tarea:
            self.lista_tareas.insert(END, tarea)
            self.entry.delete(0, END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    def marcar_completada(self):
        try:
            seleccion = self.lista_tareas.curselection()[0]
            tarea = self.lista_tareas.get(seleccion)
            self.lista_tareas.delete(seleccion)
            self.lista_tareas.insert(seleccion, f"{tarea} - Completada")
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

    def eliminar_tarea(self):
        try:
            seleccion = self.lista_tareas.curselection()[0]
            self.lista_tareas.delete(seleccion)
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaDeTareas(root)
    root.mainloop()
