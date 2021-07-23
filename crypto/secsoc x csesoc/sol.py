with open("data/secsocxcsesoc.txt", "r") as f:
    data = f.read()
    data = data.replace("secsoc", "0")
    data = data.replace("csesoc", "1")
    print("".join(map(lambda binStr: chr(int(binStr, 2)), data.split(" "))))