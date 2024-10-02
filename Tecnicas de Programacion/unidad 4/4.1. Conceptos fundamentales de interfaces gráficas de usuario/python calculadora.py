import tkinter as tk

def agregar_caracter(caracter):
    entrada.insert(tk.END, caracter)

def calcular(*args):
    try:
        expresion = entrada.get().strip()
        resultado = eval(expresion)  # Cuidado: eval puede ser peligroso si no se controla la entrada
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
        log.config(text=f"Operación: {expresion}, Resultado: {resultado}")
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")
        log.config(text="Error")

def limpiar():
    entrada.delete(0, tk.END)
    log.config(text="Limpiar")

def salir():
    ventana.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x500")

# Centrar la ventana en la pantalla
ancho_ventana = 400
alto_ventana = 500
posicion_derecha = int(ventana.winfo_screenwidth() / 2 - ancho_ventana / 2)
posicion_abajo = int(ventana.winfo_screenheight() / 2 - alto_ventana / 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_derecha}+{posicion_abajo}")

# Crear un menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Limpiar", command=limpiar)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

# Crear un campo de entrada
entrada = tk.Entry(ventana, font=("Arial", 16), justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entrada.bind("<Return>", calcular)
entrada.bind("<Escape>", lambda event: limpiar())

# Crear un label para visualizar las operaciones en formato de log
log = tk.Label(ventana, text="Crea un label", font=("Arial", 12))
log.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

# Crear los botones de los números
numeros = "789456123"
for i, num in enumerate(numeros):
    tk.Button(ventana, text=num, font=("Arial", 14),
              command=lambda numero=num: agregar_caracter(numero)).grid(row=(i//3)+2, column=(i%3), padx=8, pady=8)

# Botón para el cero
tk.Button(ventana, text="0", font=("Arial", 14),
          command=lambda: agregar_caracter("0")).grid(row=5, column=1, padx=8, pady=8)

# Botón para el punto decimal
tk.Button(ventana, text=".", font=("Arial", 14), command=lambda: agregar_caracter(".")).grid(row=5, column=0, padx=8, pady=8)

# Botón para el cálculo
tk.Button(ventana, text="Calcular", font=("Arial", 14), command=calcular).grid(row=5, column=2, columnspan=2, padx=8, pady=8)

# Crear los botones de las operaciones
operadores = ["+", "-", "*", "/"]
for i, operador in enumerate(operadores):
    tk.Button(ventana, text=operador, font=("Arial", 16),
              command=lambda op=operador: agregar_caracter(op)).grid(row=(i+2), column=3, padx=8, pady=8)

# Ejecutar el bucle de eventos
ventana.mainloop()

