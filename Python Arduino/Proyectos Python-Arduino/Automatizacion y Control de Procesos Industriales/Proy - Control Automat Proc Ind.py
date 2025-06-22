import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3
import serial
import time
from datetime import datetime
import os
import numpy as np
import soundfile as sf
from gtts import gTTS
import tempfile
from playsound import playsound
import threading


# Configuración de conexión con Arduino (ajusta el puerto y la velocidad)
try:
    arduino = serial.Serial('COM8', 9600)  # Cambia 'COM3' al puerto de tu Arduino
    time.sleep(2)  # Espera para asegurar la conexión
except:
    arduino = None
    print("No se pudo conectar con Arduino")


# Funcion activacion luz
luz_on=False
def toggle_luz():
    global luz_on
    if arduino.is_open:
        if not luz_on:
            arduino.write(b'1')  # Enviar a arduino 
            button_luz.config(text="Apagar Luz")
        else:
            arduino.write(b'4')  # Enviar a arduino 
            button_luz.config(text="Encender Luz")
        luz_on = not luz_on

# Funcion activacion motor
motor_on=False
def toggle_motor():
    global motor_on
    if arduino.is_open:
        if not motor_on:
            arduino.write(b'2')  # Enviar a arduino 
            button_motor.config(text="Apagar Motor")

        else:
            arduino.write(b'5')  # Enviar a arduino
            button_motor.config(text="Encender Motor")
            
        motor_on = not motor_on

#Funcion activacion luz
luz_on2=False
def toggle_luz2():
    global luz_on2
    if arduino.is_open:
        if not luz_on2:
            arduino.write(b'3')  # Enviar a arduino
            button_luz2.config(text="Apagar Luz")
        else:
            arduino.write(b'6')  # Enviar a arduino
            button_luz2.config(text="Encender Luz")
        luz_on2 = not luz_on2

'''
# Función para convertir texto a audio
def text_to_audio():
    # Define el texto que deseas convertir en voz
    texto = "bienvenidos, gracias por su asistencia el dia de hoy, a continuación se presentará el siguiente proyecto: Automatización y control de Procesos Industriales."
     
    tts = gTTS(text=texto, lang="es")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        temp_path = fp.name
        tts.save(temp_path)

    data, samplerate = sf.read(temp_path)
    velocidad = 1.1  # Aumenta la velocidad en un 50%
    new_data = np.interp(np.arange(0, len(data), velocidad), np.arange(0, len(data)), data)    
    sf.write(temp_path, new_data, samplerate)

    playsound(temp_path)

    # Elimina el archivo temporal después de la reproducción
    os.remove(temp_path)
'''

'''
def leer_texto(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Configurar velocidad
    engine.setProperty('volume', 0.9)  # Configurar volumen
    engine.say(texto)
    engine.runAndWait()

def text_to_audio():
    # Texto a reproducir
    texto = "ahora si te agarré, piscuí durázno."
    # Crear y ejecutar un hilo para la voz
    hilo_voz = threading.Thread(target=leer_texto, args=(texto,))
    hilo_voz.start()
'''

# Función para convertir texto a audio
def reproducir_audio(texto):     
     
    tts = gTTS(text=texto, lang="es")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        temp_path = fp.name
        tts.save(temp_path)

    data, samplerate = sf.read(temp_path)
    velocidad = 1.1  # Aumenta la velocidad en un 50%
    new_data = np.interp(np.arange(0, len(data), velocidad), np.arange(0, len(data)), data)   
    new_data = new_data * 1

    # Asegurarse de que los valores no se salgan del rango de -1 a 1 (normalización)
    new_data = np.clip(new_data, -1.0, 1.0)

    sf.write(temp_path, new_data, samplerate)
    playsound(temp_path)
    # Elimina el archivo temporal después de la reproducción
    os.remove(temp_path)


def bienvenida(): 
    txt="Bienvenidos a nuestra escuela de educación tecnica número 3 de maquinista savio"
    hilo = threading.Thread(target=reproducir_audio, args=(txt,))
    hilo.start()

def alarma(): 
    txt_alarm="Atención, se detecta inestabilidad de iluminacion en el sector 9"
    hilo = threading.Thread(target=reproducir_audio, args=(txt_alarm,))
    hilo.start()


