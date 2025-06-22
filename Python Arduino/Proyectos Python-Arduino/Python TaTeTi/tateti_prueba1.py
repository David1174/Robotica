import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir los colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

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

# Mostrar el menú de selección de jugador
def elegir_quien_empieza():
    global turno
    pantalla.fill(BLANCO)
    fuente = pygame.font.Font(None, 74)
    texto1 = fuente.render("¿Quién empieza?", True, NEGRO)
    texto2 = fuente.render("Presiona X o O", True, NEGRO)
    pantalla.blit(texto1, (100, 200))
    pantalla.blit(texto2, (100, 300))
    pygame.display.update()

    seleccionando = True
    while seleccionando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    turno = "X"
                    seleccionando = False
                elif event.key == pygame.K_o:
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

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reiniciar_juego()

    if fin_juego:
        fuente = pygame.font.Font(None, 74)
        if ganador:
            texto = fuente.render(f"Ganador: {ganador}", True, NEGRO)
        else:
            texto = fuente.render("Empate", True, NEGRO)
        pantalla.blit(texto, (150, 250))

    pygame.display.update()