import serial
import time
import tkinter as tk
from tkinter import messagebox

# Configuración del puerto serial
arduino_port = 'COM8'  # Ajusta según el puerto de tu Arduino
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Espera para establecer la conexión con el Arduino

# Función para iniciar el juego de luces
def start_light_game():
    ser.write(b'1')  # Envía 'S' para iniciar el juego de luces
    print("Juego de luces iniciado.")
   # messagebox.showinfo("Estado", "Juego de luces iniciado.")

# Función para detener el juego de luces
def stop_light_game():
    ser.write(b'0')  # Envía 'P' para detener el juego de luces
    print("Juego de luces detenido.")
   # messagebox.showinfo("Estado", "Juego de luces detenido.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Control del Juego de Luces")
root.geometry("300x150")

# Crear botones para iniciar y detener el juego de luces
start_button = tk.Button(root, text="Iniciar Juego de Luces", command=start_light_game, width=25, height=2, bg="green", fg="white")
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Detener Juego de Luces", command=stop_light_game, width=25, height=2, bg="red", fg="white")
stop_button.pack(pady=10)

# Ejecuta la interfaz gráfica
root.mainloop()

# Cierra la conexión serial al cerrar la ventana
ser.close()
