import fileinput
unique_words = set()

for line in fileinput.input('story.txt'):
    words = line.split()
    # s.add(x) -> add x to the set
    # add all "things" from list words
    unique_words.update(words)

print(unique_words)