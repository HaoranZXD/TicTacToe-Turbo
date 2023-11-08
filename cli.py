from logic import check_winner, get_empty_board,print_board,get_player_input


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
            if board[row][col] is None:
                board[row][col] = current_player
                winner = check_winner(board)
                current_player = 'X' if current_player == 'O' else 'O'
            else:
                print("Invalid input, try again") 
     print_board(board)
     if winner == "Draw":
        print("The game is a draw")
     else:
        print(f"Winner is {winner}")