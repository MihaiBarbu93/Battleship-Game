import tkinter as Tk
from tkinter import *
from tkinter.messagebox import showinfo
root = Tk()
root.title('PLAYER1 ATTACK HERE               PLAYER2 ATTACK HERE')
root1 = Tk()
root1.title('Player1')
root2 = Tk()
root2.title('Player2')
vertical = 0
turn = 0
attack_phase_buttons_P1 = []
attack_phase_buttons_P2 = []
Player1 = [['', '', '', '', '', '', ''],
           ['', '', '', '', '', '', ''],
           ['', '', '', '', '', '', ''],
           ['', '', '', '', '', '', ''],
           ['', '', '', '', '', '', ''],
           ['', '', '', '', '', '', ''],
           ['', '', '', '', '', '', '']]
Player2 = [['', '', '', '', '', '', ''],
           ['', '', '', '', '', '', ''],
           ['', '', '', '', '', '', ''],
           ['', '', '', '', '', '', ''],
           ['', '', '', '', '', '', ''],
           ['', '', '', '', '', '', ''],
           ['', '', '', '', '', '', '']]


# Create a 7x7 placement table
def create_Grid(k, game_button, root_name):
    u = k
    for i in range(7):
        game_button.append(list())
        for j in range(7):
            game_button[i].append(Button(root_name, text="", width=1,
                                         command=lambda row=i, col=j:
                                         createShip(row, col, u, game_button, root_name)))
            game_button[i][j].grid(row=i, column=j)
    orientation_btn = Button(root_name, text='V', width=1,
                             command=lambda: modifyOrientationToVert())
    orientation_btn2 = Button(
        root_name, text='H', width=1, command=lambda: modifyOrientationToHor())
    orientation_btn.grid(column=2, row=10)
    orientation_btn2.grid(column=4, row=10)
    root.withdraw()


# Count the number of ships placed
def ships_counter(player_list):
    counter = 0
    for i in player_list:
        for j in i:
            if j == 'H':
                counter += 1
    return counter


# Check the number of discovered ships in attack phase
def check_winner(Player):
    counter_winner = 0
    if Player == 'Player1':
        for i in attack_phase_buttons_P1:
            for j in i:
                if j['bg'] == 'black':
                    counter_winner += 1
    elif Player == 'Player2':
        for i in attack_phase_buttons_P2:
            for j in i:
                if j['bg'] == 'black':
                    counter_winner += 1
    return counter_winner


# Create a 3 square ship on horizontal or vertical orientation by selecting orientation and the middle of ship
def createShip(x, y, player_list, button_list, root_name):
    global v
    if ships_counter(player_list) < 9:
        if vertical == 1:
            if x == 0 or x == 6:
                showinfo("Try again", "Out of border")
            elif button_list[x + 1][y]['bg'] == 'black' or button_list[x - 1][y]['bg'] == 'black':
                showinfo("Try again", "Overlaid Ships")
            else:
                button_list[x][y]['bg'] = 'black'
                button_list[x+1][y]['bg'] = 'black'
                button_list[x-1][y]['bg'] = 'black'
                player_list[x][y] = 'H'
                player_list[x + 1][y] = 'H'
                player_list[x-1][y] = 'H'
        elif vertical == 0:
            if y == 0 or y == 6:
                showinfo("Try again", "Out of border")
            elif button_list[x][y+1]['bg'] == 'black' or button_list[x][y-1]['bg'] == 'black':
                showinfo("Try again", "Overlaid Ships")
            else:
                button_list[x][y]['bg'] = 'black'
                button_list[x][y+1]['bg'] = 'black'
                button_list[x][y-1]['bg'] = 'black'
                player_list[x][y] = 'H'
                player_list[x][y+1] = 'H'
                player_list[x][y-1] = 'H'
    else:
        root_name.destroy()
    if root_name == root2 and ships_counter(player_list) >= 9:
        root.deiconify()


def modifyOrientationToVert():
    global vertical
    vertical = 1
    return vertical


def modifyOrientationToHor():
    global vertical
    vertical = 0
    return vertical


# Check if selected button in attack phase hits a piece of ship or not
def hit_or_miss(x, y, player):
    global turn
    if turn == 0:
        if player == 'Player1':
            if Player1[x][y] == 'H':
                attack_phase_buttons_P1[x][y]['bg'] = 'black'
                turn = 1
            else:
                attack_phase_buttons_P1[x][y]['bg'] = 'red'
                turn = 1
        if check_winner('Player1') == 9:
            showinfo("Battleship", "Player 1 win")
            root.destroy()
            root1.destroy()
            root2.destroy()
    if turn == 1:
        if player == 'Player2':
            if Player2[x][y] == 'H':
                attack_phase_buttons_P2[x][y]['bg'] = 'black'
                turn = 0
            else:
                attack_phase_buttons_P2[x][y]['bg'] = 'red'
                turn = 0
        if check_winner('Player2') == 9:
            showinfo("Battleship", "Player 2 win")
            root.destroy()
            root1.destroy()
            root2.destroy()


# Create 2 7x7 tables for attack phase
def attack_phase(int, player):
    if player == 'Player1':
        for i in range(7):
            attack_phase_buttons_P1.append(list())
            for j in range(7):
                attack_phase_buttons_P1[i].append(Button(
                    root, text="", width=1, command=lambda row=i, column=j: hit_or_miss(row, column, 'Player1')))
                attack_phase_buttons_P1[i][j].grid(row=i, column=j + int)
    elif player == 'Player2':
        for i in range(7):
            attack_phase_buttons_P2.append(list())
            for j in range(7):
                attack_phase_buttons_P2[i].append(Button(
                    root, text="", width=1, command=lambda row=i, column=j: hit_or_miss(row, column, 'Player2')))
                attack_phase_buttons_P2[i][j].grid(row=i, column=j + int)


# Create a delimiter between the attack phase tables
def middle_board_space(str, int):
    for _ in range(10):
        Label(root, text=str, bg='grey').grid(row=2, column=int)


def main():
    create_Grid(Player1, [], root2)
    create_Grid(Player2, [], root1)
    attack_phase(0, 'Player1')
    middle_board_space("  ", 8)
    attack_phase(30, 'Player2')
    showinfo('NOTES', 'Select orientation of ship before you place it. \n If you hit a piece of ship the button will turn black, if you miss it will turn red.')
    root.mainloop()
    root1.mainloop()
    root2.mainloop()


main()
