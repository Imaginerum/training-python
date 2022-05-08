#tic tac toe the simplest it can be: Player vs. player version.

theBoard = {'7': " ", '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

def gamesControl():
    print("\nSterowanie grą to: ", end='\n\n')
    print("7|8|9")
    print("-+-+-")
    print("4|5|6")
    print("-+-+-")
    print("1|2|3", end='\n\n')

def printBoard(board):
    print("Przebieg gry: \n")
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('–+–+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('–+–+–')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print()

gamesControl()

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print("Ruch gracza " + turn + ". W którym polu stawiasz znak?")
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
    printBoard(theBoard)

printBoard(theBoard)