from tkinter import *
from tkinter.messagebox import showinfo
import time
root = Tk()
root.title('PLAYER1 ATTACK HERE               PLAYER2 ATTACK HERE')
v = 0
game_button_P1 = []
game_button_P2 = []
a = [['', '', '', '', '', '', ''],
     ['', '', '', '', '', '', ''],
     ['', '', '', '', '', '', ''],
     ['', '', '', '', '', '', ''],
     ['', '', '', '', '', '', ''],
     ['', '', '', '', '', '', ''],
     ['', '', '', '', '', '', '']]
b = [['', '', '', '', '', '', ''],
     ['', '', '', '', '', '', ''],
     ['', '', '', '', '', '', ''],
     ['', '', '', '', '', '', ''],
     ['', '', '', '', '', '', ''],
     ['', '', '', '', '', '', ''],
     ['', '', '', '', '', '', '']]


def create_Grid(k, game_button, player_name):
    root = Tk()
    root.title(player_name)
    u = k
    for i in range(7):
        game_button.append(list())
        for j in range(7):
            game_button[i].append(Button(root, text="", width=1,
                                         command=lambda row=i, col=j:
                                         createShip(row, col, u, game_button)))
            game_button[i][j].grid(row=i, column=j)
    orientation_btn = Button(root, text='V', width=1,
                             command=lambda: modifyOrientation())
    orientation_btn2 = Button(
        root, text='H', width=1, command=lambda: modifyOrientation1())
    orientation_btn.grid(column=2, row=10)
    orientation_btn2.grid(column=4, row=10)


def buttons_counter(button_list):
    counter = 0
    for i in button_list:
        for j in i:
            if j == 'H':
                counter += 1
    return counter


def winner(Player):
    counter_winner = 0
    if Player == 'Player1':
        for i in game_button_P1:
            for j in i:
                if j['bg'] == 'red':
                    counter_winner += 1
                    print('counter p1', counter_winner)
    elif Player == 'Player2':
        for i in game_button_P2:
            for j in i:
                if j['bg'] == 'red':
                    counter_winner += 1
                    print('counnter p2', counter_winner)
    return counter_winner


def createShip(x, y, u, button_list):
    global v
    if buttons_counter(u) < 9:
        if v == 1:
            if x == 0 or x == 6:
                showinfo("Try again", "Out of border")
            elif button_list[x + 1][y]['bg'] == 'black' or button_list[x - 1][y]['bg'] == 'black':
                showinfo("Try again", "Out of border")
            else:
                button_list[x][y]['bg'] = 'black'
                button_list[x+1][y]['bg'] = 'black'
                button_list[x-1][y]['bg'] = 'black'
                u[x][y] = 'H'
                u[x + 1][y] = 'H'
                u[x-1][y] = 'H'
                print(x, y)
                print(u)
                print(v)
        elif v == 0:
            if y == 0 or y == 6:
                showinfo("Try again", "Out of border")
            elif button_list[x][y+1]['bg'] == 'black' or button_list[x][y-1]['bg'] == 'black':
                showinfo("Try again", "Out of border")
            else:
                button_list[x][y]['bg'] = 'black'
                button_list[x][y+1]['bg'] = 'black'
                button_list[x][y-1]['bg'] = 'black'
                u[x][y] = 'H'
                u[x][y+1] = 'H'
                u[x][y-1] = 'H'
                print(x, y)
                print(u)
                print(v)
        print(buttons_counter(u))
    else:
        print('.................')


def modifyOrientation():
    global v
    v = 1
    print(v)
    return v


def modifyOrientation1():
    global v
    v = 0
    print(v)
    return v


turn = 0


def hit_or_miss(x, y, player):
    global turn
    if turn == 0:
        if player == 'Player1':
            if a[x][y] == 'H':
                game_button_P1[x][y]['bg'] = 'red'
                turn = 1
            else:
                game_button_P1[x][y]['bg'] = 'blue'
                turn = 1
        if winner('Player1') == 9:
            showinfo("Battleship", "Player 1 win")
            print('P1 WIN')
    if turn == 1:
        if player == 'Player2':
            if b[x][y] == 'H':
                game_button_P2[x][y]['bg'] = 'red'
                turn = 0
            else:
                game_button_P2[x][y]['bg'] = 'blue'
                turn = 0
        if winner('Player2') == 9:
            showinfo("Battleship", "Player 2 win")
            print('P2 WIN')


def attack_phase(int, player):

    if player == 'Player1':
        for i in range(7):
            game_button_P1.append(list())
            for j in range(7):
                game_button_P1[i].append(Button(
                    root, text="", width=1, command=lambda row=i, column=j: hit_or_miss(row, column, 'Player1')))
                game_button_P1[i][j].grid(row=i, column=j + int)
    elif player == 'Player2':
        for i in range(7):
            game_button_P2.append(list())
            for j in range(7):
                game_button_P2[i].append(Button(
                    root, text="", width=1, command=lambda row=i, column=j: hit_or_miss(row, column, 'Player2')))
                game_button_P2[i][j].grid(row=i, column=j + int)


def middle_board_space(str, int):
    for _ in range(10):
        Label(root, text=str, bg='grey').grid(row=2, column=int)


attack_phase(0, 'Player1')
middle_board_space("  ", 8)
attack_phase(30, 'Player2')
create_Grid(a, [], 'PLAYER2')
create_Grid(b, [], 'PLAYER1')
root.mainloop()
