import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"  # X starts
        self.board = [""] * 9      # 3x3 grid as a flat list
        self.buttons = []          # To store button references
        
        # Create the game grid
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text="", font=('Arial', 20), width=5, height=2,
                                 command=lambda row=i, col=j: self.button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)
        
        # Reset button
        reset_button = tk.Button(self.window, text="Reset", font=('Arial', 12),
                               command=self.reset_game)
        reset_button.grid(row=3, column=1, pady=10)
        
        self.window.mainloop()

    def button_click(self, row, col):
        # Calculate the index in the flat board list
        index = row * 3 + col
        
        # Check if the spot is empty
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            
            # Check for a winner
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.disable_buttons()
            else:
                # Switch players
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != "":
                return True
        
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != "":
                return True
        
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != "":
            return True
        if self.board[2] == self.board[4] == self.board[6] != "":
            return True
        
        return False

    def disable_buttons(self):
        # Disable all buttons after game ends
        for button in self.buttons:
            button.config(state="disabled")

    def reset_game(self):
        # Reset the game state
        self.current_player = "X"
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="", state="normal")

if __name__ == "__main__":
    game = TicTacToe()