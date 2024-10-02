import tkinter as tk
from tkinter import messagebox

class TareaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Tareas")
        self.master.geometry("400x400")  # Tamaño de la ventana

        # Campo de entrada para añadir tareas
        self.entry = tk.Entry(master, font=("Arial", 14))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.agregar_tarea)  # Atajo para añadir tarea con Enter
        self.entry.bind("<Escape>", lambda event: master.quit())  # Cerrar aplicación con Escape

        # Botones
        self.boton_agregar = tk.Button(master, text="Añadir Tarea", command=self.agregar_tarea)
        self.boton_agregar.pack(pady=5)

        self.boton_completar = tk.Button(master, text="Marcar como Completada", command=self.marcar_completada)
        self.boton_completar.pack(pady=5)

        self.boton_eliminar = tk.Button(master, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=5)

        # Lista de tareas
        self.lista_tareas = tk.Listbox(master, font=("Arial", 14), selectmode=tk.SINGLE)
        self.lista_tareas.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Atajos de teclado para las tareas
        self.master.bind("<C>", lambda event: self.marcar_completada())  # Atajo para completar
        self.master.bind("<Delete>", lambda event: self.eliminar_tarea())  # Atajo para eliminar
        self.master.bind("<D>", lambda event: self.eliminar_tarea())  # Atajo para eliminar con D

    def agregar_tarea(self, event=None):
        tarea = self.entry.get()
        if tarea:
            self.lista_tareas.insert(tk.END, tarea)
            self.entry.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            tarea = self.lista_tareas.get(seleccion)
            self.lista_tareas.delete(seleccion)
            self.lista_tareas.insert(seleccion, tarea + " (Completada)")  # Marcamos como completada
            self.lista_tareas.itemconfig(seleccion, {'fg': 'gray'})  # Cambia el color del texto
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            self.lista_tareas.delete(seleccion)
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TareaApp(root)
    root.mainloop()

