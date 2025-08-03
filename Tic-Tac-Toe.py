#Implementation of Two Player Tic-Tac-Toe game in Python.

''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

the_board = {'7': ' ' , '8': ' ' , '9': ' ' ,
             '4': ' ' , '5': ' ' , '6': ' ' ,
             '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in the_board:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Now we'll write the main function which has all the gameplay functionality.

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(the_board)
        print(f"It's your turn, {turn} . Move to which place?")

        move = input()

        if the_board[move] == ' ':
            the_board[move] = turn
            count += 1
        else:
            print(f"That place is already occupied!\n Choose another one.")
            continue

        if count >= 5:

            if the_board['7'] == the_board['8'] == the_board['9'] != ' ':
                printBoard(the_board)
                print("\n Game Over! \n")
                print(f"****{turn} Won! ****")
                break
            elif the_board['4'] == the_board['5'] == the_board['6'] != ' ':
                printBoard(the_board)
                print("\n Game Over! \n")
                print(f"****{turn} Won! ****")
                break
            elif the_board['1'] == the_board['2'] == the_board['3'] != ' ':
                printBoard(the_board)
                print("\n Game Over! \n")
                print(f"****{turn} Won! ****")
                break
            elif the_board['1'] == the_board['4'] == the_board['7'] != ' ':
                printBoard(the_board)
                print("\n Game Over! \n")
                print(f"****{turn} Won! ****")
                break
            elif the_board['2'] == the_board['5'] == the_board['8'] != ' ':
                printBoard(the_board)
                print("\n Game Over! \n")
                print(f"****{turn} Won! ****")
                break
            elif the_board['3'] == the_board['6'] == the_board['9'] != ' ':
                printBoard(the_board)
                print("\n Game Over! \n")
                print(f"****{turn} Won! ****")
                break
            elif the_board['7'] == the_board['5'] == the_board['3'] != ' ':
                printBoard(the_board)
                print("\n Game Over! \n")
                print(f"****{turn} Won! ****")
                break
            elif the_board['1'] == the_board['5'] == the_board['9'] != ' ':
                printBoard(the_board)
                print("\n Game Over! \n")
                print(f"****{turn} Won! ****")
                break

        if count == 9:
            print("\n Game Over! \n")
            print("It's a Tie!")
            break

        if turn == 'X':
            turn = 'O'

        else:
            turn = 'X'

    restart = input("Do you want to play again? (Y/N): ")
    
    if restart == 'Y' or restart == 'y':
        for key in board_keys:
            the_board[key] = ' '
        game()

if __name__ == "__main__":
    game()
