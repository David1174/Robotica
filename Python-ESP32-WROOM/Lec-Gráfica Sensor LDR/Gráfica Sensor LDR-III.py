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
ventana.geometry("700x400")

# Frame principal para organizar los widgets horizontalmente
frame_principal = tk.Frame(ventana)
frame_principal.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)

# Frame izquierdo para el botón de adorno
frame_izq = tk.Frame(frame_principal)
frame_izq.pack(side=tk.LEFT, fill=tk.Y, padx=10)

# Botón de adorno "LED"
boton_led = tk.Button(frame_izq, text="LED", font=("Arial", 14, "bold"), bg="#e0e0e0", fg="#333333", width=10, height=2, state=tk.DISABLED)
boton_led.pack(pady=30)

# Frame derecho para la gráfica
frame_der = tk.Frame(frame_principal)
frame_der.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Título en la ventana
titulo = tk.Label(frame_der, text="Gráfica de LDR", font=("Arial", 16, "bold"))
titulo.pack(pady=5)

# Crear figura de Matplotlib (más pequeña)
fig, ax = plt.subplots(figsize=(0, 0))
linea, = ax.plot([], [], lw=2)
ax.set_title("Lectura de LDR (resistencia relativa) vs Tiempo", fontsize=8)
ax.set_xlabel("Tiempo (s)", fontsize=5)
ax.set_ylabel("Valor leído", fontsize=6)
ax.tick_params(axis='both', which='major', labelsize=6)
ax.grid(True)

# Embebe la figura en la ventana Tkinter con tamaño fijo
canvas = FigureCanvasTkAgg(fig, master=frame_der)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(pady=15)
canvas_widget.config(width=360, height=150)  # Ajusta el tamaño aquí

''' Embebe la figura en la ventana Tkinter
canvas = FigureCanvasTkAgg(fig, master=frame_der)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)
'''


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

def cerrar_ventana():
    try:
        if puerto_serie.is_open:
            puerto_serie.close()
    except:
        pass
    plt.close('all')
    ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

# Ejecuta el mainloop de Tkinter

ventana.mainloop()

