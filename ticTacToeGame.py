# WIP
def move():
    pass

def validateMove(board, square):
    if square < 1 or square > 9:
        print("Invalid Move: Square selected is out of range. Try again!.")
    if board[square] != '?':
        print("Invalid Move: Square selected is already occupied. Try again!")  

def updateActivePlayer(currentPlayer):
    # if currentPlayer == 1:
    #     return currentPlayer + 1
    # else:
    #     return currentPlayer - 1
    return currentPlayer + 1 if currentPlayer == 1 else currentPlayer - 1

def updatePlayerLastMoves(player):
    pass

def updateBoard(board, moves1, moves2):
    for i in range(len(moves1)):
        board[moves1[i]] = "X"
        board[moves2[i]] = "O"
    return board

def isGameOver(currentPlayer):
    winningMoves = [
        (1,2,3),(4,5,6),(7,8,9),(1,4,7),
        (2,5,8),(3,6,9),(3,5,7),(1,5,9),
    ]
    if currentPlayer in winningMoves:
        print("Winner Winner chiken dinner")
        return True

def getWinner():
    pass

def printBoard(board):    
    print("")
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("")

def main():
    print("Tic Tac Toe Game")
    initialBoard = {
        1:"?",
        2:"?",
        3:"?",
        4:"?",
        5:"?",
        6:"?",
        7:"?",
        8:"?",
        9:"?"
    }
    printBoard(initialBoard)
    currentPlayer = 1
    player1 = (3,8,6)
    player2 = (1,5,9)
    
    currentBoard = updateBoard(initialBoard, player1, player2)
    # print(currentBoard)
    printBoard(currentBoard)
    currentPlayer = updateActivePlayer(currentPlayer)
    print(currentPlayer)
    currentPlayer = updateActivePlayer(currentPlayer)
    print(currentPlayer)
    currentPlayer = updateActivePlayer(currentPlayer)
    print(currentPlayer)
    print(isGameOver(player2))
    

if __name__ == "__main__":
    main()