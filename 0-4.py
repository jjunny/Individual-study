from random import randint

prediction = randint(0, 100)
print(prediction)
while(True):
    n = input("High or Low?:")
    if n == "H" or n == "h":
        min = prediction
        prediction = randint(min + 1, 100)
        print(prediction)
    elif n == "L" or n == "l":
        max = prediction
        prediction = randint(0, max - 1)
        print(prediction)
    elif n == "C" or n == "c":
        print("Correct!")
        break
