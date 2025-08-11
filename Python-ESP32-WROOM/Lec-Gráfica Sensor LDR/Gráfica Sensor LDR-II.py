import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import deque
import tkinter as tk

# Configuración del puerto (ajusta el COM según tu PC)
puerto_serie = serial.Serial('COM7', 115200)

# Configuración de la gráfica
tiempo_max = 60  # segundos visibles en la gráfica
intervalo = 50  # intervalo de actualización en milisegundos

# Inicializar buffers
tiempos = deque(maxlen=tiempo_max * 1000 // intervalo)
valores = deque(maxlen=tiempo_max * 1000 // intervalo)

# Crear ventana principal con Tkinter
ventana = tk.Tk()
ventana.title("Gráfica de LDR")
ventana.geometry("800x500")

# Título en la ventana
titulo = tk.Label(ventana, text="Gráfica de LDR", font=("Arial", 18, "bold"))
titulo.pack(pady=10)

# Crear figura de Matplotlib
fig, ax = plt.subplots()
linea, = ax.plot([], [], lw=2)
ax.set_title("Lectura de LDR (resistencia relativa) vs Tiempo")
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Valor leído")
ax.grid(True)

# Embebe la figura en la ventana Tkinter
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)

# Tiempo relativo
tiempo_inicial = None

def actualizar(frame):
    global tiempo_inicial
    try:
        dato = puerto_serie.readline().decode().strip()
        valor = int(dato)

        if tiempo_inicial is None:
            tiempo_inicial = frame * (intervalo / 1000)

        velocidad = 4  # Cambia este valor para ajustar la velocidad
        tiempo_actual = (frame * (intervalo / 1000) - tiempo_inicial) * velocidad
        tiempos.append(tiempo_actual)
        valores.append(valor)

        linea.set_data(tiempos, valores)
        if tiempo_actual > tiempo_max:
            ax.set_xlim(tiempo_actual - tiempo_max, tiempo_actual)
        else:
            ax.set_xlim(0, tiempo_max)
        ax.set_ylim(0, 4095)
    except Exception as e:
        print(f"Error leyendo dato: {e}")

    return linea,

ani = animation.FuncAnimation(fig, actualizar, interval=intervalo)

# Ejecuta el mainloop de Tkinter
ventana.mainloop()