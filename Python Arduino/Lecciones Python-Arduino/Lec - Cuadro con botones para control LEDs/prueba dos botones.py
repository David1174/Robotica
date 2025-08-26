import tkinter as tk
import serial
import time

# Configurar el puerto serial con Arduino
try:
    arduino = serial.Serial('COM7', 9600)  # Cambia 'COM3' por el puerto correcto de tu Arduino
    time.sleep(2)  # Esperar un momento para establecer la conexión
except Exception as e:
    print("No se pudo conectar al Arduino:", e)

# Funciones para activar/desactivar cada LED
led1_on = False
led2_on = False

#****************************************
def toggle_led1():
    global led1_on
    if arduino.is_open:
        if not led1_on:
            arduino.write(b'1')  # Enviar '1' para encender el LED 1
            button_led1.config(text="Apagar LED 1")
        else:
            arduino.write(b'0')  # Enviar '0' para apagar el LED 1
            button_led1.config(text="Encender LED 1")
        led1_on = not led1_on

def toggle_led2():
    global led2_on
    if arduino.is_open:
        if not led2_on:
            arduino.write(b'2')  # Enviar '2' para encender el LED 2
            button_led2.config(text="Apagar LED 2")
        else:
            arduino.write(b'3')  # Enviar '3' para apagar el LED 2
            button_led2.config(text="Encender LED 2")
        led2_on = not led2_on

# Crear la ventana principal
window = tk.Tk()
window.title("Control de LEDs con Arduino")
window.geometry("400x300")


#****************************************************
# Crear los botones para controlar los LEDs y ubicarlos en coordenadas específicas
button_led1 = tk.Button(window, text="Encender LED 1", command=toggle_led1)
button_led1.place(x=50, y=50)  # Coordenadas del botón 1 (ajústalas según prefieras)


button_led2 = tk.Button(window, text="Encender LED 2", command=toggle_led2)
button_led2.place(x=50, y=100)  # Coordenadas del botón 2 (ajústalas según prefieras)

# Ejecutar el bucle de la interfaz
window.mainloop()

# Cerrar el puerto serial al salir
if arduino.is_open:
    arduino.close()
