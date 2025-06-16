import pygame
import random
import os
import time

# Inicializa pygame y el mezclador de sonido
pygame.init()
pygame.mixer.init()

# Define el directorio donde están los archivos de sonido
directorio_sonidos = r"D:\Robotica\Python\Pyth - Reprod sound aleat de una lista"

# Cargar todos los archivos .wav en la lista de sonidos
sonidos = [
    pygame.mixer.Sound(os.path.join(directorio_sonidos, archivo))
    for archivo in os.listdir(directorio_sonidos)
    if archivo.endswith(".wav")  # Asegúrate de que sean archivos .wav
]


# Función para reproducir un sonido aleatorio
def reproducir_sonido_aleatorio():
    sonido_aleatorio = random.choice(sonidos)
    sonido_aleatorio.play()

    # Espera hasta que el sonido termine de reproducirse
    while pygame.mixer.get_busy():
        time.sleep(0.1)  # Espera un corto periodo para evitar uso excesivo de CPU

# Bucle para reproducir sonidos aleatorios
try:
    while True:
        reproducir_sonido_aleatorio()
        time.sleep(1)  # Espera 1 segundo entre reproducciones
except KeyboardInterrupt:
    print("Programa detenido por el usuario.")

# Cierra pygame al final
pygame.quit()
