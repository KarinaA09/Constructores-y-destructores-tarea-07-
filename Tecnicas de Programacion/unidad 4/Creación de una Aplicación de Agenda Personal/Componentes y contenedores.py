import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Asegúrate de haber instalado tkcalendar

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Frame para la lista de eventos
        self.frame_lista = ttk.Frame(self.root)
        self.frame_lista.pack(pady=10)

        # Treeview para mostrar eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para entrada de datos
        self.frame_entrada = ttk.Frame(self.root)
        self.frame_entrada.pack(pady=10)

        # Campos de entrada
        self.label_fecha = ttk.Label(self.frame_entrada, text="Fecha:")
        self.label_fecha.grid(row=0, column=0)
        self.entry_fecha = DateEntry(self.frame_entrada)
        self.entry_fecha.grid(row=0, column=1)

        self.label_hora = ttk.Label(self.frame_entrada, text="Hora:")
        self.label_hora.grid(row=1, column=0)
        self.entry_hora = ttk.Entry(self.frame_entrada)
        self.entry_hora.grid(row=1, column=1)

        self.label_desc = ttk.Label(self.frame_entrada, text="Descripción:")
        self.label_desc.grid(row=2, column=0)
        self.entry_desc = ttk.Entry(self.frame_entrada)
        self.entry_desc.grid(row=2, column=1)

        # Botones
        self.boton_agregar = ttk.Button(self.root, text="Agregar Evento", command=self.agregar_evento)
        self.boton_agregar.pack(pady=5)

        self.boton_eliminar = ttk.Button(self.root, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.boton_eliminar.pack(pady=5)

        self.boton_salir = ttk.Button(self.root, text="Salir", command=self.root.quit)
        self.boton_salir.pack(pady=5)

    def agregar_evento(self):
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_desc.get()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")
            return

        self.tree.insert("", "end", values=(fecha, hora, descripcion))
        self.entry_fecha.set_date("")  # Limpiar el DateEntry
        self.entry_hora.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)

    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")
            return

        confirm = messagebox.askyesno("Confirmación", "¿Está seguro de que desea eliminar el evento seleccionado?")
        if confirm:
            for item in selected_item:
                self.tree.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()


