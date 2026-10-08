text = input("Enter text: ")
text = text.lower()
words = text.split()
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
