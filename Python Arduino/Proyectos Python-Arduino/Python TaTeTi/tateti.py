import tkinter as tk
import pygame
from tkinter import messagebox

pygame.mixer.init()

channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)

melodia1 = pygame.mixer.Sound("prueba.wav")
melodia2 = pygame.mixer.Sound("Message 1.mp3")
melodia3 = pygame.mixer.Sound("Mechanical.mp3")
# pygame.mixer.music.load("Message 1.mp3")

class TicTacToe:
  
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.current_player = "X"
        self.board = [[None for _ in range(3)] for _ in range(3)]
        
        self.create_widgets()
        
    def create_widgets(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=('normal', 40), width=8, height=3,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
    
    def on_button_click(self, row, col):
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner():
                #pygame.mixer.music.play()
                channel3.stop()
                channel1.play(melodia1)
                channel2.play(melodia2)
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} Ganaste !!")                
                self.reset_game()
                channel3.play(melodia3)
            elif all(self.board[row][col] is not None for row in range(3) for col in range(3)):
                
                messagebox.showinfo("Tic Tac Toe", "Empate")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] and self.board[row][0] is not None:
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] is not None:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return True
        return False
    
    def reset_game(self):
        self.current_player = "X"
        self.board = [[None for _ in range(4)] for _ in range(4)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    channel3.play(melodia3)
    game = TicTacToe(root)
    
    root.mainloop()