#Funcion muestra valores del sensor de luz LDR
boolean=True
c=0
def actualizar_LDR():
    global c,boolean
    if arduino and arduino.in_waiting > 0:  # Verifica si hay datos disponibles
        try:
            linea = arduino.readline().decode('utf-8').strip()  # Lee y procesa la línea         
            etiqueta_valor['text'] = f"Valores LDR:  {linea}"
           
        except Exception as e:
            etiqueta_valor.config(text="Error al leer datos")

        if linea>'700':
            c=c+1
            if c>40 and boolean:
                alarma()
                boolean=False
                c=0  
        else:
            boolean=True         
                
    window.after(50, actualizar_LDR)  # Llama nuevamente a la función después de 1 ms


#Automatizacion
autom1_a=True
autom1_b=True
def automatizacion():
    global autom1_a,autom1_b
    
    # Obtiene la hora actual del sistema en formato HH:MM  %H:%M:%S
    hora_actual = datetime.now().strftime("%H:%M")
    hora_en_ventana = datetime.now().strftime("%H:%M:%S")
    # Actualiza el texto de la etiqueta con la hora actual
    etiqueta_hora.config(text=hora_en_ventana)

    # Verifica si la hora actual coincide con el primer horario ingresado y si no se ha mostrado el mensaje
    if hora_actual == entrada_hora1.get() and autom1_a:
        arduino.write(b'1')
        autom1_a=False
        autom1_b=True      
       
    # Verifica si la hora actual coincide con el segundo horario ingresado y si no se ha mostrado el mensaje
    elif hora_actual == entrada_hora2.get() and autom1_b:
        arduino.write(b'4')
        autom1_b=False
        autom1_a=True
      
    if hora_actual == entrada_hora3.get():
        arduino.write(b'2')
    elif hora_actual == entrada_hora4.get():
        arduino.write(b'5')

      
    if hora_actual == entrada_hora5.get():
        arduino.write(b'3')        
    elif hora_actual == entrada_hora6.get():
        arduino.write(b'6')
    
    window.after(1000, automatizacion)

# Función para cargar la hora ingresada en el primer campo de entrada y quitar el foco
def cargar_hora1(event=None):
    global hora_alarma1
    hora_alarma1 = entrada_hora1.get()   
    print(f"Hora de alarma 1 guardada: {hora_alarma1}")
    window.focus()  # Quita el foco del campo de entrada

def cargar_hora2(event=None):
    global hora_alarma2
    hora_alarma2 = entrada_hora2.get()    
    print(f"Hora de alarma 2 guardada: {hora_alarma2}")
    window.focus()  # Quita el foco del campo de entrada


def cargar_hora3(event=None):
    global hora_alarma3
    hora_alarma3 = entrada_hora3.get()    
    print(f"Hora de alarma 3 guardada: {hora_alarma3}")
    window.focus()  # Quita el foco del campo de entrada

def cargar_hora4(event=None):
    global hora_alarma4
    hora_alarma4 = entrada_hora4.get()    
    print(f"Hora de alarma 4 guardada: {hora_alarma4}")
    window.focus()  # Quita el foco del campo de entrada


def cargar_hora5(event=None):
    global hora_alarma5
    hora_alarma5 = entrada_hora5.get()    
    print(f"Hora de alarma 4 guardada: {hora_alarma5}")
    window.focus()  # Quita el foco del campo de entrada

def cargar_hora6(event=None):
    global hora_alarma6
    hora_alarma6 = entrada_hora6.get()    
    print(f"Hora de alarma 4 guardada: {hora_alarma6}")
    window.focus()  # Quita el foco del campo de entrada


# Configuración de la ventana general de tkinter
window = tk.Tk()
window.title("Automatizacion y Control de Procesos Industriales")
window.geometry("800x600") # (x=Col=Ancho; y=Fil=Alto)

# Título
title1 = tk.Label(window, text="EEST Nº3 - Eva Peron Maquinista Savio", font=("Arial", 25))
#title.grid(row=0, column=2, columnspan=2, pady=1)
title1.place(x=50, y=20)

# Título
title2 = tk.Label(window, text="7mo 4ta - Especialidad IPP - Informática Personal y Profesional", font=("Arial", 16))
title2.place(x=50, y=80)

# Ruta de la imagen
image_path = r"D:\Robotica\Z-Imagenes\Escudo-Tec3.jpg"  # Asegúrate de colocar la ruta correcta aquí

# Cargar y mostrar la imagen
try:
    image = Image.open(image_path)
    image = image.resize((100, 100))  # Cambia el tamaño según sea necesario
    tk_image = ImageTk.PhotoImage(image)  # Crear la imagen en un formato compatible con Tkinter

    # Colocar la imagen en un Label y ubicarlo en la ventana
    label_image = tk.Label(window, image=tk_image)
    label_image.image = tk_image  # Mantener una referencia a la imagen
    label_image.place(x=600, y=180)  # Ubicar en las coordenadas deseadas

