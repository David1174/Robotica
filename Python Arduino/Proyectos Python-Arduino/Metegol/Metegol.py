import serial
import pyttsx3
import pygame
import time
import random
import tkinter as tk  # Interfaz gráfica
import os

# Configuración del puerto serial (ajusta 'COM3' según tu sistema)
arduino = serial.Serial('COM7', 9600, timeout=1)

# Inicialización de Pygame para sonidos
pygame.mixer.init()

pygame.mixer.music.load("Tribuna_4-mp3.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(loops=-1)

sonido_gol2 = pygame.mixer.Sound("gol_2.mp3")
sonido_gol2.set_volume(0.5)

directorio_anuncios = r"D:\Robotica\Python Programacion Juegos USB\Proyectos Python-Arduino\Metegol\Anuncios"
directorio_GolesArg = r"D:\Robotica\Python Programacion Juegos USB\Proyectos Python-Arduino\Metegol\Goles-Arg"

GolesArg = [
    pygame.mixer.Sound(os.path.join(directorio_GolesArg, archivo))
    for archivo in os.listdir(directorio_GolesArg)
    if archivo.endswith(".wav")  # Asegúrate de que sean archivos .wav
]

# Carga los archivos anuncios .wav en la lista de sonidos
anuncios = [
    pygame.mixer.Sound(os.path.join(directorio_anuncios, archivo))
    for archivo in os.listdir(directorio_anuncios)
    if archivo.endswith(".wav")  # Asegúrate de que sean archivos .wav
]

# Variables del marcador  ------   Sector de variables

goles_equipo1 = 0
goles_equipo2 = 0

intervalo_reproduccion = 35 # Tiempo de reproduccion
ultimo_tiempo_reproduccion = time.time()

# Función para actualizar el marcador en la interfaz  ----    Sector de Funciones
def actualizar_marcador():
    marcador_label.config(text=f"{goles_equipo1} - {goles_equipo2}")

# Configuración de la interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Marcador de Metegol")
root.geometry("400x300")

# Etiquetas para mostrar el marcador
marcador_label = tk.Label(root, text="0 - 0", font=("Helvetica", 48))
marcador_label.pack(pady=20)

# Función para reproducir sonidos
def reproducir_sonido(sonido):  
    sonido.play()    

# Función para reproducir GolesArg aleatorios
def reproducir_GolesArg_aleatorio():
    GolesArg_aleatorio = random.choice(GolesArg)
    GolesArg_aleatorio.set_volume(1)
    GolesArg_aleatorio.play()

    while pygame.mixer.get_busy():  # Espera hasta que el sonido termine
        time.sleep(1)

# Función para reproducir anuncios aleatorios
def reproducir_anuncio_aleatorio():  
    anuncio_aleatorio = random.choice(anuncios)
    anuncio_aleatorio.set_volume(1)
    anuncio_aleatorio.play()

# Bucle principal para leer eventos desde Arduino
def leer_eventos():    
    global goles_equipo1, goles_equipo2, anuncio_aleatorio, ultimo_tiempo_reproduccion

    tiempo_actual = time.time()

    # Verificar si han pasado 10 segundos desde la última reproducción
    if tiempo_actual - ultimo_tiempo_reproduccion >= intervalo_reproduccion:
        reproducir_anuncio_aleatorio()
        ultimo_tiempo_reproduccion = tiempo_actual
    try:    
        evento = arduino.readline().decode().strip()        
        if evento:                       
            if "Gol Equipo 1" in evento:                
                goles_equipo1 += 1            
                reproducir_GolesArg_aleatorio()                                                  
               
            elif "Gol Equipo 2" in evento:
                goles_equipo2 += 1
                reproducir_sonido(sonido_gol2)
                
            actualizar_marcador()

    except Exception as e:
        print(f"Error: {e}")

    # Volver a llamar a esta función 
    root.after(400, leer_eventos)

# Inicia la lectura de eventos desde Arduino
leer_eventos()

# Inicia la interfaz gráfica
root.mainloop()
