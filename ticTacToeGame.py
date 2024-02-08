# WIP
class Player:
    def __init__(self, name):
        self.name = name
        self.lastMoves = ['?','?','?']
        self.isActive = False
        
    def toggleIsActive(self):
        if self.isActive == True:
            self.isActive = False
        else:
            self.isActive = True

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
        printBoard(board)
        temp = int(input('Please select a square [1-9] to move\n'))
        if validateMove(board, temp):
            return temp
        else:
            move(board)

def validateMove(board, square):
    if square < 1 or square > 9:
        print("Invalid Move: Square selected is out of range. Try again!")
        return False
    if board[square] != '?':
        print("Invalid Move: Square selected is already occupied. Try again!")   
        return False
    return True

def updateActivePlayer(player1, player2):
    if player1.isActive == False:
        player1.toggleIsActive()
        player2.toggleIsActive()
        return player1
    else:
        player1.toggleIsActive()
        player2.toggleIsActive()
        return player2
        

def setBoard():
    board = {
        1:"?", 2:"?", 3:"?",
        4:"?", 5:"?", 6:"?",
        7:"?", 8:"?", 9:"?"
    }
    return board

def updatePlayerLastMove(board, currentPlayer, move):
    if len(currentPlayer.lastMoves) < 3:
        currentPlayer.lastMoves.append(move)
    else:
        elementRemoved = currentPlayer.lastMoves.pop(0)
        board[elementRemoved] = '?'
        currentPlayer.lastMoves.append(move)

def updateBoard(board, player1, player2):
    for i in range(len(player1.lastMoves)):
        board[player2.lastMoves[i]] = "O"
    for j in range(len(player2.lastMoves)):
        board[player1.lastMoves[j]] = "X"
    return board

def isGameOver(currentPlayer):
    winningMoves = [
        {1,2,3},{4,5,6},{7,8,9},{1,4,7},
        {2,5,8},{3,6,9},{3,5,7},{1,5,9},
    ]
    if set(currentPlayer.lastMoves) in winningMoves:
        print("Winner Winner chiken dinner")
        return True
    return False

def getWinner(currentPlayer):
    print("Game Over, " + currentPlayer.name + " is the winner")

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
    currentBoard = setBoard()
    printBoard(currentBoard)
    player1 = Player('player1')
    player2 = Player('player2')
    currentPlayer = player1 if setStartingPlayer() == 1 else player2
    currentPlayer.toggleIsActive()
    while isGameOver(currentPlayer) == False:
        validMove = move(currentBoard)
        updatePlayerLastMove(currentBoard, currentPlayer, validMove)
        currentBoard = updateBoard(currentBoard, player1, player2)
        if isGameOver(currentPlayer) == True:
            getWinner(currentPlayer)
            return
        currentPlayer = updateActivePlayer(player1, player2)
        printBoard(currentBoard)
if __name__ == "__main__":
    main()