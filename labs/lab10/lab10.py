"""
Name: Erin Phillips
lab10.py
"""


def build():
    return list(range(1, 10))


def display(board):
    for i in range(3):
        num = i * 3
        print(board[num], board[num + 1], board[num + 2], sep=" | ")
        print(10 * "_")


def place(board, pos, piece):
    if piece == "x" or piece == "o":
        board[pos - 1] = piece


def legal(board, pos):
    if board[pos - 1] == pos and pos != 0:
        return True
    return False


def is_won(board, piece):
    # horizontal win
    for i in range(3):
        num = i * 3
        if board[num] != piece:
            continue
        if board[num + 1] != piece:
            continue
        if board[num + 2] != piece:
            continue
        return True

    # vertical win
    for i in range(3):
        if board[i] != piece:
            continue
        if board[i + 3] != piece:
            continue
        if board[i + 6] != piece:
            continue
        return True

    # diagonal win
    if board[0] == piece:
        if board[4] == piece:
            if board[8] == piece:
                return True

    if board[2] == piece:
        if board[4] == piece:
            if board[6] == piece:
                return True

    return False


def game_over(board):
    if is_won(board, "x"):
        return True
    elif is_won(board, "o"):
        return True
    else:
        for i in range(9):
            if board[i] == i + 1:
                return False
        return True


def play():
    board = build()
    while True:
        display(board)
        x_pos = eval(input("Enter where you want to play x: "))
        while not legal(board, x_pos):
            x_pos = eval(input("Illegal move! Enter where you want to play x: "))
        place(board, x_pos, "x")
        if game_over(board):
            if is_won(board, "x"):
                display(board)
                print("Player x wins!")
                exit()
            if is_won(board, "o"):
                display(board)
                print("Player o wins!")
                exit()
            else:
                display(board)
                print("Wow! Its a tie!")
                exit()
        display(board)
        o_pos = eval(input("Enter where you want to play o: "))
        while not legal(board, o_pos):
            o_pos = eval(input("Illegal move! Enter where you want to play o: "))
        place(board, o_pos, "o")
        if game_over(board):
            if is_won(board, "x"):
                display(board)
                print("Player x wins!")
                exit()
            if is_won(board, "o"):
                display(board)
                print("Player o wins!")
                exit()
            else:
                display(board)
                print("Wow! Its a tie!")
                exit()


def main():
    play()
    pass


main()
