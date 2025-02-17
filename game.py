import tkinter as tk
from tkinter import messagebox
import random
import time

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.buttons = []
        self.create_board()
    
    def create_board(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text="", font=("Arial", 24), height=2, width=5,
                                command=lambda row=i, col=j: self.make_move(row, col))
                btn.grid(row=i, column=j)
                self.buttons.append(btn)
    
    def make_move(self, row, col):
        index = row * 3 + col
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
                return
            if "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
                return
            self.current_player = "O" if self.current_player == "X" else "X"
            if self.current_player == "O":
                self.root.after(1000, self.computer_move)  # Delay 1 giây trước khi máy đánh
    
    def computer_move(self):
        available_moves = [i for i in range(9) if self.board[i] == ""]
        if available_moves:
            index = random.choice(available_moves)
            self.board[index] = "O"
            self.buttons[index].config(text="O")
            if self.check_winner():
                messagebox.showinfo("Game Over", "Computer wins!")
                self.reset_board()
                return
            if "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
                return
            self.current_player = "X"
    
    def check_winner(self):
        win_patterns = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for a, b, c in win_patterns:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != "":
                return True
        return False
    
    def reset_board(self):
        self.board = ["" for _ in range(9)]
        for btn in self.buttons:
            btn.config(text="")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
