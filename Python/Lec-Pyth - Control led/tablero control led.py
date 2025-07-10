# Este programa crea una interfaz gráfica simple para controlar un LED.
# Utiliza la biblioteca tkinter para crear la ventana y los elementos de la interfaz.

import tkinter as tk

class ControlLedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprendiendo")
        self.root.geometry("300x300")
        self.root.configure(bg="#D6EAF8")  # fondo azul claro

        # Título dentro del espacio de trabajo
        self.titulo = tk.Label(self.root, text="Control de led", font=("Arial", 16), bg="#D6EAF8")
        self.titulo.pack(pady=10)

        # Canvas para dibujar la luz
        self.canvas = tk.Canvas(self.root, width=200, height=150, bg="#D6EAF8", highlightthickness=0)
        self.canvas.pack()

        # Dibujo de la luz (círculo)
        self.luz_encendida = False
        self.luz = self.canvas.create_oval(90, 50, 150, 110, fill="gray")

        # Botón único que prende/apaga
        self.boton = tk.Button(self.root, text="Encender", command=self.toggle_luz)
        self.boton.pack(pady=20)

    def toggle_luz(self):
        if self.luz_encendida:
            self.canvas.itemconfig(self.luz, fill="gray")
            self.boton.config(text="Encender")
        else:
            self.canvas.itemconfig(self.luz, fill="green")
            self.boton.config(text="Apagar")
        self.luz_encendida = not self.luz_encendida

# Crear y ejecutar la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = ControlLedApp(root)
    root.mainloop()
