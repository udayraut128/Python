import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - GUI")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        self.build_gui()

    def build_gui(self):
        for i in range(9):
            button = tk.Button(
                self.root, text="", font=("Arial", 24), width=5, height=2,
                command=lambda i=i: self.make_move(i)
            )
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        self.reset_button = tk.Button(self.root, text="Restart", font=("Arial", 14), command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def make_move(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.disable_buttons()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state="disabled")

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="", state="normal")

    def check_winner(self):
        combos = [
            (0,1,2), (3,4,5), (6,7,8),  # rows
            (0,3,6), (1,4,7), (2,5,8),  # columns
            (0,4,8), (2,4,6)            # diagonals
        ]
        for a, b, c in combos:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
