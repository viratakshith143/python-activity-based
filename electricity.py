days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

appliances = [
    [2, 2, 2, 2, 2, 3, 3],
    [1, 1, 1, 1, 1, 2, 2],
    [4, 3, 4, 4, 5, 2, 1]
]

names = ["Fan", "Light", "Computer"]

for i in range(len(appliances)):
    print(names[i], "weekly usage:", sum(appliances[i]))

daily = []

for j in range(7):
    total = 0

    for i in range(3):
        total += appliances[i][j]

    daily.append(total)
    print(days[j], "usage:", total)

peak = daily.index(max(daily))

print("Highest consumption day:", days[peak])