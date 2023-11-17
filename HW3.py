board = [i for i in range(1, 10)]


def play_board(board):
    for i in range(3):
        print(board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3])

def get_info(symbol):
    valid = False
    while not valid:
        answer = int(input(("Выберите позицию для " + symbol + "? ")))

        if answer >= 1 and answer <= 9:
            if str(board[answer - 1]) not in "XO":
                board[answer - 1] = symbol
                valid = True
            else:
                print("Позиция занята!")
        else:
            print("Некорректный ввод, ведите число от 1 до 9!.")


def check_win(board):
    win_position = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_position:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        play_board(board)
        if counter % 2 == 0:
            get_info("X")
        else:
            get_info("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break

    play_board(board)


main(board)