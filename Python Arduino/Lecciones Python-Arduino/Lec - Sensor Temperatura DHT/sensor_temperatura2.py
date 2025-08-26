import tkinter as tk
import serial
import time

# Configuración del puerto serial (ajusta el puerto y la velocidad)
arduino_port = "COM12"  # Cambia esto al puerto que esté usando tu Arduino
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

# Función para actualizar la temperatura y humedad
def actualizar_datos():
    try:
        # Leer línea desde Arduino
        linea = ser.readline().decode('utf-8').strip()

        if "Temp:" in linea and "Hum:" in linea:
            # Separar los datos de temperatura y humedad
            partes = linea.split(" ")
            temp = partes[1]
            hum = partes[3]
            
            # Actualizar los campos de la ventana
            etiqueta_temperatura.config(text=f"Temperatura: {temp}°C")
            etiqueta_humedad.config(text=f"Humedad:     {hum}%")

    except Exception as e:
        print(f"Error al leer del puerto serial: {e}")

    # Llamar a esta función de nuevo después de 1000 ms (1 segundo)
    root.after(1000, actualizar_datos)

# Crear la ventana principal
root = tk.Tk()
root.title("Datos de Temperatura y Humedad")

# Tamaño de la ventana
root.geometry("400x500")

# Etiqueta para la temperatura
etiqueta_temperatura = tk.Label(root, text="Temperatura: --°C", font=("Helvetica", 10))
etiqueta_temperatura.place(x=50, y=30)  # Posicionar la etiqueta en la ventana

# Etiqueta para la humedad
etiqueta_humedad = tk.Label(root, text="Humedad: --%", font=("Helvetica", 10))
etiqueta_humedad.place(x=50, y=70)  # Posicionar la etiqueta en la ventana

# Llamar a la función para actualizar los datos por primera vez
actualizar_datos()

# Iniciar el loop de la ventana
root.mainloop()
