from sys import exit
f_1 = open("1.txt", 'r')
f_2 = open("2.txt", 'r')
f_3 = open("3.txt", 'r')


def main():
    number_1 = f_1.read()
    number_2 = f_2.read()
    number_3 = f_3.read()
    number_choose = input("Please select number(1, 2, 3):")
    if number_choose == 1:
        print(number_1)
        answer_1 = input("Please input your answer:")
        if answer_1 == "a":
            print(number_2)
            answer = input("Please input your answer:")
            if answer == "b":
                print(number_3)
                answer = input("Please input your answer:")
                if answer == "c":
                    print("Congratulation!")
