days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

prepared = [100, 120, 90, 110, 80]
served = [88, 100, 82, 90, 75]

for i in range(len(days)):
    leftover = prepared[i] - served[i]
    waste = leftover / prepared[i] * 100

    print("\nDay:", days[i])
    print("Leftover meals:", leftover)
    print("Waste percentage:", round(waste, 2), "%")

    if waste > 15:
        print("Warning: High food waste")