from base64 import b64decode

with open("data/base-onion.txt", "r") as f:
    data = f.read()
    while True:
        data = b64decode(data)
        if b"NEWBIE{" in data:
            break

    print(data)