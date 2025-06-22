import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Dimensiones de la ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Juego del Ahorcado')

# Fuentes
FONT = pygame.font.SysFont('arial', 40)
SMALL_FONT = pygame.font.SysFont('arial', 30)

# Palabras para el juego
WORDS = ['PYTHON', 'PROGRAMMING', 'COMPUTER', 'KEYBOARD', 'MONITOR', 'PYGAME']

# Escoge una palabra al azar
word = random.choice(WORDS)

# Variables del juego
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6
correct_guesses = ['_' for _ in word]
game_over = False

# Función para dibujar el soporte del ahorcado
def draw_gallows():
    # Dibuja el soporte del ahorcado
    pygame.draw.line(screen, BLACK, (100, 500), (300, 500), 10)  # Base
    pygame.draw.line(screen, BLACK, (200, 500), (200, 100), 10)  # Poste vertical
    pygame.draw.line(screen, BLACK, (200, 100), (400, 100), 10)  # Brazo horizontal
    pygame.draw.line(screen, BLACK, (400, 100), (400, 150), 5)   # Cuerda

# Función para dibujar el ahorcado
def draw_hangman():
    if wrong_guesses >= 1:  # Cabeza
        pygame.draw.circle(screen, BLACK, (400, 200), 50, 5)
    if wrong_guesses >= 2:  # Cuerpo
        pygame.draw.line(screen, BLACK, (400, 250), (400, 350), 5)
    if wrong_guesses >= 3:  # Brazo izquierdo
        pygame.draw.line(screen, BLACK, (400, 275), (350, 325), 5)
    if wrong_guesses >= 4:  # Brazo derecho
        pygame.draw.line(screen, BLACK, (400, 275), (450, 325), 5)
    if wrong_guesses >= 5:  # Pierna izquierda
        pygame.draw.line(screen, BLACK, (400, 350), (350, 450), 5)
    if wrong_guesses >= 6:  # Pierna derecha (juego perdido)
        pygame.draw.line(screen, BLACK, (400, 350), (450, 450), 5)

# Función para mostrar el estado de la palabra
def display_word():
    display = ' '.join(correct_guesses)
    text = FONT.render(display, True, BLACK)
    screen.blit(text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 100))

# Función para manejar el texto en pantalla
def display_message(message):
    text = FONT.render(message, True, RED)
    screen.blit(text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))

# Función principal del juego
def main():
    global wrong_guesses, game_over

    running = True
    while running:
        screen.fill(WHITE)
        draw_gallows()  # Dibuja el soporte del ahorcado
        draw_hangman()  # Dibuja las partes del cuerpo conforme avanza el juego
        display_word()  # Muestra el progreso de la palabra adivinada

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and not game_over:
                letter = pygame.key.name(event.key).upper()
                if letter.isalpha() and len(letter) == 1:  # Solo permitir letras
                    if letter in word and letter not in guessed_letters:
                        # Añadir letra a adivinadas y actualizar palabra correcta
                        guessed_letters.append(letter)
                        for i in range(len(word)):
                            if word[i] == letter:
                                correct_guesses[i] = letter
                    elif letter not in guessed_letters:
                        guessed_letters.append(letter)
                        wrong_guesses += 1

        # Verificar si el jugador ganó o perdió
        if '_' not in correct_guesses:
            game_over = True
            display_message('¡Ganaste!')
        elif wrong_guesses >= max_wrong_guesses:
            game_over = True
            display_message(f'Perdiste! La palabra era {word}')

        pygame.display.update()

if __name__ == '__main__':
    main()
