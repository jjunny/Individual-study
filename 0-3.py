from random import randint

board = []

for x in range(0, 10):
    board.append(["O"] * 10)

guess_row = int(input("열:"))
guess_col = int(input("행:"))
row_rotate = randint(0, 9)
col_rotate = randint(0, 9)
distance = int(((guess_row - row_rotate)**2 + (guess_col - col_rotate)**2)**0.5)

while(True):
    if guess_row == row_rotate and guess_col == col_rotate:
        print("쥐를 잡았습니다.~")
        break
    else:
        print("남은 거리는")
        print(distance)
        print("입니다.")
        guess_row = int(input("열:"))
        guess_col = int(input("행:"))

