import pygame
import random
import time
import os

# Inicializar pygame
pygame.mixer.init()

# Obtener una lista de archivos de audio en la carpeta
carpeta_sonidos = "D:/Robotica/Python Programacion Juegos USB/Proyectos Python-Arduino/Metegol/Anuncios"  # Cambia si tus sonidos están en otra ubicación
archivos_sonidos = [f for f in os.listdir(carpeta_sonidos) if f.endswith(('.mp3', '.wav'))]

def reproducir_sonido_aleatorio():
    """Selecciona y reproduce un sonido aleatorio."""
    sonido = random.choice(archivos_sonidos)
    print(f"Reproduciendo: {sonido}")
    pygame.mixer.music.load(sonido)
    pygame.mixer.music.play()
    
    # Esperar hasta que termine la reproducción
    while pygame.mixer.music.get_busy():
        time.sleep(1)

# Reproducir sonidos aleatorios en un bucle
try:
    while True:
        reproducir_sonido_aleatorio()
        time.sleep(2)  # Pausa entre sonidos
except KeyboardInterrupt:
    print("Reproducción detenida.")
