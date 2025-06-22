import pygame
import sys
import serial
import time

# Configurar la conexión serial (ajusta el puerto según sea necesario)
arduino = serial.Serial('COM8', 9600, timeout=1)
time.sleep(2)  # Dar tiempo al Arduino para inicializar

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(r"D:\Robotica\Python Arduino\Proyectos Python-Arduino\Python TaTeTi\Techno.mp3")
pygame.mixer.music.play()

# Cargar efectos de sonido
sonido_click = pygame.mixer.Sound(r"D:\Robotica\Python Arduino\Proyectos Python-Arduino\Python TaTeTi\mouse2.mp3")  # Sonido al hacer clic
sonido_ganador = pygame.mixer.Sound(r"D:\Robotica\Python Arduino\Proyectos Python-Arduino\Python TaTeTi\Empate.mp3")  # Sonido al ganar
sonido_empate = pygame.mixer.Sound(r"D:\Robotica\Python Arduino\Proyectos Python-Arduino\Python TaTeTi\Empate.mp3")  # Sonido al empatar

# Definir los colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
GRIS_CLARO = (100, 200, 200)
VERDE_CLARO = (144, 144, 144)

# Configurar el tamaño de la pantalla
ANCHO = 600
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Configurar el título
pygame.display.set_caption("Tateti - Tres en Línea")

color_fondo = (200, 200, 200)  # RGB para blanco
pantalla.fill(color_fondo)

# Definir el tablero (una lista de 9 elementos vacíos)
tablero = [""] * 9

# Definir algunas variables del juego
turno = None  # El primer jugador será definido por el usuario
fin_juego = False
ganador = None
senial_ganador=True

# Dibujar el tablero
def dibujar_tablero():
    # Líneas verticales
    pygame.draw.line(pantalla, NEGRO, (200, 0), (200, 600), 5)
    pygame.draw.line(pantalla, NEGRO, (400, 0), (400, 600), 5)
    # Líneas horizontales
    pygame.draw.line(pantalla, NEGRO, (0, 200), (600, 200), 5)
    pygame.draw.line(pantalla, NEGRO, (0, 400), (600, 400), 5)

# Dibujar las piezas (X y O)
def dibujar_piezas():
    for i in range(9):
        x = (i % 3) * 200 + 100
        y = (i // 3) * 200 + 100
        if tablero[i] == "X":
            pygame.draw.line(pantalla, ROJO, (x - 50, y - 50), (x + 50, y + 50), 10)
            pygame.draw.line(pantalla, ROJO, (x + 50, y - 50), (x - 50, y + 50), 10)
        elif tablero[i] == "O":
            pygame.draw.circle(pantalla, AZUL, (x, y), 60, 10)

# Verificar si hay un ganador
def verificar_ganador():
    combinaciones_ganadoras = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontales
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Verticales
        (0, 4, 8), (2, 4, 6)  # Diagonales
    ]
    
    for combo in combinaciones_ganadoras:
        a, b, c = combo
        if tablero[a] == tablero[b] == tablero[c] and tablero[a] != "":
            return tablero[a]
    return None

# Dibujar los botones para seleccionar el jugador que empieza
def dibujar_botones():
    fuente = pygame.font.Font(None, 60) # (None, 74)
    texto = fuente.render("EEST Nº3   Eva Perón", True, AZUL)
    pantalla.blit(texto, (45, 30)) #(col150,fil100)

    fuente = pygame.font.Font(None, 40) # (None, 74)
    texto_2 = fuente.render("Maquinista Savio", True, NEGRO)
    pantalla.blit(texto_2, (40, 100)) #(col150,fil100)
    
    fuente = pygame.font.Font(None, 40) # (None, 74)
    texto1 = fuente.render("¿Quién empieza?", True, NEGRO)
    pantalla.blit(texto1, (100, 180)) #(150,100)

    
    # Botón para X
    fuente = pygame.font.Font(None, 120) # (None, 74)
    pygame.draw.rect(pantalla, GRIS_CLARO, (148, 245, 109, 105))   #(izq140, Sup250, der104, inf110) 
    texto_x = fuente.render("X", True, ROJO)
    pantalla.blit(texto_x, (175, 260))
    
    # Botón para O
    pygame.draw.rect(pantalla, GRIS_CLARO, (350, 243, 113, 107))
    texto_o = fuente.render("O", True, AZUL)
    pantalla.blit(texto_o, (375, 260))

