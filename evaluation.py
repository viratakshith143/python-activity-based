key = input("Enter answer key: ").upper()
answers = input("Enter student answers (- for blank): ").upper()

if len(key) != len(answers):
    print("Answer lengths must be equal")
else:
    correct = 0
    wrong = 0
    blank = 0

    for i in range(len(key)):
        if answers[i] == "-":
            blank += 1
        elif answers[i] == key[i]:
            correct += 1
        else:
            wrong += 1

    score = correct - 0.25 * wrong

    print("Correct answers:", correct)
    print("Wrong answers:", wrong)
    print("Unanswered:", blank)
    print("Final score:", score)