marks = [
    [78, 85, 90],
    [88, 76, 92],
    [69, 80, 74]
]

names = ["Student 1", "Student 2", "Student 3"]

highest = -1
top_student = ""

for i in range(len(marks)):
    total = sum(marks[i])
    average = total / len(marks[i])

    print(names[i], "Total:", total)
    print("Average:", round(average, 2))

    if total > highest:
        highest = total
        top_student = names[i]

print("Top performer:", top_student)
print("Highest total:", highest)