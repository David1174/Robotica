import tkinter as tk
import serial
import time

# Configurar la conexión serial (ajusta el puerto según sea necesario)
arduino = serial.Serial('COM7', 9600, timeout=1)
time.sleep(2)  # Dar tiempo al Arduino para inicializar

# Función para encender el LED
def encender_led():
    arduino.write(b'1')
    print("LED encendido")

# Función para apagar el LED
def apagar_led():
    arduino.write(b'0')
    print("LED apagado")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Control de LED con Arduino")

# Ajustar el tamaño de la ventana
ventana.geometry("300x200")  # Aumentar el tamaño de la ventana

# Crear el botón para encender el LED (del mismo tamaño que el de apagar)
boton_encender = tk.Button(ventana, text="Encender LED", command=encender_led, width=15, height=2)
boton_encender.pack(pady=10)

# Crear el botón para apagar el LED (del mismo tamaño que el de encender)
boton_apagar = tk.Button(ventana, text="Apagar LED", command=apagar_led, width=15, height=2)
boton_apagar.pack(pady=10)

# Iniciar el loop de la interfaz gráfica
ventana.mainloop()

# Cerrar el puerto serie al cerrar la ventana
arduino.close()