# Dibujar el botón de reiniciar
def dibujar_boton_reiniciar():
    fuente = pygame.font.Font(None, 50)
    pygame.draw.rect(pantalla, GRIS_CLARO, (200, 500, 200, 60))
    texto_reiniciar = fuente.render("Reiniciar", True, NEGRO)
    pantalla.blit(texto_reiniciar, (215, 510))

# Mostrar el cartel de ganador (más llamativo)
def mostrar_cartel_ganador(ganador):
    global senial_ganador
    fuente = pygame.font.Font(None, 50)  # Tamaño de la frase
    texto_ganador = f"¡Ganaste:    {ganador}!"
    if senial_ganador: 
        arduino.write(b'1')  #COMPUNICACION POR EL PUERTO SERIE
        senial_ganador=False        
        sonido_ganador.set_volume(0.4)  # Ajusta el volumen al 50% 
        sonido_ganador.play()  # Reproducir sonido ganador
    
    # Dibujar un rectángulo de fondo para el cartel de ganador
    pygame.draw.rect(pantalla, BLANCO, (150, 130, 400, 80), border_radius=20) #Izq,superior,der,inferior
    
    # Mostrar el texto del ganador en grande y centrado
    texto_render = fuente.render(texto_ganador, True, NEGRO)
    pantalla.blit(texto_render, (200, 150))  #Ubicacion de frase CARTEL GANADOR (columna, fila)(230, 160)

# Mostrar el menú de selección de jugador
def elegir_quien_empieza():
    global turno
    seleccionando = True
    while seleccionando:
        pantalla.fill(GRIS_CLARO)  #Color de Pantalla Principal
        dibujar_botones()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Verificar si hizo clic en el botón de "X"
                if 150 <= x <= 250 and 250 <= y <= 350:
                    turno = "X"
                    seleccionando = False
                # Verificar si hizo clic en el botón de "O"
                elif 350 <= x <= 450 and 250 <= y <= 350:
                    turno = "O"
                    seleccionando = False

# Reiniciar el juego
def reiniciar_juego():
    global tablero, turno, fin_juego, ganador, senial_ganador
    tablero = [""] * 9
    turno = None
    fin_juego = False
    ganador = None
    pantalla.fill(VERDE_CLARO)
    arduino.write(b'0')   #COMUNICACION POR EL PUERTO SERIE
    senial_ganador=True    
    elegir_quien_empieza()


# Loop principal del juego
elegir_quien_empieza()

while True:
    pantalla.fill(VERDE_CLARO)  #Color de cuadrícula de juego
    dibujar_tablero()
    dibujar_piezas()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not fin_juego:
            x, y = pygame.mouse.get_pos()
            fila = y // 200
            columna = x // 200
            indice = fila * 3 + columna

            if tablero[indice] == "":
                tablero[indice] = turno
                turno = "O" if turno == "X" else "X"
                sonido_click.play()  # Reproducir sonido al hacer clic
                ganador = verificar_ganador()
                if ganador or "" not in tablero:
                    fin_juego = True

        if event.type == pygame.MOUSEBUTTONDOWN and fin_juego:
            x, y = pygame.mouse.get_pos()
            # Verificar si hizo clic en el botón de "Reiniciar"
            if 200 <= x <= 400 and 500 <= y <= 560:
                reiniciar_juego()

    if fin_juego:
        if ganador:            
            mostrar_cartel_ganador(ganador)  # Mostrar el cartel de ganador con el nuevo diseño
        else:
            fuente = pygame.font.Font(None, 74)
            texto = fuente.render("Empate", True, NEGRO)
            pantalla.blit(texto, (220, 250))

        dibujar_boton_reiniciar()

    pygame.display.update()