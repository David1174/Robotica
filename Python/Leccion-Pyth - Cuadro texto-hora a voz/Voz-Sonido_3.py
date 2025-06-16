import tkinter as tk
import pyttsx3  # Nueva librería para control de voz
from datetime import datetime

# Inicializar el motor de texto a voz
engine = pyttsx3.init()

# Función para obtener y mostrar las voces disponibles
def listar_voces():
    voces = engine.getProperty('voices')
    lista_voces.delete(0, tk.END)  # Limpiar la lista
    for i, voz in enumerate(voces):
        lista_voces.insert(tk.END, f"{i}: {voz.name} ({voz.languages})")

# Función para reproducir el texto con la voz seleccionada
def reproducir_texto():
    texto = entrada_texto.get()
    if texto:
        configurar_voz_y_leer(texto)

# Función para leer la hora actual
def reproducir_hora():
    hora_actual = datetime.now().strftime("Son las %H horas y %M minutos.")
    configurar_voz_y_leer(hora_actual)

# Configurar la voz y leer el texto
def configurar_voz_y_leer(texto):
    voz_id = lista_voces.curselection()  # Obtener la voz seleccionada
    if voz_id:
        engine.setProperty('voice', engine.getProperty('voices')[voz_id[1]].id)
    engine.setProperty('rate', int(entrada_velocidad.get()))  # Configurar la velocidad
    engine.say(texto)
    engine.runAndWait()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Texto a Voz con pyttsx3")

# Campo de entrada para el texto
label_texto = tk.Label(ventana, text="Escribe una palabra o frase:", font=("Arial", 12))
label_texto.pack(pady=5)

entrada_texto = tk.Entry(ventana, width=30, font=("Arial", 12))
entrada_texto.pack(pady=5)

# Botones para reproducir el texto y la hora
boton_texto = tk.Button(ventana, text="Reproducir Texto", command=reproducir_texto)
boton_texto.pack(pady=5)

boton_hora = tk.Button(ventana, text="Reproducir Hora Actual", command=reproducir_hora)
boton_hora.pack(pady=5)

# Selector de velocidad de voz
label_velocidad = tk.Label(ventana, text="Velocidad de voz:", font=("Arial", 12))
label_velocidad.pack(pady=5)

entrada_velocidad = tk.Entry(ventana, width=5, font=("Arial", 12))
entrada_velocidad.insert(0, "150")  # Velocidad por defecto
entrada_velocidad.pack(pady=5)

# Lista de voces disponibles
label_voces = tk.Label(ventana, text="Selecciona una voz:", font=("Arial", 12))
label_voces.pack(pady=5)

lista_voces = tk.Listbox(ventana, height=5)
lista_voces.pack(pady=5)

boton_listar = tk.Button(ventana, text="Listar Voces", command=listar_voces)
boton_listar.pack(pady=5)

ventana.mainloop()