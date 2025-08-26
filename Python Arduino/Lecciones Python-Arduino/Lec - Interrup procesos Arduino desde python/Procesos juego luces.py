import serial
import time

# Configuración del puerto serial
arduino_port = 'COM8'  # Ajusta según el puerto de tu Arduino
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Espera para establecer la conexión con el Arduino

# Función para iniciar el juego de luces
def start_light_game():
    ser.write(b'1')  # Envía 'S' para iniciar el juego de luces
    print("Juego de luces iniciado.")

# Función para detener el juego de luces
def stop_light_game():
    ser.write(b'0')  # Envía 'P' para detener el juego de luces
    print("Juego de luces detenido.")

# Inicia y detiene el juego de luces con un tiempo de espera en medio
start_light_game()
#time.sleep(6)  # Duración del juego de luces (10 segundos)
stop_light_game()

# Cierra la conexión serial
ser.close()
