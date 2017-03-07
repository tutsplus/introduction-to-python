lorem_file = open("lorem.txt")
for line in lorem_file:
    print(line.rstrip())
lorem_file.close()
