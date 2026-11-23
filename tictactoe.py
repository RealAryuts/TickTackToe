def show_board(b):
    print()
    print(" " + b[0] + " | " + b[1] + " | " + b[2])
    print("---+---+---")
    print(" " + b[3] + " | " + b[4] + " | " + b[5])
    print("---+---+---")
    print(" " + b[6] + " | " + b[7] + " | " + b[8])
    print()


def check_win(b, p):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for w in wins:
        if b[w[0]] == p and b[w[1]] == p and b[w[2]] == p:
            return True
    return False

def play():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    turn = "X"
    moves = 0

    while True:
        show_board(board)
        move = input("Player " + turn + ", pick a spot (1-9): ")

        if not move.isdigit():
            print("Enter a number from 1 to 9.")
            continue



        pos = int(move) - 1
        if pos < 0 or pos > 8:
            print("Out of range, try again.")
            continue

        if board[pos] == "X" or board[pos] == "O":
            print("Spot already taken.")
            continue

        board[pos] = turn
        moves += 1

        if check_win(board, turn):
            show_board(board)
            print("Player " + turn + " wins!")
            break

        if moves == 9:
            show_board(board)
            print("It's a draw!")
            break

        if turn == "X":
            turn = "O"
        else:
            turn = "X"


while True:
    play()
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")
        break
