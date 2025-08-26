import serial
import pyttsx3
import time

# Configura el puerto serial, asegúrate de que sea el mismo que utiliza tu Arduino
arduino_port = 'COM7'  # Cambia 'COM3' por el puerto adecuado (en Mac/Linux puede ser '/dev/ttyUSB0')
baud_rate = 9600

# Inicia conexión serial con Arduino
ser = serial.Serial(arduino_port, baud_rate)
engine = pyttsx3.init()  # Inicializa el motor de texto a voz
text_to_read = "Hola chicos como estan todos"

try:
    while True:
        if ser.in_waiting > 0:  # Verifica si hay datos en el puerto serial
            line = ser.readline().decode('utf-8').strip()
            print(line)
            if line == "Activar voz":
                engine.say(text_to_read)
                engine.runAndWait()
                #time.sleep(1)  # Pausa antes de la siguiente lectura
except KeyboardInterrupt:
    print("Programa terminado.")
finally:
    ser.close()
