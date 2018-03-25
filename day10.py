from collections import defaultdict
instructions = defaultdict(list)
bots = defaultdict(list)
outputs = defaultdict(int)

def findnextbot(bots):
    for bot in bots.items():
        if len(bot[1]) == 2:
            return bot[0]
    return "done"

with open("day10") as file:
    for line in file:
        if line.startswith("value"):
            bots[int(line.split()[-1])].append(int(line.split()[1]))
        else:
            instructions[int(line.split()[1])].extend(line.split()[5:7] + line.split()[10:12])

while findnextbot(bots) != "done":
    bot = findnextbot(bots)
    cur_instr = instructions[bot]

    low, high = min(bots[bot]), max(bots[bot])

    # part 1
    if low == 17 and high == 61:
        print("Part 1:", bot)

    if cur_instr[0] == "bot":
        bots[int(cur_instr[1])].append(low)
    elif cur_instr[0] == "output":
        outputs[int(cur_instr[1])] = low
    bots[bot].remove(low)

    if cur_instr[2] == "bot":
        bots[int(cur_instr[3])].append(high)
    elif cur_instr[2] == "output":
        outputs[int(cur_instr[3])] = high
    bots[bot].remove(high)

# part 2
print("Part 2:", outputs[0] * outputs[1] * outputs[2])