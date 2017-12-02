instructions = []
with open("day02") as file:
	for line in file:
		instructions.append(line.strip())

# part 1
keypad = [[1, 2, 3],
		  [4, 5, 6],
		  [7, 8, 9]]

point = [1, 1]

for instruction in instructions:
	for step in instruction:
		if step == "U" and point[0] > 0:
			point[0] -= 1
		if step == "D" and point[0] < 2:
			point[0] += 1
		if step == "L" and point[1] > 0:
			point[1] -= 1
		if step == "R" and point[1] < 2:
			point[1] += 1
	print(keypad[point[0]][point[1]], end="")	
print()

# part 2
keypad2 = [["", "", 1, "", ""],
		   ["", 2,  3,  4, ""],
		   [5,  6,  7,  8,  9],
		   ["", "A", "B", "C", ""],
		   ["", "", "D", "", ""]]

point2 = [2, 0]

for instruction in instructions:
	for step in instruction:
		if step == "U" and point2[0] > 0:
			if (keypad2[point2[0]-1][point2[1]]):
				point2[0] -= 1
		if step == "D" and point2[0] < 4:
			if (keypad2[point2[0]+1][point2[1]]):
				point2[0] += 1
		if step == "L" and point2[1] > 0:
			if (keypad2[point2[0]][point2[1]-1]):
				point2[1] -= 1
		if step == "R" and point2[1] < 4:
			if (keypad2[point2[0]][point2[1]+1]):
				point2[1] += 1
	print(keypad2[point2[0]][point2[1]], end="")
print()