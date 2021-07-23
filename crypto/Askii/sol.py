with open("data/askii.txt", "r") as f:
   print("".join(map(lambda x: chr(int(x)), f.read().strip().split(" "))))