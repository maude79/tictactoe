#!/usr/bin/python3

#print(
#'''
#Welcome to Tic Tac Toe!\n
#In this game, two players fight to become the first to get 3-in-a-row.\n
#First player starts off by picking his favorite symbol: X or O and entering it into any of the numbered cells in the grid.\n
#A cell cannot be overwritten if it's already been filled with an \'X\' or an \'O\'.\n
#Let the game begin!\n\n
#''')

def get_player_info():
    p1 = input('Player 1, please enter your chosen player symbol, \'X\' or \'O\' :')
    while p1 != 'X' and p1 != 'O':
        p1 = input('Please chose either \'X\' \'O\':')
    p2 = 'O' if p1 == 'X' else 'X'     
    return {'1': p1, '2': p2}


def we_have_a_winner(players, cells):
    return (three_in_a_row(players, cells, 1,4,0) or
            three_in_a_row(players, cells, 4,7,0) or
            three_in_a_row(players, cells, 7,10,0) or
            three_in_a_row(players, cells, 1,8,3) or
            three_in_a_row(players, cells, 2,9,3) or
            three_in_a_row(players, cells, 3,10,3) or
            three_in_a_row(players, cells, 1,10,4) or
            three_in_a_row(players, cells, 3,8,2))

    
def three_in_a_row(players, cells, beg, end, step):
    #val = cells[beg:end] if step == 0 else cells[beg:end:step]
    #print(beg, end, step, val)
    row = set(cells[beg:end]) if step == 0 else set(cells[beg:end:step])
    if len(row) == 1:
        winner_symbol = list(row)
        player_number = None
        for player, symbol in players.items():
            if symbol == winner_symbol[0]:
                player_number = player
        print(f'Congratulations! Player {player_number} wins!')
    return len(row) == 1
    

def board_is_full(cells):
    full = sorted(set(cells)) == ['#','O','X']
    if full:
        print(f'It\'t a draw.')
    return full
        
    
def game_is_on(players, cells):
    #print(sorted(set(cells)))
    return (not we_have_a_winner(players, cells) and not board_is_full(cells))
          

def color(cell_value):
    TRED = '\033[31m' # red text
    TBLU = '\033[34m' # red text
    ENDC = '\033[m'   # reset to the defaults

    if 'X' == cell_value:
        return (TRED + cell_value + ENDC)
    elif 'O' == cell_value:
        return (TBLU + cell_value + ENDC)
    else:
        return cell_value

def print_board(cells):
    #ENDC = '\033[m'   # reset to the defaults
    #print(ENDC)
    board  = {'sep_line':'-'*25, 
              'cell_line': '|' + ' '*7 + '|' + ' '*7 + '|' + ' '*7 + '|',
              'cell_line1': '|' + ' '*3 + color(cells[1]) + ' '*3 + '|' + ' '*3 + color(cells[2]) +
                            ' '*3 + '|' + ' '*3 + color(cells[3]) + ' '*3 + '|',
              'cell_line2': '|' + ' '*3 + color(cells[4]) + ' '*3 + '|' + ' '*3 + color(cells[5]) +
                            ' '*3 + '|' + ' '*3 + color(cells[6]) + ' '*3 + '|',
              'cell_line3': '|' + ' '*3 + color(cells[7]) + ' '*3 + '|' + ' '*3 + color(cells[8]) +
                            ' '*3 + '|' + ' '*3 + color(cells[9]) + ' '*3 + '|'}

    print(board['sep_line'])
    print(board['cell_line'])
    print(board['cell_line1'])
    print(board['cell_line'])
    print(board['sep_line'])
    print(board['cell_line'])
    print(board['cell_line2'])
    print(board['cell_line'])
    print(board['sep_line'])
    print(board['cell_line'])
    print(board['cell_line3'])
    print(board['cell_line'])
    print(board['sep_line'])


def get_player_entry(players, player, cells):
    print_board(cells)
    x = input(f'Player {player} please enter your chosen cell: ')
    x = check_for_digit(x)
    x = check_cell_availability(cells, x)
    cells[int(x)] = players[player]


def check_for_digit(x):
    while not x.isdigit() or not int(x) in range(1,10):
        x = input('Please enter a digit between 1 and 9:')
    return x


def check_cell_availability(cells, x):
    while 'X' in cells[int(x)] or 'O' in cells[int(x)]:
        x = input(f'Cell {x} is already taken, please choose an available cell: ')
        x = check_for_digit(x)    
    return x
    

def play():
    cells = ['#','1','2','3','4','5','6','7','8','9']
    players = get_player_info() 
   
    while game_is_on(players, cells):
        get_player_entry(players, '1', cells)
        if game_is_on(players, cells):
            get_player_entry(players, '2', cells)
        else:
            return
    return

        
is_first_round = True
def start_a_game():
    play_again = False
    if not is_first_round:
        play_again = input('The game has ended, would you like to play another one (y/n)?').lower().startswith('y')

    return is_first_round or play_again

            
while start_a_game():
    print('Start TicTacToe')
    is_first_round = False
    play()
