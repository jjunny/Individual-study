first = input("First Sentence:")
second = input("Second Sentence:")

first = ' '.join(sorted(first))
second = ' '.join(sorted(second))

if first == second:
    print("It is anagram")
else:
    print("It is not anagram")
