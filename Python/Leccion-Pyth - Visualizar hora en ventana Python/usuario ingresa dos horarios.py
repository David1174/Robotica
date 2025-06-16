import tkinter as tk
from datetime import datetime
from tkinter import messagebox

# Función para actualizar la hora en la etiqueta y verificar la coincidencia
def actualizar_hora():
    # Obtiene la hora actual del sistema en formato HH:MM
    hora_actual = datetime.now().strftime("%H:%M")
    # Actualiza el texto de la etiqueta con la hora actual
    etiqueta_hora.config(text=hora_actual)

    # Verifica si la hora actual coincide con cualquiera de las horas ingresadas
    if hora_actual == entrada_hora1.get():
        messagebox.showinfo("Alerta", "¡La hora coincide con la hora ingresada en el primer campo!")
        
    if hora_actual == entrada_hora2.get():
        messagebox.showinfo("Alerta", "¡La hora coincide con la hora ingresada en el segundo campo!")

    # Programa la función para que se ejecute de nuevo en 1000 ms (1 segundo)
    ventana.after(1000, actualizar_hora)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Reloj con Dos Alertas")
ventana.geometry("400x300")

# Etiqueta para mostrar la hora actual
etiqueta_hora = tk.Label(ventana, font=("Arial", 30), fg="blue")
etiqueta_hora.pack(pady=10)

# Etiqueta y primer campo de entrada de hora
etiqueta_ingresar_hora1 = tk.Label(ventana, text="Ingrese primera hora (HH:MM):")
etiqueta_ingresar_hora1.place(x=20, y=150)  # Ubicación específica
entrada_hora1 = tk.Entry(ventana, font=("Arial", 20), justify="center", width=5)
entrada_hora1.place(x=250, y=145)  # Ubicación específica para el primer campo de entrada

# Etiqueta y segundo campo de entrada de hora
etiqueta_ingresar_hora2 = tk.Label(ventana, text="Ingrese segunda hora (HH:MM):")
etiqueta_ingresar_hora2.place(x=20, y=200)  # Ubicación específica
entrada_hora2 = tk.Entry(ventana, font=("Arial", 20), justify="center", width=5)
entrada_hora2.place(x=250, y=195)  # Ubicación específica para el segundo campo de entrada

# Inicia la actualización de la hora
actualizar_hora()

# Inicia el bucle de la interfaz gráfica
ventana.mainloop()
