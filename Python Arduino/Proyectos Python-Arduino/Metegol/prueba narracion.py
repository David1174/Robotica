import pyttsx3
import pygame

# Inicializar el motor de voz
narrador = pyttsx3.init()

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("Tribuna_1.mp3")
pygame.mixer.music.play()

# Ajustar propiedades
narrador.setProperty('rate', 150)  # Velocidad de la voz (puedes ajustarla)
narrador.setProperty('volume', 1.0)  # Volumen máximo (1.0 es el tope)

# Usar una voz específica (ajusta según tu sistema)
narrador.setProperty('voice', narrador.getProperty('voices')[2].id)  # Voz predeterminada

# Probar la narración con volumen máximo
narrador.say("¡Hola! Esta es una prueba de narración con el volumen al máximo.")
narrador.runAndWait()
