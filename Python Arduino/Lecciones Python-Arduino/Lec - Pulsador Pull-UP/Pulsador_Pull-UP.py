import tkinter as tk
from tkinter import Canvas
import serial
import threading

# Configuración del puerto serial (ajusta el puerto según tu sistema)
arduino = serial.Serial('COM7', 9600)  # En Windows
# arduino = serial.Serial('/dev/ttyACM0', 9600)  # En Linux

def leer_datos():
    """Función que lee datos del Arduino y actualiza la luz."""
    while True:
        try:
            data = arduino.readline().decode().strip()  # Lee y limpia la línea
            if data == "ON":
                encender_luz()
            elif data == "OFF":
                apagar_luz()
        except:
            break

def encender_luz():
    """Cambia el color de la luz a amarillo."""
    canvas.itemconfig(luz, fill='yellow')

def apagar_luz():
    """Apaga la luz (color gris)."""
    canvas.itemconfig(luz, fill='gray')

# Configuración de la ventana Tkinter
root = tk.Tk()
root.title("Control de Luz con Arduino")

canvas = Canvas(root, width=200, height=200)
canvas.pack()

# Dibujar un círculo que representa la luz
luz = canvas.create_oval(50, 50, 150, 150, fill='gray')

# Iniciar el hilo para leer datos del Arduino
hilo = threading.Thread(target=leer_datos)
hilo.daemon = True  # El hilo se cerrará al salir del programa
hilo.start()

# Iniciar el bucle principal de Tkinter
root.mainloop()
