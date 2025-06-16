import tkinter as tk
from gtts import gTTS
import os
import pygame
import time

# Función para generar el audio
def generar_audio(txto, audi):
    tts = gTTS(txto, lang='es')
    tts.save(audi)
    print(f"Archivo de audio '{audi}' generado correctamente.")

# Función para reproducir el audio
def reproducir_audio(aud):
    if not os.path.exists(aud):
        print(f"Error: El archivo '{aud}' no existe.")
        return
    pygame.mixer.init()
    #pygame.mixer.music.stop()
    pygame.mixer.music.load(aud)
    pygame.mixer.music.play()
    print(f"Reproduciendo: {aud}")

    if os.path.exists(aud):
        os.remove(aud)

# Función principal para manejar el flujo
def manejar_audio(txt):
    audio = "nom.mp3"
    if not os.path.exists(audio):  # Generar el audio si no existe
        generar_audio(txt, audio)
    reproducir_audio(audio)

# Crear la ventana gráfica
ventana = tk.Tk()
ventana.title("Lector de Texto")
ventana.geometry("300x200")

# Etiqueta de texto
label = tk.Label(ventana, text="Presiona el botón para escuchar el texto.")
label.pack(pady=20)

# Botón para generar y reproducir el audio
texto_a_leer = "bienvenido compa a mis clases ."
boton = tk.Button(ventana, text="Escuchar Voz", command=lambda: manejar_audio(texto_a_leer))
boton.pack(pady=20)

# Ejecutar la ventana
ventana.mainloop()
