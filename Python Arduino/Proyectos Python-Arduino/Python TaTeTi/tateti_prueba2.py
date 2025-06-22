import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir los colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
GRIS_CLARO = (200, 200, 200)

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
    texto1 = fuente.render("¿Quién empieza?", True, NEGRO)
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

# Reiniciar el juego
def reiniciar_juego():
    global tablero, turno, fin_juego, ganador
    tablero = [""] * 9
    turno = None
    fin_juego = False
    ganador = None
    pantalla.fill(BLANCO)
    elegir_quien_empieza()

# Loop principal del juego
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
                ganador = verificar_ganador()
                if ganador or "" not in tablero:
                    fin_juego = True

        if event.type == pygame.MOUSEBUTTONDOWN and fin_juego:
            x, y = pygame.mouse.get_pos()
            # Verificar si hizo clic en el botón de "Reiniciar"
            if 200 <= x <= 400 and 500 <= y <= 560:
                reiniciar_juego()

    if fin_juego:
        fuente = pygame.font.Font(None, 74)
        if ganador:
            texto = fuente.render(f"Ganador: {ganador}", True, NEGRO)
        else:
            texto = fuente.render("Empate", True, NEGRO)
        pantalla.blit(texto, (150, 250))

        dibujar_boton_reiniciar()

    pygame.display.update()