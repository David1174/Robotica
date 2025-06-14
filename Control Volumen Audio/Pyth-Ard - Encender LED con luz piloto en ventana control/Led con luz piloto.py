import tkinter as tk
import serial

# Configuración del puerto serial
arduino_port = "COM7"  # Cambia esto por el puerto donde esté conectado tu Arduino
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

# Variable para almacenar el estado del LED
led_encendido = False

# Función para alternar el estado del LED
def alternar_led():
    global led_encendido
    
    if led_encendido:
        ser.write(b"OFF\n")  # Apagar el LED
        boton.config(text="Encender LED")  # Cambiar el texto del botón
        actualizar_luz_piloto(False)  # Actualizar la luz piloto a rojo
        print("LED apagado")
    else:
        ser.write(b"ON\n")  # Encender el LED
        boton.config(text="Apagar LED")  # Cambiar el texto del botón
        actualizar_luz_piloto(True)  # Actualizar la luz piloto a verde
        print("LED encendido")
    
    # Cambiar el estado del LED
    led_encendido = not led_encendido

# Función para actualizar la luz piloto
def actualizar_luz_piloto(estado):
    if estado:
        luz_piloto.config(bg="green")  # Luz verde si el LED está encendido
    else:
        luz_piloto.config(bg="red")  # Luz roja si el LED está apagado

# Crear la ventana principal
root = tk.Tk()
root.title("Control de LED con Arduino")
root.geometry("300x150")

# Botón para alternar entre encender/apagar el LED
boton = tk.Button(root, text="Encender LED", command=alternar_led)
boton.grid(row=0, column=0, padx=10, pady=10)

# Luz piloto para indicar el estado del LED
luz_piloto = tk.Label(root, text="Luz Piloto", bg="red", width=10, height=2)
luz_piloto.grid(row=0, column=1, padx=10, pady=10)

# Iniciar el loop de la ventana
root.mainloop()

# Cerrar la conexión serial cuando la ventana se cierre
ser.close()