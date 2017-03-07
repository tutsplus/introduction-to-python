with open("lorem_copy.txt", "r+") as lorem_copy:
    lorem_copy.write("Tuts+ is Awesome!")
    print(lorem_copy.read())
