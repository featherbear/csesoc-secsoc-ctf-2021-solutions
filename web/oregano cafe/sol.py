from data.starch import *

# hex(int(bitstr, 2))[2:]
final = "a4ec243c744c8424fcb454f4cc4464246ca40484243cd454bcf41424fc048c04"

# hex(int(bitstr, 2))
final = "0x" + final

# # int(bitstr, 2)
# final = int(final, 16)

# bitstr
final = hex_to_bitstring(final)

print(final)

chunks = [final[i:i+8] for i in range(0, len(final), 8)]
print(chunks, len(chunks))

# Calculate the first ASCII string
'''
last = lcg(ord(input_string[0]))

10100100 = lcg(ord(char) * lcg(ord(char)))
'''

results = []
import string
def recu(upToNow, idx, last):
    if idx >= 32:
        res = "".join([*map(chr, upToNow)])
        if res not in results:
            res = "".join([*map(chr, upToNow)])
            results.append(res)
            print("Found new", res, len(res))
        return
        # raise Exception(upToNow)
    for x in string.printable:
        x = ord(x)
        if idx == 0: last = lcg(x)
        attempt = lcg(x * last)
        if str(bin(attempt))[2:].zfill(8) == chunks[idx]:
            recu([*upToNow, x], idx+1, lcg(attempt))

recu([], 0, None)
