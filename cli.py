from logic import check_winner
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


if __name__ =='__main__':
     board = get_empty_board()
     current_player = "X"
     winner = None

     while winner is None:
            print_board(board)
            #ask user input
            try:
                row,col = get_player_input(current_player)            
            except ValueError:
                 print("Invalid input, try again")
                 continue
            
            board[row][col] = current_player
            winner = check_winner(board)
            current_player = 'X' if current_player == 'O' else 'O' 
     print_board(board)
     print(f"Winner is {winner}")