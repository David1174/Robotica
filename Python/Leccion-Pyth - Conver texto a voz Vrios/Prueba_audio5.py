import tkinter as tk
from gtts import gTTS
import os
import pygame

# Función para generar el audio
def generar_audio(texto, archivo_audio):
    tts = gTTS(texto, lang='es')
    tts.save(archivo_audio)
    print(f"Archivo de audio '{archivo_audio}' generado correctamente.")

# Función para reproducir el audio
def reproducir_audio(archivo_audio):
    if not os.path.exists(archivo_audio):
        print(f"Error: El archivo '{archivo_audio}' no existe.")
        return
    pygame.mixer.init()
    pygame.mixer.music.load(archivo_audio)
    pygame.mixer.music.play()
    print(f"Reproduciendo: {archivo_audio}")

# Función principal para manejar el flujo
def manejar_audio(txt):
    archivo_audio = "texto_voz.mp3"
    if not os.path.exists(archivo_audio):  # Generar el audio si no existe
        generar_audio(txt, archivo_audio)
    reproducir_audio(archivo_audio)

# Crear la ventana gráfica
ventana = tk.Tk()
ventana.title("Lector de Texto")
ventana.geometry("300x200")

# Etiqueta de texto
label = tk.Label(ventana, text="Presiona el botón para escuchar el texto.")
label.pack(pady=20)

# Botón para generar y reproducir el audio
texto_a_leer = "Hola, este es un ejemplo de texto leído."
boton = tk.Button(ventana, text="Escuchar Voz", command=lambda: manejar_audio(texto_a_leer))
boton.pack(pady=20)

# Ejecutar la ventana
ventana.mainloop()
