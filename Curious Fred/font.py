#!/usr/bin/env python3

height = 14
all_chars = list(map(chr, range(0x21, 0x60)))

data = {}
with open("font-master.txt", "r") as f:
    for c in all_chars:
        data[c] = {}
        data[c]["description"] = f.readline().strip()[1:]
        data[c]["Left"] = []
        data[c]["Right"] = []
        for row in range(height):
            data[c]["Left"].append(f.read(7))
            data[c]["Right"].append(f.read(7))
            f.readline()

print("; Curious Fred pixel font")
print("; (c) 2022-3 by 4am")
print("; license:Open Font License 1.1, see OFL.txt")
print("; This file is automatically generated")
print()
print(f"kFontDataMin = {hex(ord(all_chars[0]))} ; ASCII value of first character")
for side in ("Left", "Right"):
    for row in range(height):
        print(f"FontData{side}Row{row}")
        for c in all_chars:
            print(f"         !byte %1{data[c][side][row][::-1]} ; {data[c]['description']}")
