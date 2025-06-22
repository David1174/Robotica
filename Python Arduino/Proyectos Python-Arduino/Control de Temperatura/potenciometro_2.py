import tkinter as tk
import serial
import threading
import time

# Configuración del puerto serial
arduino_port = "COM12"  # Cambia esto al puerto donde esté conectado tu Arduino
baud_rate = 9600

try:
    ser = serial.Serial(arduino_port, baud_rate, timeout=1)
except serial.SerialException as e:
    print(f"No se puede abrir el puerto serial: {e}")
    ser = None

# Variable para detener la comunicación de manera segura
detener_comunicacion = False

# Función para enviar la velocidad al Arduino
def enviar_velocidad(velocidad):
    if ser:
        try:
            ser.write(f"{velocidad}\n".encode())  # Enviar el valor como cadena
            print(f"Velocidad enviada: {velocidad}")
        except serial.SerialException as e:
            print(f"Error al enviar datos al puerto serial: {e}")

# Función que se ejecuta cada vez que se mueve el deslizador
def actualizar_velocidad(value):
    velocidad = int(value)
    enviar_velocidad(velocidad)

# Función que se ejecuta al cerrar la ventana
def cerrar_programa():
    global detener_comunicacion
    detener_comunicacion = True
    ser.close() if ser else None
    root.quit()

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

# Vincular el cierre de la ventana a la función de salida segura
root.protocol("WM_DELETE_WINDOW", cerrar_programa)

# Iniciar el loop de la ventana
root.mainloop()

# Cerrar la conexión serial cuando se cierre la ventana
if ser:
    ser.close()
