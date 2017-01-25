from random import randint
from time import sleep

n = int(input("인원수를 입력해 주세요.:"))
i = randint(1, n)

for x in range(1, n + 1):
    empty = input("엔터를 눌러주세요.")
    if x == i:
        print("당첨입니다.")
        sleep(3)
    else:
        print("통과입니다.")
