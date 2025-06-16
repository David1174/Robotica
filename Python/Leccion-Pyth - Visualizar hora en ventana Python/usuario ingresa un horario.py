import tkinter as tk
from datetime import datetime
from tkinter import messagebox

# Función para actualizar la hora en la etiqueta y verificar la coincidencia
def actualizar_hora():
    # Obtiene la hora actual del sistema
    hora_actual = datetime.now().strftime("%H:%M")
    # Actualiza el texto de la etiqueta
    etiqueta_hora.config(text=hora_actual)

    # Verifica si la hora actual coincide con la hora ingresada por el usuario
    if hora_actual == entrada_hora.get():
        messagebox.showinfo("Alerta", "¡La hora coincide con la ingresada!")

    # Programa la función para que se ejecute de nuevo en 1000 ms (1 segundo)
    ventana.after(1000, actualizar_hora)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Reloj con Alerta")
ventana.geometry("400x300")

# Etiqueta para mostrar la hora actual
etiqueta_hora = tk.Label(ventana, font=("Arial", 30), fg="blue")
etiqueta_hora.pack(pady=10)

# Etiqueta y entrada de hora
etiqueta_ingresar_hora = tk.Label(ventana, text="Activa motor:")
etiqueta_ingresar_hora.place(x=170, y=120)  # Ubicación específica
entrada_hora = tk.Entry(ventana, font=("Arial", 20), justify="center", width=5)
entrada_hora.place(x=170, y=145)  # Ubicación específica para el campo de entrada

# Inicia la actualización de la hora
actualizar_hora()

# Inicia el bucle de la interfaz gráfica
ventana.mainloop()
