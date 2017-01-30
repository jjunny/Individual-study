from random import randint

h1 = []
h2 = []
h3 = []
h4 = []
horse_list = [h1, h2, h3, h4]
winner = []
loser = []

def moving_horse():
    while(True):
        h1.append(randint(0, 10))
        h2.append(randint(0, 10))
        h3.append(randint(0, 10))
        h4.append(randint(0, 10))
        if h1 >= 300 or h2 >= 300 or h3 >= 300 or h4 >= 300:
            break


def main():
    human_select = input("말을 선택해 주세요(h1, h2, h3, h4):")
    computer_select = horse_list.pop()
if __name__ == '__main__':
    main()
