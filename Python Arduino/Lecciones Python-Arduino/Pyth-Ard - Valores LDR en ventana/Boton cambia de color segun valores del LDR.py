import tkinter as tk
import serial

# Configuración del puerto serie
try:
    arduino = serial.Serial('COM12', 9600, timeout=0.01)  # Cambia 'COM3' por tu puerto Arduino
except Exception as e:
    print(f"Error al conectar con Arduino: {e}")
    arduino = None

# Configuración de la ventana gráfica
ventana = tk.Tk()
ventana.title("Sensor LDR - Cambiar Color del Botón")
ventana.geometry("400x300")

# Configuración del botón
boton = tk.Button(ventana, text="LDR", font=("Arial", 14), width=20, height=2)
boton.pack(pady=100)

# Función para mapear valores
def mapear(valor, in_min, in_max, out_min, out_max):
    """Mapea un valor desde un rango de entrada a un rango de salida."""
    return int((valor - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# Bucle de actualización
def actualizar():
    if arduino and arduino.in_waiting > 0:  # Verifica si hay datos disponibles
        try:
            linea = arduino.readline().decode('utf-8').strip()  # Lee y procesa la línea
            if linea.isdigit():  # Asegura que el dato es un número válido
                valor_ldr = int(linea)
                # Mapear valor LDR (0-1023) a RGB (0-255)
                rojo = mapear(valor_ldr, 0, 1023, 0, 255)
                verde = mapear(valor_ldr, 0, 1023, 255, 0)
                azul = mapear(valor_ldr, 0, 1023, 50, 200)
                color_hex = f"#{rojo:02x}{verde:02x}{azul:02x}"  # Convertir a formato hexadecimal
                boton.config(bg=color_hex)  # Cambiar color del botón
        except Exception as e:
            print(f"Error al procesar datos: {e}")
    
    ventana.after(10, actualizar)  # Llama nuevamente a la función después de 10 ms

# Inicia la actualización continua
actualizar()

# Ejecuta la ventana gráfica
ventana.mainloop()

# Cierra el puerto serie al salir
if arduino:
    arduino.close()
