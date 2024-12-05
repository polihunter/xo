def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Игрок {current_player}, введите номер строки (0-2): "))
            col = int(input(f"Игрок {current_player}, введите номер столбца (0-2): "))

            if board[row][col] != " ":
                print("Эта клетка уже занята! Попробуйте снова.")
                continue

            board[row][col] = current_player

            if check_winner(board):
                print_board(board)
                print(f"Поздравляем, игрок {current_player} выиграл!")
                break

            if is_board_full(board):
                print_board(board)
                print("Игра закончилась вничью!")
                break

            current_player = "O" if current_player == "X" else "X"

        except (ValueError, IndexError):
            print("Некорректный ввод.")

if __name__ == "__main__":
    main()

