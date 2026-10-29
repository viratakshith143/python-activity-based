n = int(input("Enter a positive odd number: "))

if n <= 0 or n % 2 == 0:
    print("Enter a positive odd number")
else:
    for i in range(1, n + 1, 2):
        print(" " * ((n - i) // 2) + "*" * i)

    for i in range(n - 2, 0, -2):
        print(" " * ((n - i) // 2) + "*" * i)