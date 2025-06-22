import tkinter as tk
import serial
import time

# Configurar el puerto serial con Arduino
try:
    arduino = serial.Serial('COM3', 9600)  # Reemplaza 'COM3' con el puerto correcto de tu Arduino
    time.sleep(2)  # Esperar un momento para establecer la conexión
except Exception as e:
    print("No se pudo conectar al Arduino:", e)

# Función para activar/desactivar el LED
led_on = False  # Estado del LED

def toggle_led():
    global led_on
    if arduino.is_open:
        if not led_on:
            arduino.write(b'1')  # Enviar '1' para encender el LED
            led_button.config(text="Apagar LED")
        else:
            arduino.write(b'0')  # Enviar '0' para apagar el LED
            led_button.config(text="Encender LED")
        led_on = not led_on  # Cambia el estado del LED

# Crear la ventana principal
window = tk.Tk()
window.title("Control de LED con Arduino")
window.geometry("300x300")

# Crear el botón y ubicarlo con coordenadas específicas
led_button = tk.Button(window, text="Encender LED", command=toggle_led)
led_button.place(x=50, y=100)  # Coordenadas del botón en la ventana (ajusta según prefieras)

# Ejecutar el bucle de la interfaz
window.mainloop()

# Cerrar el puerto serial al salir
if arduino.is_open:
    arduino.close()
