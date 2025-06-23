import tkinter as tk
import serial
import time
import mysql.connector  # Nueva librería para base de datos

# Crear la ventana principal primero
root = tk.Tk()
root.title("Datos de Temperatura y Humedad")
root.geometry("400x500")

etiqueta_temperatura = tk.Label(root, text="Temperatura: --°C", font=("Helvetica", 10))
etiqueta_temperatura.place(x=50, y=30)

etiqueta_humedad = tk.Label(root, text="Humedad: --%", font=("Helvetica", 10))
etiqueta_humedad.place(x=50, y=70)

etiqueta_error = tk.Label(root, text="", font=("Helvetica", 10), fg="red")
etiqueta_error.place(x=50, y=110)

# Intentar conectar a la base de datos y al puerto serial
conexion = None
cursor = None
ser = None

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",         # Reemplaza con tu usuario MySQL
        password="admin",  # Reemplaza con tu contraseña MySQL
        database="meteorologia"
    )
    cursor = conexion.cursor()
except Exception as e:
    etiqueta_error.config(text=f"Error DB: {e}")

try:
    arduino_port = "COM12"
    baud_rate = 9600
    ser = serial.Serial(arduino_port, baud_rate, timeout=1)
except Exception as e:
    etiqueta_error.config(text=f"Error Serial: {e}")

# Función para actualizar la temperatura y humedad
def actualizar_datos():
    try:
        if ser is not None:
            linea = ser.readline().decode('utf-8').strip()
            if "Temp:" in linea and "Hum:" in linea:
                partes = linea.split(" ")
                temp = float(partes[1])
                hum = float(partes[3])
                etiqueta_temperatura.config(text=f"Temperatura: {temp}°C")
                etiqueta_humedad.config(text=f"Humedad:     {hum}%")
                if cursor is not None and conexion is not None:
                    cursor.execute("INSERT INTO datos (humedad, temperatura) VALUES (%s, %s)", (hum, temp))
                    conexion.commit()
    except Exception as e:
        etiqueta_error.config(text=f"Error: {e}")
    root.after(1000, actualizar_datos)

actualizar_datos()
root.mainloop()

# Cerrar la conexión al cerrar la app (opcional, si root.mainloop termina)
if cursor is not None:
    cursor.close()
if conexion is not None:
    conexion.close()
