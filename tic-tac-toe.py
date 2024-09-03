import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.current_player = 'X'
        self.game_board = [['', '', ''], ['', '', ''], ['', '', '']]
        
        # Create the main window
        self.root = tk.Tk()
        self.root.title('Tic Tac Toe')
        
        # Create the buttons
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.root, text='', font=('Arial', 50), width=4, height=2, command=lambda row=row, col=col: self.button_click(row, col))
                button.grid(row=row, column=col, sticky='nsew')
                button_row.append(button)
            self.buttons.append(button_row)
        
        # Create the menu
        menu_bar = tk.Menu(self.root)
        game_menu = tk.Menu(menu_bar, tearoff=0)
        game_menu.add_command(label='New Game', command=self.new_game)
        game_menu.add_separator()
        game_menu.add_command(label='Exit', command=self.root.quit)
        menu_bar.add_cascade(label='Game', menu=game_menu)
        self.root.config(menu=menu_bar)
        
        # Start the main loop
        self.root.mainloop()
        
    def button_click(self, row, col):
        if self.game_board[row][col] == '':
            self.game_board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_win():
                messagebox.showinfo('Tic Tac Toe', f'{self.current_player} wins!')
                self.new_game()
            elif self.check_tie():
                messagebox.showinfo('Tic Tac Toe', 'Tie game!')
                self.new_game()
            else:
                self.switch_player()
    
    def check_win(self):
        # Check rows
        for row in range(3):
            if self.game_board[row][0] == self.game_board[row][1] == self.game_board[row][2] != '':
                return True
        # Check columns
        for col in range(3):
            if self.game_board[0][col] == self.game_board[1][col] == self.game_board[2][col] != '':
                return True
        # Check diagonals
        if self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] != '':
            return True
        if self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] != '':
            return True
        return False
    
    def check_tie(self):
        for row in range(3):
            for col in range(3):
                if self.game_board[row][col] == '':
                    return False
        return True
    
    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
    
    def new_game(self):
        self.current_player = 'X'
        self.game_board = [['', '', ''], ['', '', ''], ['', '', '']]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text='')


# Start the game
if __name__ == '__main__':
    TicTacToe()
