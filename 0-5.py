from random import randint

result = []

# 1 == S
# 2 == R
# 3 == P

for x in range(0, 10):
    a = randint(1, 3)
    n = input("가위 = S, 바위 = R, 보 = P:")
    if n == "S" and a == 1:
        print("Draw")
        result.append("D")
    elif n == "S" and a == 2:
        print("Lose")
        result.append("L")
    elif n == "S" and a == 3:
        print("Win")
        result.append("W")
    # ---------------------- #
    elif n == "R" and a == 1:
        print("Win")
        result.append("W")
    elif n == "R" and a == 2:
        print("Draw")
        result.append("D")
    elif n == "R" and a == 3:
        print("Lose")
        result.append("L")
    # ---------------------- #
    elif n == "P" and a == 1:
        print("Lose")
        result.append("L")
    elif n == "P" and a == 2:
        print("Win")
        result.append("W")
    elif n == "P" and a == 3:
        print("Draw")
        result.append("D")

Win = result.count("W")
Draw = result.count("D")
Lose = result.count("L")

print(str(Win) + " times win, " + str(Draw) + " times draw, " + str(Lose) + " times lose.")
