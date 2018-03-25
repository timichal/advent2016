screen = [50 * ["."] for i in range(6)]
with open("day08") as file:
    cmds = [line.strip() for line in file]

for cmd in cmds:
    if cmd.startswith("rect"):
        x, y = cmd.split(" ")[1].split("x")
        for row in range(int(y)):
            for col in range(int(x)):
                screen[row][col] = "x"

    elif cmd.startswith("rotate"):
        pos = int(cmd.split("=")[1].split()[0])
        by = int(cmd.split("=")[1].split()[2])
        if "row" in cmd:
            screen[pos] = screen[pos][-by:] + screen[pos][:-by]
        elif "column" in cmd:
            column = [screen[row][pos] for row in range(len(screen))]
            column = column[-by:] + column[:-by]
            for row, content in enumerate(column):
                screen[row][pos] = content

lit_pixels = 0
for row in screen:
    for char in row:
        if char == "x":
            lit_pixels += 1
    print(''.join(row))
print(lit_pixels)