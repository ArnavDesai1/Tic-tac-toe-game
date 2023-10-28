import tkinter as tk
from tkinter import messagebox

# Initialize the game board
board = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}

# Initialize player info
player_info = {'player_turn': 'X', 'moves': 0}

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("300x400")  # Set the size of the main window

# Define colors
bg_color = "#f0f0f0"  # Background color
button_bg = "#e0e0e0"  # Button background color
button_fg = "#000000"  # Button text color
label_color = "#ff0000"  # Color for X and O labels
label_font_size = 12  # Font size for X and O labels
number_font_size = 16  # Font size for numbers

# Function to handle a player's move
def play(position):
    if board[position] == ' ':
        player_turn = player_info['player_turn']
        board[position] = player_turn
        update_game_board()  # Update the game board
        winner, win_combo = check_winner()

        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins with {' ,'.join(win_combo)}!")
            clear_board()
            menu_frame.pack()  # Display the menu
            game_frame.pack_forget()  # Hide the game board
        else:
            player_info['player_turn'] = 'X' if player_turn == 'O' else 'O'
            player_info['moves'] += 1

            if player_info['moves'] == 9:  # Check for a draw when all squares are filled
                if not winner:
                    messagebox.showinfo("Game Over", "It's a draw!")
                    clear_board()
                    menu_frame.pack()  # Display the menu
                    game_frame.pack_forget()  # Hide the game board

# Function to check for a winner
def check_winner():
    winning_combinations = [
        ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
        ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
        ['1', '5', '9'], ['3', '5', '7']
    ]
    for player in ('X', 'O'):
        for combo in winning_combinations:
            if all(board[position] == player for position in combo):
                return player, combo  # Return the winning player and combination
    return None, None  # No winner

# Function to update the game board
def update_game_board():
    for i in range(1, 10):
        buttons[i].config(text=board[str(i)])
        if board[str(i)] != ' ':
            labels[i].config(font=("Arial", label_font_size), fg=label_color)  # Adjust label size and color
            buttons[i].config(state=tk.DISABLED)  # Disable buttons after being clicked

# Function to clear the game board
def clear_board():
    for position in board:
        board[position] = ' '

    update_game_board()
    player_info['moves'] = 0  # Reset the move count
    for i in range(1, 10):
        buttons[i].config(state=tk.NORMAL)  # Re-enable buttons

# Function to reset the game board
def reset_board():
    for position in board:
        board[position] = ' '

# Function to start a new game
def new_game():
    reset_board()
    update_game_board()

    # Display the game board
    game_frame.pack()
    menu_frame.pack_forget()  # Hide the menu

# Function to quit the game
def quit_game():
    root.destroy()

# Create the menu frame
menu_frame = tk.Frame(root, bg=bg_color)
menu_frame.pack(expand=True)

# Create a button frame for menu buttons
button_frame = tk.Frame(menu_frame, bg=bg_color)
button_frame.pack(pady=20)  # Add padding to the button frame

# Create "New Game" button in the button frame
new_game_button = tk.Button(button_frame, text="New Game", command=new_game, font=("Arial", 12), width=10, height=2, bg=button_bg, fg=button_fg)
new_game_button.pack(side=tk.LEFT, padx=10)  # Add padding

# Create "Quit" button in the button frame
quit_button = tk.Button(button_frame, text="Quit", command=quit_game, font=("Arial", 12), width=10, height=2, bg=button_bg, fg=button_fg)
quit_button.pack(side=tk.RIGHT, padx=10)  # Add padding

# Create the game board frame
game_frame = tk.Frame(root, bg=bg_color)

buttons = {}
labels = {}  # Store labels for displaying numbers inside squares
for i in range(1, 10):
    buttons[i] = tk.Button(game_frame, text=' ', font=('Arial', 24), width=5, height=2, bg=button_bg, fg=button_fg,
                          command=lambda i=i: play(str(i))
                          )
    buttons[i].grid(row=(i - 1) // 3, column=(i - 1) % 3)
    
    # Add labels to display numbers in the squares
    labels[i] = tk.Label(buttons[i], text=str(i), font=("Arial", number_font_size), fg=label_color)
    labels[i].place(x=5, y=5)

# Initially hide the game board
game_frame.pack_forget()

root.mainloop()
