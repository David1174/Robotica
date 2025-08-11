import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

# Configuración del puerto (ajusta el COM según tu PC)
puerto_serie = serial.Serial('COM7', 115200)  # Cambia 'COM3' si es otro puerto

# Configuración de la gráfica
tiempo_max = 60  # segundos visibles en la gráfica
intervalo = 50  # intervalo de actualización en milisegundos

# Inicializar buffers
tiempos = deque(maxlen=tiempo_max * 1000 // intervalo)
valores = deque(maxlen=tiempo_max * 1000 // intervalo)

fig, ax = plt.subplots()
linea, = ax.plot([], [], lw=2)
ax.set_title("Lectura de LDR (resistencia relativa) vs Tiempo")
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Valor leído")
ax.grid(True)

# Tiempo relativo
tiempo_inicial = None

def actualizar(frame):
    global tiempo_inicial

    try:
        # ...existing code...
        dato = puerto_serie.readline().decode().strip()
        valor = int(dato)

        if tiempo_inicial is None:
            tiempo_inicial = frame * (intervalo / 1000)

        # Multiplica el avance del tiempo (por ejemplo, x2 para el doble de velocidad)
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
plt.show()






'''
def actualizar(frame):
    global tiempo_inicial

    try:
        dato = puerto_serie.readline().decode().strip()
        valor = int(dato)

        if tiempo_inicial is None:
            tiempo_inicial = frame * (intervalo / 1000)

        tiempo_actual = frame * (intervalo / 1000) - tiempo_inicial
        tiempos.append(tiempo_actual)
        valores.append(valor)

# ...existing code...
        linea.set_data(tiempos, valores)
        # Mostrar solo los últimos 'tiempo_max' segundos (ventana deslizante)
        ax.set_xlim(tiempo_actual - tiempo_max, tiempo_actual)
        ax.set_ylim(0, 4095)  # Rango de 12 bits ADC ESP32
# ...existing code...

 #       linea.set_data(tiempos, valores)
 #      ax.set_xlim(max(0, tiempo_actual - tiempo_max), tiempo_actual)
 #       ax.set_ylim(0, 4095)  # Rango de 12 bits ADC ESP32

'''
