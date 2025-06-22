import tkinter as tk
import serial

# Configura la conexión con Arduino
arduino = serial.Serial('COM12', 9600)  # Cambia 'COM3' según el puerto de tu Arduino

# Estado inicial del LED
led_encendido = False

# Función para alternar el LED
def alternar_led():
    global led_encendido  # Permite modificar la variable global
    if led_encendido:
        arduino.write(b'OFF\n')  # Enviar comando 'OFF'
        
        btn_alternar.config(text="Encender LED")  # Cambiar texto del botón
        led_encendido = False
    else:
        arduino.write(b'ON\n')  # Enviar comando 'ON'
       
        btn_alternar.config(text="Apagar LED")  # Cambiar texto del botón
        led_encendido = True

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Control de LED con Arduino")
ventana.geometry("300x200")

# Crear botón y etiqueta
btn_alternar = tk.Button(ventana,text="Encender LED",command=alternar_led,bg="blue",fg="white",font=("Arial", 14), width=15,height=2)   

btn_alternar.place(x=100, y=100)


# Iniciar el bucle de la ventana
ventana.mainloop()

