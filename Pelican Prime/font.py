#!/usr/bin/env python3

# |all_chars| array must match order of data in font-master.txt.
# This is not checked.
# Characters may be in any order, except that the first must be the lowest
# ASCII value and the last must be the highest ASCII value.
# Gaps in ASCII values are allowed anywhere.
# Do not include the space character.
all_chars = list(map(chr, range(0x21, 0x80)))

min_index = ord(all_chars[0])
max_index = ord(all_chars[-1]) + 1
step = 18
data = {}
with open("font-master.txt", "r") as f:
    for c in all_chars:
        data[c] = {}
        data[c]["description"] = f.readline().strip()[1:]
        data[c]["rawbits"] = []
        data[c]["width"] = 0
        for row in range(9):
            rawbits = f.readline().strip()
            data[c]["rawbits"].append(rawbits)
            rowwidth = rawbits.rfind("1")
            data[c]["width"] = max(rowwidth, data[c]["width"])

used_chars = ''.join(all_chars)
# # delete font data for unused characters
# # commented out but feel free to use this as a template for minimizing
# # the data set of characters included in the outputted font data

# used_chars = '0123456789' + chr(0x7F)
# with open('../../src/ui.strings.a', 'r') as f:
#     lines = [l.split('"')[1] for l in f.readlines() if '!raw' in l]
# used_chars += "".join(lines)
# used_set = set(used_chars)
# used_list = list(used_set)
# used_list.sort()
# used_chars = "".join(used_list)
# used_chars  = used_chars.replace(' ', '')
# for c in all_chars:
#     if c not in used_chars:
#         del data[c]

print("; Pelican Prime pixel font")
print("; (c) 2023 by 4am")
print("; license:Open Font License 1.1, see OFL.txt")
print("; This file is automatically generated")

print()
print(f"kPelicanPrimeMin = {hex(min_index)} ; ASCII value of first character")
print(f"kPelicanPrimeCount = {len(used_chars)} ; total number of characters")

print()
print("_PelicanPrimeWidths")
for c in map(chr, range(min_index, max_index)):
    if c in used_chars:
        width = data[c]['width'] + 2
        description = data[c]['description']
    else:
        width = 0
        description = "unused"
    print(f"         !byte {width} ; {description}")

print()
print("_PelicanPrimeOffsetLo")
for c in map(chr, range(min_index, max_index)):
    if c in used_chars:
        offset = step * used_chars.find(c)
        description = data[c]["description"]
    else:
        offset = 65535
        description = "unused"
    print(f"         !byte <{offset} ; {description}")

print()
print("_PelicanPrimeOffsetHi")
for c in map(chr, range(min_index, max_index)):
    if c in used_chars:
        offset = step * used_chars.find(c)
        description = data[c]["description"]
    else:
        offset = 65535
        description = "unused"
    print(f"         !byte >{offset} ; {description}")

print()
print(f"_PelicanPrimeShift0")
for c in used_chars:
    print(f"         ; {data[c]['description']}")
    for rawbits in data[c]["rawbits"]:
        bits = rawbits[::-1] + "0000000" + rawbits[::-1]
        byte1 = "%0" + bits[:7]
        print(f"         !byte {byte1}")
