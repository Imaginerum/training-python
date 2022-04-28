#tic tac toe the simplest it can be.

theBoard = {'top-L': " ", 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('–+–+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('–+–+–')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print('\n')

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