def valid_move(origin, destination, board):
    """Confirms that move is only one vertical or horizontal space away,
        and that it results in a match"""
    (drow, dcolumn) = destination
    (orow, ocolumn) = origin
    
    if (drow == orow-1 or drow==orow+1) and dcolumn == ocolumn:
        single_move(origin, destination, board)#move buttons for test
        match_list = get_matches(board)
        single_move(origin, destination, board)#move them back
        return len(match_list)

    elif (dcolumn == ocolumn-1 or dcolumn == ocolumn+1) and drow == orow:
        single_move(origin, destination, board)#move buttons for test
        match_list = get_matches(board)
        single_move(origin, destination, board)#move them back
        return len(match_list)


def single_move(origin, destination, board):
    """Swaps a selected shape with a selected neighbor. Use the 'test'
        parameter to prevent screen updating"""
    board[destination][1], board[origin][1] = board[origin][1], board[destination][1]

def match_factory(origin, destination, board):
    """Called on valid moves to get all matches and cascades and call
        screen updates"""
    match_list = get_matches(board)
    while len(match_list):
        matches_down(match_list, board)
        match_list = get_matches(board)
    board[destination][0] = ''
    board[origin][0] = ''


def get_matches(board, *args):
    """Search algorithm to find all matches on the board. Implements a
       variation of a flood fill algorithm."""
    matches = []
#horizontal matches
    for y in range(8):
        for x in range(8):
            shape = board[(x,y)][1]
            if shape !=0:
                match = []
                i = x
                while i < 8:
                    if board[(i,y)][1] == shape:
                        match.append((i,y))
                    else:
                        break
                    i += 1
                if len(match) > 2:
                    x = i+1
                    matches.append(match)
# vertical matches
    for x in range(8):
        for y in range(8):
            shape = board[(x,y)][1]
            if shape != 0:
                match = []
                i = y
                while i < 8:
                    if board[(x,i)][1] == shape:
                        match.append((x,i))
                    else:
                        break
                    i += 1

                if len(match) > 2:
                    y = i+1
                    matches.append(match)
    return matches


def matches_down(matches, board):
    """Animation factory for match removal. Accepts a list of lists"""
    for match in matches:
        for location in match:
            board[location][1] = 0

def get_potential_matches(board, *args):
    """Search algorithm to find all potential matches on the board. """
#horizontal potential matches
    for y in range(8):
        for x in range(8):
            shape = board[(x,y)][1]
            if shape !=0:
                if (board[(x+1,y)][1]==shape and (
                        board[(x+2,y+1)][1]==shape or
                        board[(x+3,y  )][1]==shape or
                        board[(x+2,y-1)][1]==shape)):
                    return True
                elif (board[(x+2,y)]==shape and (
                        board[(x+1,y+1)][1]==shape or
                        board[(x+3,y  )][1]==shape or
                        board[(x+1,y-1)][1]==shape)):
                    return True
                elif ((board[(x+1,y+1)][1]==shape and 
                        board[(x+2,y+1)][1]==shape) or (
                        board[(x-1,y-1)][1]==shape and
                        board[(x+2,y-1)][0]==shape)):
                    return True
# vertical potential matches
    for x in range(8):
        for y in range(8):
            shape = board[(x,y)][1]
            if shape !=0:
                if board[(x,y+1)][1]==shape and (
                        board[(x+1,y+2)][1]==shape or
                        board[(x  ,y+3)][1]==shape or
                        board[(x-1,y+2)][1]==shape):
                    return True
                elif board[(x,y+2)][1]==shape and (
                        board[(x+1,y+1)][1]==shape or
                        board[(x  ,y+3)][1]==shape or
                        board[(x-1,y+1)][1]==shape):
                    return True
                elif ((board[(x+1,y+1)][1]==shape and 
                             board[(x+1,y+2)][1]==shape) or
                            (board[(x-1,y+1)][1]==shape and
                             board[(x-1,y+2)][1]==shape)):
                    return True
    return False
