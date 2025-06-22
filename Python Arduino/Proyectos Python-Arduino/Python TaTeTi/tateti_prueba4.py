import pygame
import sys
import serial
import time

# Configurar la conexión serial (ajusta el puerto según sea necesario)
arduino = serial.Serial('COM7', 9600, timeout=1)
time.sleep(2)  # Dar tiempo al Arduino para inicializar

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("Techno.mp3")
pygame.mixer.music.play()

# Cargar efectos de sonido
sonido_click = pygame.mixer.Sound("mouse2.mp3")  # Sonido al hacer clic
sonido_ganador = pygame.mixer.Sound("winning.mp3")  # Sonido al ganar
sonido_empate = pygame.mixer.Sound("Empate.mp3")  # Sonido al empatar


# Definir los colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
GRIS_CLARO = (200, 200, 200)
VERDE_CLARO = (144, 238, 144)

# Configurar el tamaño de la pantalla
ANCHO = 600
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Configurar el título
pygame.display.set_caption("Tateti - Tres en Línea")

# Definir el tablero (una lista de 9 elementos vacíos)
tablero = [""] * 9

# Definir algunas variables del juego
turno = None  # El primer jugador será definido por el usuario
fin_juego = False
ganador = None
nombre_x = ""
nombre_o = ""
ingresando_nombres = True

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
    fuente = pygame.font.Font(None, 74)
    texto1 = fuente.render("¿Inicia Jagada?:", True, NEGRO)
    pantalla.blit(texto1, (150, 100))
    
    # Botón para X
    pygame.draw.rect(pantalla, GRIS_CLARO, (150, 250, 100, 100))
    texto_x = fuente.render("X", True, ROJO)
    pantalla.blit(texto_x, (175, 260))
    
    # Botón para O
    pygame.draw.rect(pantalla, GRIS_CLARO, (350, 250, 100, 100))
    texto_o = fuente.render("O", True, AZUL)
    pantalla.blit(texto_o, (375, 260))

# Dibujar el botón de reiniciar
def dibujar_boton_reiniciar():
    fuente = pygame.font.Font(None, 50)
    pygame.draw.rect(pantalla, GRIS_CLARO, (200, 500, 200, 60))
    texto_reiniciar = fuente.render("Reiniciar", True, NEGRO)
    pantalla.blit(texto_reiniciar, (215, 510))



#def juego_de_luces():
    #arduino.write(b'1')



# Mostrar el cartel de ganador (más llamativo)
def mostrar_cartel_ganador(ganador):    
    fuente = pygame.font.Font(None, 74)
    texto_ganador = f"¡Ganaste {nombre_x if ganador == 'X' else nombre_o}!"
    #juego_de_luces()
    arduino.write(b'1')
    sonido_ganador.set_volume(0.05)  # Ajusta el volumen al 50%
    sonido_ganador.play()  # Reproducir sonido ganador
    pygame.mixer.music.stop()
    
    # Dibujar un rectángulo de fondo para el cartel de ganador
    pygame.draw.rect(pantalla, VERDE_CLARO, (50, 200, 500, 200), border_radius=20)
    
    # Mostrar el texto del ganador en grande y centrado
    
    texto_render = fuente.render(texto_ganador, True, NEGRO)
    pantalla.blit(texto_render, (80, 260))
    


# Mostrar el cartel de empate(más llamativo)
def mostrar_cartel_empate():
    fuente = pygame.font.Font(None, 74)
    texto_empate = f"¡Empate!"
    pygame.mixer.music.stop()
    sonido_empate.set_volume(0.05)
    sonido_empate.play()
    # Dibujar un rectángulo de fondo para el cartel empate
    pygame.draw.rect(pantalla, VERDE_CLARO, (50, 200, 500, 200), border_radius=20)
    
    # Mostrar el texto de empate grande y centrado
    texto_render = fuente.render(texto_empate, True, NEGRO)
    pantalla.blit(texto_render, (200, 260))    

# Dibujar el cuadro de entrada de nombres
def dibujar_cuadro_entrada(texto, posicion):
    fuente = pygame.font.Font(None, 50)
    entrada = fuente.render(texto, True, NEGRO)
    pantalla.blit(entrada, posicion)

# Reiniciar el juego
def reiniciar_juego(): 
    #arduino.write(b'0') #Apaga las luces
    tablero = [""] * 9
    turno = None
    fin_juego = False
    ganador = None
    pantalla.fill(BLANCO)
    elegir_quien_empieza()
    sonido_ganador.stop()
    sonido_empate.stop()


# Mostrar el menú de selección de jugador
def elegir_quien_empieza():
    global turno
    seleccionando = True
    while seleccionando:
        pantalla.fill(BLANCO)
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

# Solicitar nombres de los jugadores
def solicitar_nombres():
    global nombre_x, nombre_o, ingresando_nombres
    nombre_actual = ""
    activo_x = True

    while ingresando_nombres:
        pantalla.fill(BLANCO)
        fuente = pygame.font.Font(None, 50)
        
        # Mostrar instrucciones
        texto_instruccion = fuente.render("Ingresa nombre del jugador X:", True, NEGRO) if activo_x else fuente.render("Ingresa nombre del jugador O:", True, NEGRO)
        pantalla.blit(texto_instruccion, (50, 100))
        
        # Mostrar el nombre que se está escribiendo
        dibujar_cuadro_entrada(nombre_actual, (50, 200))
                
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    nombre_actual = nombre_actual[:-1]
                elif event.key == pygame.K_RETURN:
                    if activo_x:
                        nombre_x = nombre_actual
                        nombre_actual = ""
                        activo_x = False
                    else:
                        nombre_o = nombre_actual
                        ingresando_nombres = False
                else:
                    nombre_actual += event.unicode

# Loop principal del juego
solicitar_nombres()
elegir_quien_empieza()

while True:
    pantalla.fill(BLANCO)
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
            if 200 <= x <= 400 and 500 <= y <= 560:
                reiniciar_juego()
                pygame.mixer.music.play()
                

  
    if ganador:
        mostrar_cartel_ganador(ganador)
        dibujar_boton_reiniciar()
    elif "" not in tablero:        
        mostrar_cartel_empate()
        dibujar_boton_reiniciar()

    pygame.display.update()
