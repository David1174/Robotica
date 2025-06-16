import tkinter as tk
from tkinter import Toplevel

# Función para abrir una nueva ventana
def abrir_ventana():
    nueva_ventana = Toplevel(root)  # Crear una ventana secundaria
    nueva_ventana.title("Ventana Secundaria")
    nueva_ventana.geometry("300x200")

    etiqueta = tk.Label(nueva_ventana, text="¡Hola desde la nueva ventana!")
    etiqueta.pack(pady=20)

    boton_cerrar = tk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy)
    boton_cerrar.pack(pady=10)

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana Principal")
root.geometry("400x300")

# Botón para abrir la nueva ventana
boton_abrir = tk.Button(root, text="Abrir Ventana", command=abrir_ventana)
boton_abrir.place(x=170, y=200) #ubica el boton en la coordenada deseada

root.mainloop()
