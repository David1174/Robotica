import tkinter as tk
from datetime import datetime
from tkinter import messagebox

# Variables globales para almacenar los horarios ingresados por el usuario
hora_alarma1 = ""
hora_alarma2 = ""

# Variables para rastrear si ya se ha mostrado el mensaje para cada hora
mensaje_mostrado_hora1 = False
mensaje_mostrado_hora2 = False

# Función para actualizar la hora en la etiqueta y verificar la coincidencia
def actualizar_hora():
    global mensaje_mostrado_hora1, mensaje_mostrado_hora2
    
    # Obtiene la hora actual del sistema en formato HH:MM
    hora_actual = datetime.now().strftime("%H:%M")
    # Actualiza el texto de la etiqueta con la hora actual
    etiqueta_hora.config(text=hora_actual)

    # Verifica si la hora actual coincide con el primer horario ingresado y si no se ha mostrado el mensaje
    if hora_actual == hora_alarma1 and not mensaje_mostrado_hora1:
        messagebox.showinfo("Alerta", "¡La hora coincide con la hora ingresada en el primer campo!")
        mensaje_mostrado_hora1 = True  # Marca que ya se mostró el mensaje para el primer horario

    # Verifica si la hora actual coincide con el segundo horario ingresado y si no se ha mostrado el mensaje
    elif hora_actual == hora_alarma2 and not mensaje_mostrado_hora2:
        messagebox.showinfo("Alerta", "¡La hora coincide con la hora ingresada en el segundo campo!")
        mensaje_mostrado_hora2 = True  # Marca que ya se mostró el mensaje para el segundo horario

    # Programa la función para que se ejecute de nuevo en 1000 ms (1 segundo)
    ventana.after(1000, actualizar_hora)

# Función para cargar la hora ingresada en el primer campo de entrada y quitar el foco
def cargar_hora1(event=None):
    global hora_alarma1, mensaje_mostrado_hora1
    hora_alarma1 = entrada_hora1.get()
    mensaje_mostrado_hora1 = False  # Reinicia el mensaje para la primera hora
    print(f"Hora de alarma 1 guardada: {hora_alarma1}")
    ventana.focus()  # Quita el foco del campo de entrada

# Función para cargar la hora ingresada en el segundo campo de entrada y quitar el foco
def cargar_hora2(event=None):
    global hora_alarma2, mensaje_mostrado_hora2
    hora_alarma2 = entrada_hora2.get()
    mensaje_mostrado_hora2 = False  # Reinicia el mensaje para la segunda hora
    print(f"Hora de alarma 2 guardada: {hora_alarma2}")
    ventana.focus()  # Quita el foco del campo de entrada

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Reloj con Dos Alertas")
ventana.geometry("400x300")

# Etiqueta para mostrar la hora actual
etiqueta_hora = tk.Label(ventana, font=("Arial", 30), fg="blue")
etiqueta_hora.pack(pady=10)

# Etiqueta y primer campo de entrada de hora
etiqueta_ingresar_hora1 = tk.Label(ventana, text="Ingrese primera hora (HH:MM):")
etiqueta_ingresar_hora1.place(x=20, y=150)  # Ubicación específica
entrada_hora1 = tk.Entry(ventana, font=("Arial", 20), justify="center", width=5)
entrada_hora1.place(x=250, y=145)
# Evento para guardar la hora en la variable al presionar "Enter" o al perder el enfoque
entrada_hora1.bind("<Return>", cargar_hora1)
entrada_hora1.bind("<FocusOut>", cargar_hora1)

# Etiqueta y segundo campo de entrada de hora
etiqueta_ingresar_hora2 = tk.Label(ventana, text="Ingrese segunda hora (HH:MM):")
etiqueta_ingresar_hora2.place(x=20, y=200)  # Ubicación específica
entrada_hora2 = tk.Entry(ventana, font=("Arial", 20), justify="center", width=5)
entrada_hora2.place(x=250, y=195)
# Evento para guardar la hora en la variable al presionar "Enter" o al perder el enfoque
entrada_hora2.bind("<Return>", cargar_hora2)
entrada_hora2.bind("<FocusOut>", cargar_hora2)

# Inicia la actualización de la hora
actualizar_hora()

# Inicia el bucle de la interfaz gráfica
ventana.mainloop()
