# open(...)
with open('demo.txt', 'r', encoding='UTF-8') as f:
    first_line = f.readline()
    print(first_line)
    #for line in f:
    #    print(line, end="")

# automatically call
# f.close()

print(f.readline())