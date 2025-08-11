import serial
import threading
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import time

class SensorReader:
    def __init__(self, port, baudrate=115200):
        self.ser = serial.Serial(port, baudrate, timeout=1)
        self.running = True
        self.humedad = []
        self.temperatura = []
        self.tiempos = []

    def leer_datos(self):
        while self.running:
            try:
                linea = self.ser.readline().decode().strip()
                if linea.startswith("HUMEDAD:"):
                    partes = linea.replace("HUMEDAD:", "").replace("TEMP:", "").split(",")
                    h = float(partes[0])
                    t = float(partes[1])
                    self.humedad.append(h)
                    self.temperatura.append(t)
                    self.tiempos.append(time.time())
            except Exception as e:
                print("Error:", e)

    def detener(self):
        self.running = False
        self.ser.close()

class App:
    def __init__(self, root, sensor):
        self.root = root
        self.sensor = sensor
        self.root.title("Valores de humedad y temperatura")

        self.fig = Figure(figsize=(8, 5))
        self.ax_hum = self.fig.add_subplot(211)
        self.ax_temp = self.fig.add_subplot(212)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

        self.actualizar_graficas()

    def actualizar_graficas(self):
        tiempos = [t - self.sensor.tiempos[0] for t in self.sensor.tiempos] if self.sensor.tiempos else []

        self.ax_hum.clear()
        self.ax_temp.clear()

        self.ax_hum.plot(tiempos, self.sensor.humedad, label="Humedad (%)", color="blue")
        self.ax_temp.plot(tiempos, self.sensor.temperatura, label="Temperatura (°C)", color="red")

        self.ax_hum.set_title("Humedad")
        self.ax_temp.set_title("Temperatura")

        self.ax_hum.set_ylabel("%")
        self.ax_temp.set_ylabel("°C")
        self.ax_temp.set_xlabel("Tiempo (s)")

        self.ax_hum.legend()
        self.ax_temp.legend()

        self.canvas.draw()
        self.root.after(1000, self.actualizar_graficas)

def main():
    puerto = "COM7"  # <-- Cambia esto según tu sistema
    sensor = SensorReader(puerto)

    hilo = threading.Thread(target=sensor.leer_datos)
    hilo.daemon = True
    hilo.start()

    root = tk.Tk()
    app = App(root, sensor)
    root.protocol("WM_DELETE_WINDOW", lambda: (sensor.detener(), root.destroy()))
    root.mainloop()

if __name__ == "__main__":
    main()
