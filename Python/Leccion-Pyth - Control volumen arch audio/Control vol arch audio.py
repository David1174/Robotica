import pygame
import time

# Inicializa pygame
pygame.mixer.init()

# Carga el archivo de audio
pygame.mixer.music.load("D:\Robotica\Python\Control volumen arch audio\Locución.mp3")

# Ajusta el volumen (0.0 a 1.0)
pygame.mixer.music.set_volume(0.3)  # Volumen al máximo

# Reproduce el archivo
pygame.mixer.music.play()

# Mantén el programa en ejecución mientras se reproduce el audio
while pygame.mixer.music.get_busy():
    time.sleep(1)  # Espera 1 segundo entre cada comprobación
