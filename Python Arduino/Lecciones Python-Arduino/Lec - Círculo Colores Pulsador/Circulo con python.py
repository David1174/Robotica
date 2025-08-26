import tkinter as tk
import serial
import threading
import time

# Configurar puerto serie (ajusta el nombre del puerto COM o /dev/ttyUSB0)
arduino = serial.Serial('COM8', 9600, timeout=1)  # En Linux podría ser '/dev/ttyUSB0'

# Conversión cm → píxeles (96 dpi ≈ 37.8 px/cm)
CM_TO_PX = 37.8  
diametro_cm = 10
diametro_px = int(diametro_cm * CM_TO_PX)

# Lista de colores para el círculo
colores = ["lightgreen", "lightblue", "yellow", "orange", "pink"]
indice_color = 0

# Crear ventana
ventana = tk.Tk()
ventana.title("Círculo con Arduino")

canvas = tk.Canvas(ventana, width=diametro_px + 20, height=diametro_px + 20, bg="white")
canvas.pack()

# Dibujar círculo inicial
x0, y0 = 10, 10
x1, y1 = x0 + diametro_px, y0 + diametro_px
circulo = canvas.create_oval(x0, y0, x1, y1, fill=colores[indice_color], outline="black", width=2)

# Función para cambiar color
def cambiar_color():
    global indice_color
    indice_color = (indice_color + 1) % len(colores)
    canvas.itemconfig(circulo, fill=colores[indice_color])

# Hilo para leer datos del Arduino
def leer_serial():
    while True:
        if arduino.in_waiting > 0:
            linea = arduino.readline().decode().strip()
            if linea == "PRESION":
                ventana.after(0, cambiar_color)
        time.sleep(0.1)

# Crear hilo
threading.Thread(target=leer_serial, daemon=True).start()

ventana.mainloop()
