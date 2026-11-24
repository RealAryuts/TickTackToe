

RED = "\033[91m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def colorized(cell):
    if cell == "X":
        return RED + cell + RESET
    elif cell == "O":
        return BLUE + "O" + RESET
    return cell
    

def show_board(b):
    print()
    print(" " + colorized(b[0]) + " | " + colorized(b[1]) + " | " + colorized(b[2]))
    print("---+---+---")
    print(" " + colorized(b[3]) + " | " + colorized(b[4]) + " | " + colorized(b[5]))
    print("---+---+---")
    print(" " + colorized(b[6]) + " | " + colorized(b[7]) + " | " + colorized(b[8]))
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
p1_name = input("Enter Player X name: ") or "Player X"
p2_name = input("Enter Player O name: ") or "Player O"
x_wins = 0
o_wins = 0
draws = 0

def play():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    turn = "X"
    moves = 0
    history = []        
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
        history.append(turn + " -> " + move)
        if check_win(board, turn):
            show_board(board)
           
            global x_wins, o_wins
            if turn == "X":
                x_wins += 1
                print(GREEN + p1_name + " wins!" + RESET)
            else:
                o_wins += 1
                print(GREEN + p2_name + " wins!" + RESET)
            print("Moves played:", ", ".join(history)   )
            break

        if moves == 9:
            show_board(board)
          
            global draws
            draws += 1
            print(YELLOW + "It's a draw!" + RESET)
            print("Moves played:", ", ".join(history))
            break

        if turn == "X":
            turn = "O"
        else:
            turn = "X"


while True:
    play()
    print()
    print("Scoreboard:")
    print(p1_name + " (X): " , x_wins)
    print(p2_name + " (O): " , o_wins)
    print("Draws: " , draws)
    print("--------------------")
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")
        break
