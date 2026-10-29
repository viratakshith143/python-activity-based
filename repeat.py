sentence = input("Enter a sentence: ").lower()

for mark in ".,!?;:":
    sentence = sentence.replace(mark, " ")

words = sentence.split()

found = False

for i in range(len(words)):
    word = words[i]

    if word not in words[:i] and words.count(word) > 1:
        print(word, "appears", words.count(word), "times")
        found = True

if not found:
    print("No repeated words found")
    