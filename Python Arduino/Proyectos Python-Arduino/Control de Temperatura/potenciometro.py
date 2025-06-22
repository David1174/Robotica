import tkinter as tk
import serial
import time

# Configuración del puerto serial
arduino_port = "COM12"  # Cambia esto al puerto donde esté conectado tu Arduino
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

# Función para enviar la velocidad al Arduino
def enviar_velocidad(velocidad):
    ser.write(f"{velocidad}\n".encode())  # Enviar el valor como cadena y codificar a bytes
    print(f"Velocidad enviada: {velocidad}")  # Mostrar la velocidad enviada

# Función que se ejecuta cada vez que se mueve el deslizador
def actualizar_velocidad(value):
    velocidad = int(value)  # Convertir el valor del deslizador a entero
    enviar_velocidad(velocidad)

# Crear la ventana principal
root = tk.Tk()
root.title("Control de Velocidad del Motor")

# Tamaño de la ventana
root.geometry("300x200")

# Etiqueta para el deslizador
etiqueta = tk.Label(root, text="Velocidad del motor", font=("Helvetica", 12))
etiqueta.pack(pady=10)

# Deslizador para ajustar la velocidad (de 0 a 255)
deslizador = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, command=actualizar_velocidad, length=250)
deslizador.pack(pady=20)

# Iniciar el loop de la ventana
root.mainloop()

# Cerrar la conexión serial cuando se cierre la ventana
ser.close()
