# WIP
def instructions():
    return """TIC TAC TOE GAME
        Game Instructions:
        """

def setStartingPlayer():
    isStartingPlayerValid = False
    while isStartingPlayerValid == False:
        startingPlayer = int(input("Please enter the number (1 or 2) to select which player should start the game\n"))
        if startingPlayer > 0 and startingPlayer < 3:
            isStartingPlayerValid = True
    return startingPlayer

def move(board):
    isValidMove = False
    while isValidMove == False:
        temp = int(input('Please select a square [1-9] to move\n'))
        if validateMove(board, temp):
            return temp
        else:
            move(board)
    # return temp 

def validateMove(board, square):
    if square < 1 or square > 9:
        print("Invalid Move: Square selected is out of range. Try again!")
        return False
    if board[square] != '?':
        print("Invalid Move: Square selected is already occupied. Try again!")   
        return False
    return True

def updateActivePlayer(currentPlayer):
    # if currentPlayer == 1:
    #     return currentPlayer + 1
    # else:
    #     return currentPlayer - 1
    return currentPlayer + 1 if currentPlayer == 1 else currentPlayer - 1

def setBoard():
    board = {
        1:"?", 2:"?", 3:"?",
        4:"?", 5:"?", 6:"?",
        7:"?", 8:"?", 9:"?"
    }

    return board

def updatePlayerLastMoves(board, activePlayer, move):
    if len(activePlayer) < 3:
        activePlayer.append(move)
    else:
        elementRemoved = activePlayer.pop(0)
        board[elementRemoved] = '?'
        activePlayer.append(move)
         

def updatePlayer(board, moves1, moves2):
    for i in range(len(moves1)):
        board[moves1[i]] = "X"
        board[moves2[i]] = "O"
    return board

def isGameOver(currentPlayerMoves):
    winningMoves = [
        {1,2,3},{4,5,6},{7,8,9},{1,4,7},
        {2,5,8},{3,6,9},{3,5,7},{1,5,9},
    ]
    # print(set(currentPlayerMoves))
    # if set(currentPlayerMoves) in winningMoves:
    # for i in range(len(winningMoves)):
    #     if winningMoves[i] == set(currentPlayerMoves):
    #         return True 
    if set(currentPlayerMoves) in winningMoves:
        print("Winner Winner chiken dinner")
        return True
    return False

def getWinner(currentPlayer):
    print("Game Over, Player " + currentPlayer)

def printBoard(board):    
    print("")
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("")

def main():
    print(instructions())
    initialBoard = setBoard()
    
    printBoard(initialBoard)
    player1 = []
    player2 = []
    currentPlayer = setStartingPlayer()
    while isGameOver == False:
        pass # COMPLETE HERE
    # print(currentPlayer)
    # player1 = [3,8,6]
    # player2 = [5,1,9]
    
    
    # currentBoard = updatePlayerLastMoves(initialBoard, player1, player2)
    
    # currentBoard = {
    #     1:"O", 2:"?", 3:"X",
    #     4:"?", 5:"O", 6:"X",
    #     7:"?", 8:"X", 9:"O"
    # }


    # printBoard(currentBoard)
    # currentPlayer = updateActivePlayer(currentPlayer)
    # print(currentPlayer)
    # currentPlayer = updateActivePlayer(currentPlayer)
    # print(currentPlayer)
    # currentPlayer = updateActivePlayer(currentPlayer)
    # print(currentPlayer)
    # print(isGameOver(player1))
    # print(isGameOver(player2))
    # printBoard(currentBoard)
    # move(currentBoard)
    # printBoard(currentBoard)
    # move(currentBoard)
    # printBoard(currentBoard)
    # move(currentBoard)
    # printBoard(currentBoard)
    # move(currentBoard)
    # move(currentBoard)
    # move(currentBoard)
    

    
    

if __name__ == "__main__":
    main()