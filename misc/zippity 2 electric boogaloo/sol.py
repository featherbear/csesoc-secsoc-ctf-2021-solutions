import os
from hashlib import sha512

dir = "data/electric/"
for file in os.listdir(dir):
    with open(dir + file, "rb") as f:
        line = f.readline()
        hash = sha512(line).hexdigest()
        if not hash.startswith("146"): continue
        print(line, file)