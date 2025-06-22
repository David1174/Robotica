import tkinter as tk
import serial

# Configuración del puerto serie
try:
    arduino = serial.Serial('COM12', 9600, timeout=0.01)  # Cambia 'COM3' según tu sistema
except Exception as e:
    print(f"Error al conectar con Arduino: {e}")
    arduino = None

# Configuración de la ventana gráfica
ventana = tk.Tk()
ventana.title("Lectura del Sensor LDR en Tiempo Real")
ventana.geometry("400x200")

# Etiqueta para mostrar el valor del sensor
etiqueta_valor = tk.Label(ventana, text="Valores LDR:  ---", font=("Arial", 16))
etiqueta_valor.place(x=100, y=70)

# Bucle de actualización
def actualizar():
    if arduino and arduino.in_waiting > 0:  # Verifica si hay datos disponibles
        try:
            linea = arduino.readline().decode('utf-8').strip()  # Lee y procesa la línea
            
            etiqueta_valor['text'] = f"Valores LDR:  {linea}"
        except Exception as e:
            etiqueta_valor.config(text="Error al leer datos")
    
    ventana.after(50, actualizar)  # Llama nuevamente a la función después de 1 ms

# Inicia la actualización continua
actualizar()

# Ejecuta la ventana gráfica
ventana.mainloop()

# Cierra el puerto serie al salir
if arduino:
    arduino.close()
