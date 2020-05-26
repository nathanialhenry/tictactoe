# TODO smarter AI

import random

# Tic Tac board template
template_list = ['_|','_','|_',
                 '_|','_','|_',
                 '_|','_','|_ ']

icon = ''
win = False
prev_entry = []
pos_moves = [1,2,3,4,5,6,7,8,9]

# Explains rules and gets player's icon
def startup():
    global icon
    print('TIC TAC TOE \nRules: Enter a value between 1 and 9 to determine which space you would like to place your X or O\n'
        + 'The first player to get three of their icons in a row, wins the game')
    displayboard()
    icon = input('Please select X or O as your icon:')
    # defines accepted inputs
    while icon.lower() != 'x' and icon.lower() != 'o':
        icon = input('Please select X or O as your icon:')
    return icon

# displays board based on the template above
def displayboard():
    print(template_list[0], template_list[1], template_list[2])
    print(template_list[3], template_list[4], template_list[5])
    print(template_list[6], template_list[7], template_list[8])

# makes it not possible to enter the same value by tracking entries and removing the from possible moves list
def nodupes():
    for pos in prev_entry:
        if pos in pos_moves:
            pos_moves.remove(pos)

# uses random choice to determine next ai move (TODO use sets to determine next move, else random)
def aiplay():
    nodupes()
    ai_choice = random.choice(pos_moves)
    if icon == 'x':
        ai_icon = 'o'
    else:
        ai_icon = 'x'
    return enterpos(ai_choice, ai_icon)

# enters the ai/player entry onto board while maintaining the board's look
def enterpos(p_input, icon):
    left_row = [1, 4, 7]
    right_row = [3, 6, 9]
    prev_entry.append(p_input)
    if p_input in left_row:
        template_list[p_input - 1] = icon + '|'
    elif p_input in right_row:
        template_list[p_input - 1] = '|' + icon  
    else:
        template_list[p_input - 1] = icon
    return template_list[p_input -1]


def wincondition():
    global win
    x = []
    o = []

    # gets list of x positions and o positions on the board
    for index,spot in enumerate(template_list):
        if 'x' in spot:
            x.append(index)
        if 'o' in spot:
            o.append(index)

    # if any of the win conditions are met in the lists, a winner is declared
    if any( [set([0,1,2]).issubset(set(x)), set([3,4,5]).issubset(set(x)), set([6,7,8]).issubset(set(x)), set([0,3,6]).issubset(set(x)), 
         set([1,4,7]).issubset(set(x)), set([2,5,8]).issubset(set(x)), set([0,4,8]).issubset(set(x)), set([2,4,6]).issubset(set(x))]):
        win = True
        print('X WINS!!!!!!!!!')
        return
    
    if any([set([0,1,2]).issubset(set(o)), set([3,4,5]).issubset(set(o)), set([6,7,8]).issubset(set(o)), set([0,3,6]).issubset(set(o)), 
         set([1,4,7]).issubset(set(o)), set([2,5,8]).issubset(set(o)), set([0,4,8]).issubset(set(o)), set([2,4,6]).issubset(set(o))]):
        win = True
        print('O WINS!!!!!!!!')
        return 

# main play function
def play(icon):
    afterfirstround = 0
    while win == False:
        # only runs on the first round, and determines who goes first
        if not afterfirstround:
            gofirst = random.choice([1,0])
            if gofirst:
                print('AI goes first')
                aiplay()
                displayboard()
            else:
                print('USER goes first')
                displayboard()
        
        try:
            nodupes()
            # determines if stalemate conditions are met
            if not pos_moves:
                print('STALEMATE: There are no more possible moves')
                break
            # gets player input for their next move
            player_input = int(input('Enter position value: '))
        except:
            print('Please enter a value between 1 and 9, that has not already been selected:')
            continue
        # makes sure player input is a valid entry
        while player_input <1 or player_input > 9 or player_input in prev_entry:
            player_input = int(input('Please enter a value between 1 and 9, that has not already been selected:'))

        player_input = int(player_input)
        # enters player's position on the board
        enterpos(player_input, icon)
        # shows board to player with their recent input
        displayboard()
        # runs to determine if win condition was met by player's recent input
        wincondition()

        if win == True:
            break
        print ("AI's Turn...")

        if not pos_moves:
            print('STALEMATE: There are no more possible moves')
            break
        # runs AI's turn
        aiplay()
        # displays AI's input
        displayboard()
        # determines if AI meets win condition based on recent input
        wincondition()
        afterfirstround +=1

startup()
play(icon)
input('press Enter to end')