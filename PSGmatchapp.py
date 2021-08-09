import PySimpleGUI as sg
import board_movement
import random

def main():
    layout = [[sg.Button(size=(4,2), key=(row,col)) for col in range(8)] for row in range(8)]
    layout += [[sg.Button('Show'),sg.Button('Reset'), sg.Button('Cancel')]]
    window = sg.Window('Match App', layout, use_default_focus=False)
    board = {}
    last_pressed= None
    
    for row in range(8):
        for col in range(8):
            board[(row,col)] = ['', random.randint(1,7)]
            
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'Reset':
            for row in range(8):
                for col in range(8):
                    window[(row, col)].update(' ')
                    board[(row,col)] = ['', random.randint(1,7)]
        elif event == 'Show':
            update_board(window, board)
        elif not board[event][0]:
            if last_pressed:
                gamelogic(board, event, last_pressed)
                last_pressed = None
            else:
                last_pressed = event
                board[event][0] = 'd'
        elif board[event][0]:
            last_pressed = None
            board[event][0] = ''
        
        update_board(window, board)
        
    window.close()

def gamelogic(board, event, last_pressed):
    if board_movement.valid_move(last_pressed, event, board):
        board_movement.single_move(last_pressed, event, board)
        board_movement.match_factory(last_pressed, event, board)


def update_board(window, board):
    new_shapes(board)
    for row in range(8):
        for col in range(8):
            img = str(board[(row,col)][1])+board[(row,col)][0]
            window[(row,col)].update(
                image_filename=f'imgs/{img}.png',
                image_subsample=2)
            
def new_shapes(board):
    """generator to gaurantee fixed number of shapes. Refills any
        missing shapes after match removal."""

    #drop all shapes to lowest available slot first
    for x in range(7,-1,-1): 
        for y in range(7,-1,-1):
            if board[(x,y)][1]==0:
                for n in range(x-1,-1,-1):
                    if not board[(n,y)][1]==0:
                        board[(x,y)][1], board[(n,y)][1] \
                            = board[(n,y)][1], board[(x,y)][1]
                        break
                        
    #now fill shapes in from the top down
    for x in range(7,-1,-1):
        for y in range(7,-1,-1):
            if board[(x,y)][1]==0:
                board[(x,y)][1] = random.randint(1,7)


if __name__ == '__main__':
    main()