except Exception as e:
    print("No se pudo cargar la imagen:", e)


# Botones y ubicacion en coordenadas específicas
button_luz = tk.Button(window, text="Encender Luz",command=toggle_luz, width=20, height=4, ) #(width=Ancho; height=alto)
button_luz.place(x=50, y=200)  # Coordenadas del botón en la ventana (ajusta según prefieras)

button_motor = tk.Button(window, text="Activar motor",command=toggle_motor, width=20, height=4) #(width=Ancho; height=alto)
button_motor.place(x=250, y=200)  # Coordenadas de ubicacion de motor

button_luz2 = tk.Button(window, text="Encender Luz2",command=toggle_luz2, width=20, height=4, ) #(width=Ancho; height=alto)
button_luz2.place(x=50, y=300)  # Coordenadas del botón en la ventana (ajusta según prefieras)

# Botón para convertir texto a audio
audio_button = tk.Button(window, text="Convertir texto a audio", command=bienvenida, width=30, height=2)
audio_button.place(x=50, y=500) #(50,450)

#Etiqueta para mostrar la hora actual
etiqueta_hora = tk.Label(window, font=("Arial", 20), fg="blue")
etiqueta_hora.place(x=520, y=530)

# Etiqueta y primer linea de entrada de hora
etiq_primera_linea = tk.Label(window, text="Ingrese primera hora (HH:MM):")
etiq_primera_linea.place(x=340, y=360)  # Ubicación específica

entrada_hora1 = tk.Entry(window, font=("Arial", 20), justify="center", width=5)
entrada_hora1.place(x=520, y=350)  # Ubicación específica para el primer campo de entrada
entrada_hora1.bind("<Return>", cargar_hora1)
entrada_hora1.bind("<FocusOut>", cargar_hora1)

entrada_hora2 = tk.Entry(window, font=("Arial", 20), justify="center", width=5)
entrada_hora2.place(x=620, y=350)  # Ubicación específica para el segundo campo de entrada
entrada_hora2.bind("<Return>", cargar_hora2)
entrada_hora2.bind("<FocusOut>", cargar_hora2)


# Etiqueta y segunda linea de entrada de hora
etiq_segunda_linea = tk.Label(window, text="Ingrese primera hora (HH:MM):")
etiq_segunda_linea.place(x=340, y=410)  # Ubicación específica

entrada_hora3 = tk.Entry(window, font=("Arial", 20), justify="center", width=5)
entrada_hora3.place(x=520, y=400)  # Ubicación específica del tercer campo de entrada
entrada_hora3.bind("<Return>", cargar_hora3)
entrada_hora3.bind("<FocusOut>", cargar_hora3)

entrada_hora4 = tk.Entry(window, font=("Arial", 20), justify="center", width=5)
entrada_hora4.place(x=620, y=400)  # Ubicación específica del cuarto campo de entrada
entrada_hora4.bind("<Return>", cargar_hora4)
entrada_hora4.bind("<FocusOut>", cargar_hora4)


# Etiqueta tercer linea de entrada de hora
etiq_segunda_linea = tk.Label(window, text="Ingrese primera hora (HH:MM):")
etiq_segunda_linea.place(x=340, y=460)  # Ubicación específica


entrada_hora5 = tk.Entry(window, font=("Arial", 20), justify="center", width=5)
entrada_hora5.place(x=520, y=460)  # Ubicación específica del tercer campo de entrada
entrada_hora5.bind("<Return>", cargar_hora5)
entrada_hora5.bind("<FocusOut>", cargar_hora5)

entrada_hora6 = tk.Entry(window, font=("Arial", 20), justify="center", width=5)
entrada_hora6.place(x=620, y=460)  # Ubicación específica del tercer campo de entrada
entrada_hora6.bind("<Return>", cargar_hora6)
entrada_hora6.bind("<FocusOut>", cargar_hora6)

# Etiqueta para mostrar el valor del sensor LDR
etiqueta_valor = tk.Label(window, text="Valor del sensor LDR: ---", font=("Arial", 10))
etiqueta_valor.place(x=50, y=400)  # Posición inicial (coordenadas en píxeles)


actualizar_LDR()
automatizacion()

# Ejecutar la interfaz gráfica
window.mainloop()

# Cierra la conexión con Arduino al cerrar la ventana
if arduino:
    arduino.close()
