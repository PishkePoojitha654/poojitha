import string
sentence = input("Enter a sentence: ")

sentence = sentence.lower()

for char in string.punctuation:
    sentence = sentence.replace(char, "")

words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Words in descending order:")

while len(word_count) > 0:
    max_word = ""
    max_count = 0

    for word in word_count:
        if word_count[word] > max_count:
            max_count = word_count[word]
            max_word = word

    print(max_word, ":", max_count)

    del word_count[max_word]