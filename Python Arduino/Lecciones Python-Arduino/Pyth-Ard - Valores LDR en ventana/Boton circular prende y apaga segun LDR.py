import tkinter as tk
from tkinter import Canvas
import serial

# Configuración del puerto serie
try:
    arduino = serial.Serial('COM12', 9600, timeout=0.01)  # Cambia 'COM3' por tu puerto Arduino
except Exception as e:
    print(f"Error al conectar con Arduino: {e}")
    arduino = None

# Configuración de la ventana gráfica
ventana = tk.Tk()
ventana.title("Botón Circular - Sensor LDR")
ventana.geometry("400x400")
ventana.resizable(False, False)

# Canvas para el botón circular
canvas = Canvas(ventana, width=400, height=400, bg="white")
canvas.pack()

# Crear el círculo (botón) con color inicial verde claro
x0, y0, x1, y1 = 150, 150, 250, 250
boton_id = canvas.create_oval(x0, y0, x1, y1, fill="#90EE90")  # Verde claro (#90EE90)

# Variables para parpadeo
parpadeo_activo = False

# Actualizar el estado del botón según el valor del sensor
def actualizar_estado():
    global parpadeo_activo
    if arduino and arduino.in_waiting > 0:
        try:
            linea = arduino.readline().decode('utf-8').strip()
            if linea.isdigit():
                valor_ldr = int(linea)
                if valor_ldr > 800:
                    parpadeo_activo = True
                else:
                    parpadeo_activo = False
                    canvas.itemconfig(boton_id, fill="#90EE90")  # Verde claro
        except Exception as e:
            print(f"Error al leer datos: {e}")
    ventana.after(10, actualizar_estado)

# Manejar el parpadeo del botón
def parpadear():
    if parpadeo_activo:
        color_actual = canvas.itemcget(boton_id, "fill")
        nuevo_color = "red" if color_actual == "#90EE90" else "#90EE90"
        canvas.itemconfig(boton_id, fill=nuevo_color)
    ventana.after(500, parpadear)

# Iniciar las actualizaciones
actualizar_estado()
parpadear()

# Ejecutar la ventana
ventana.mainloop()

# Cerrar el puerto serie al salir
if arduino:
    arduino.close()
