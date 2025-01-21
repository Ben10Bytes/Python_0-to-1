with open("demoFile.txt", "r") as file:
    content = file.read()
    words = content.split()
    num_words = len(words)
    print("Number of words:", num_words)
