import random
# 1 == 가위
# 2 == 바위
# 3 == 보

while(True):
    print("1 == 가위, 2 == 바위, 3 == 보")
    person = int(input("가위 바위 보~"))
    computer = random.randint(1, 3)

    # ---------------------------- #
    if person == 1 & computer == 1:
        print("비겼습니다.")
    if person == 1 & computer == 2:
        print("졌습니다.")
    if person == 1 & computer == 3:
        print("이겼습니다.")
    # ---------------------------- #
    if person == 2 & computer == 1:
        print("이겼습니다.")
    if person == 2 & computer == 2:
        print("비겼습니다.")
    if person == 2 & computer == 3:
        print("졌습니다.")
    # ---------------------------- #
    if person == 3 & computer == 1:
        print("졌습니다.")
    if person == 3 & computer == 2:
        print("이겼습니다.")
    if person == 3 & computer == 3:
        print("비겼습니다.")
    # ---------------------------- #
