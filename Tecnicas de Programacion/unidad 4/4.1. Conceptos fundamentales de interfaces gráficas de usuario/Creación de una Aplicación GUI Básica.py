import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar


class Aplicacion:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestor de Información")

        # Etiqueta
        self.label = tk.Label(master, text="Ingrese información:")
        self.label.pack(pady=10)

        # Campo de texto
        self.entry = tk.Entry(master, width=40)
        self.entry.pack(pady=5)

        # Botón Agregar
        self.btn_agregar = tk.Button(master, text="Agregar", command=self.agregar)
        self.btn_agregar.pack(pady=5)

        # Lista para mostrar datos
        self.lista = Listbox(master, width=50, height=10)
        self.lista.pack(pady=10)

        # Barra de desplazamiento
        self.scrollbar = Scrollbar(master)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Asociar la barra de desplazamiento a la lista
        self.lista.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.lista.yview)

        # Asegurar que la lista use la barra de desplazamiento
        self.lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Botón Limpiar
        self.btn_limpiar = tk.Button(master, text="Limpiar", command=self.limpiar)
        self.btn_limpiar.pack(pady=5)

    def agregar(self):
        # Obtener el texto del campo de entrada
        texto = self.entry.get()
        if texto:
            self.lista.insert(tk.END, texto)
            self.entry.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese información.")

    def limpiar(self):
        # Limpiar la lista y el campo de entrada
        self.entry.delete(0, tk.END)
        self.lista.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
