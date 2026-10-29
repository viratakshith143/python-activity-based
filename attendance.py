conducted = int(input("Classes conducted: "))
attended = int(input("Classes attended: "))
target = float(input("Required attendance percentage: "))

if conducted <= 0 or attended < 0 or attended > conducted:
    print("Invalid input")
elif target < 0 or target > 100:
    print("Invalid target percentage")
else:
    percentage = attended / conducted * 100
    extra = 0

    while (attended + extra) / (conducted + extra) * 100 < target:
        extra += 1

    print("Current attendance:", round(percentage, 2), "%")
    print("Extra classes required:", extra)