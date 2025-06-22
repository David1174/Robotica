
import tkinter as tk
import serial
import time
import pyttsx3

# Inicializa el motor de pyttsx3
engine = pyttsx3.init()

# Configuración del puerto serial (ajusta el puerto y la velocidad)
arduino_port = "COM12"  # Cambia esto al puerto que esté usando tu Arduino
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

# Variable que almacena el estado del LED (False = apagado, True = encendido)
led_encendido = False

# Función para configurar la velocidad y volumen de la voz
def configurar_voz(velocidad, volumen):
    # Cambiar la velocidad (default es 200)
    engine.setProperty('rate', velocidad)
    # Cambiar el volumen (default es 1.0, que es el máximo)
    engine.setProperty('volume', volumen)  


# Función para actualizar la temperatura y humedad
def actualizar_datos():
    try:
        # Leer línea desde Arduino
        linea = ser.readline().decode('utf-8').strip()
        print(linea)
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
    root.after(2000, actualizar_datos)


#
def alerta_temp():
    engine.setProperty('voice', engine.getProperty('voices')[2].id)
    engine.say("Alerta, la temperatura está llegando a valores críticos para este proceso")
    engine.runAndWait()


# Saludo y Presentacion
def presentacion():
    engine.setProperty('voice', engine.getProperty('voices')[2].id)
    engine.say("Bienvenidos a la escuela Técnica Nº3")
    engine.runAndWait()
        

# Función para encender/apagar el Motor
def alternar_led():
    global led_encendido
    boton_pres.config(text="Saludo y Presentación")
    if led_encendido:
        ser.write(b'L')  # Enviar el comando 'L' para apagar el LED
        boton_led.config(text="Activar Motor")  # Cambiar el texto del botón
        
    else:
        ser.write(b'H')  # Enviar el comando 'H' para encender el LED
        boton_led.config(text="Apagar Motor")  # Cambiar el texto del botón

        
        engine.setProperty('voice', engine.getProperty('voices')[2].id)
        engine.say("Atencion, Activando motór")
        engine.runAndWait()

    led_encendido = not led_encendido  # Alternar el estado del LED


# Crear la ventana principal
root = tk.Tk()
root.title("Datos de Temperatura y Humedad")

# Tamaño de la ventana
root.geometry("400x300")

# Etiqueta para la temperatura
etiqueta_temperatura = tk.Label(root, text="Temperatura: --°C", font=("Helvetica", 10))
etiqueta_temperatura.place(x=50, y=90)  # Posicionar la etiqueta en la ventana

# Etiqueta para la humedad
etiqueta_humedad = tk.Label(root, text="Humedad: --%", font=("Helvetica", 10))
etiqueta_humedad.place(x=50, y=130)  # Posicionar la etiqueta en la ventana

# Botón para encender/apagar motor
boton_led = tk.Button(root, text="Activar Motor", command=alternar_led, font=("Helvetica", 12))
boton_led.place(x=50, y=180)  # Posicionar el botón en la ventana

# Botón para saludar
boton_pres = tk.Button(root, text="Saludo y presentación", command=presentacion, font=("Helvetica", 12))
boton_pres.place(x=50, y=30)  # Posicionar el botón en la ventana

#Configura velocidad y volumen
configurar_voz(170, 1.0)

# Llamar a la función para actualizar los datos por primera vez
actualizar_datos()

# Iniciar el loop de la ventana
root.mainloop()
