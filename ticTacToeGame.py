# WIP
def validateMove():
    pass

def updateActivePlayer():
    pass

def updateBoard(board, moves1, moves2):
    for i in range(len(moves1)):
        board[moves1[i]] = "X"
        board[moves2[i]] = "O"
    return board

def isWinner():
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
    player1 = [1,5,7]
    player2 = [3,8,9]
    currentBoard = updateBoard(initialBoard, player1, player2)
    # print(currentBoard)
    printBoard(currentBoard)

if __name__ == "__main__":
    main()