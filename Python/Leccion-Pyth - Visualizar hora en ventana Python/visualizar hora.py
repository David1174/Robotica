import tkinter as tk
import time

# Crear la ventana principal
root = tk.Tk()
root.title("Hora del Sistema")
root.geometry("400x200")  # Tamaño de la ventana

# Función para actualizar la hora
def actualizar_hora():
    hora_actual = time.strftime("%H:%M:%S")  # Formato de hora (HH:MM:SS)
    label_hora.config(text=hora_actual)
    root.after(1000, actualizar_hora)  # Llamada recursiva cada segundo

# Crear un Label para mostrar la hora y colocarlo en coordenadas específicas
label_hora = tk.Label(root, font=("Arial", 24), fg="blue")
label_hora.place(x=50, y=80)  # Ubicar el Label en coordenadas (x=150, y=80)

# Iniciar la actualización de la hora
actualizar_hora()

# Ejecutar el bucle principal
root.mainloop()
