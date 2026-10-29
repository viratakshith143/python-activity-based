text = input("Enter text: ")

if text == "":
    print("Enter some text")
else:
    result = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result += text[i - 1] + str(count)
            count = 1

    result += text[-1] + str(count)

    print("Compressed text:", result)
    print("Original length:", len(text))
    print("Compressed length:", len(result))