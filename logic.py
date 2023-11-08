def check_winner(board):
    # check rows
    #    ['X', 'X', 'X'], -> set(['X', 'X', 'X']) -> {'X'}
    #    ['O', 'X', 'O'], -> set(['O', 'X', 'O']) -> {'X', 'O'}
    #    ['O', 'O', 'X'],
    for row in board:
        if row[0] is not None and len(set(row)) == 1:
            return row[0]

    # check columns
    #    ['X', 'X', 'X'],
    #    ['O', 'X', 'O'],
    #    ['O', 'O', 'X'],
    # how to index -> board[row][column]
    # column_idxs = [[0,0], [1,0], [2,0]]
    # column_idxs = [[0,1], [1,1], [2,1]]
    for i in range(len(board)):
        # len(board) -> 3
        column = [board[j][i] for j in range(len(board))]
        # column => ['X', 'O', 'O']
        # column => ['X', 'X', 'O]
        if len(set(column)) == 1 and board[0][i] is not None:
            return board[0][i]

    # check diagonals
    # check columns
    #    ['X', 'X', 'X'],
    #    ['O', 'X', 'O'],
    #    ['O', 'O', 'X'],
    # how to index -> board[row][column]
    # idx -> [[0,0], [1,1], [2, 2]]
    top_left_to_bottom_right = [board[i][i] for i in range(len(board))]
    if len(set(top_left_to_bottom_right)) == 1 and board[0][0] is not None:
        return board[0][0]

    # check diagonals
    # check columns
    #    ['X', 'X', 'X'],
    #    ['O', 'X', 'O'],
    #    ['O', 'O', 'X'],
    # how to index -> board[row][column]
    # idx -> [[0,2], [1,1], [2, 0]]
    top_right_to_bottom_left = [board[i][len(board)-i-1] for i in range(len(board))]
    if len(set(top_right_to_bottom_left)) == 1 and board[0][len(board)-1] is not None:
        return board[0][len(board)-1]
    
    
    flat_board = []
    for row in board:
        flat_board.extend(row)

    if not None in flat_board:
        return "Draw"
        
    return None

def get_empty_board():
    return [
        [None,None,None],
        [None,None,None],
        [None,None,None],
    ]

def print_board(board):
    for row in board:
        print(row)

def get_player_input(current_player):
    player_input = input(f"player {current_player} please input (row,col): \n")
    row_col_list = player_input.split(",")
    row, col = [int(x)for x in row_col_list]
    return row, col

