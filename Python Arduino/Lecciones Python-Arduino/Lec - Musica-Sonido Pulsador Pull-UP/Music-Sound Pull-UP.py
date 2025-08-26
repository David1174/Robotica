import pygame
import serial
import time

# Configuración del puerto serie
arduino_port = 'COM7'  # Cambia a tu puerto de Arduino
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)

# Inicializa pygame
pygame.mixer.init()

# Carga el archivo de música
pygame.mixer.music.load(r"D:\Robotica\Python Programacion Juegos USB\Musica Sonido Juegos\Música\Mechanical.mp3")  # Cambia a tu ruta de música

is_playing = True  # Estado de la música

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        print(line)
        if line == "ButtonPressed":
            if is_playing:
                print("Deteniendo música...")
                pygame.mixer.music.stop()  # Detener música
                is_playing = False
            else:
                print("Reproduciendo música...")
                pygame.mixer.music.play()  # Iniciar música
                is_playing = True

    time.sleep(0.1)  # Pequeño retraso para no saturar el puerto serie
