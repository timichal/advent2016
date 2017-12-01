with open("day01") as file:
	for line in file:
		inp = line.strip().split(", ")

coords = [0, 0]

coordslist = []
found = False

angle = 0
for step in inp:
	if step[0] == "R":
		angle += 90
	elif step[0] == "L":
		angle -= 90

	angle = angle % 360

	for i in range(int(step[1:])):
		if angle == 0:
			coords[0] += 1
		elif angle == 180:
			coords[0] -= 1
		elif angle == 90:
			coords[1] += 1
		elif angle == 270:
			coords[1] -= 1

		if coords in coordslist and found == False:
			print("First point visited twice:", sum([abs(coord) for coord in coords])) # part 2
			found = True
		coordslist.append(coords[:])

print("Total distance:", sum([abs(coord) for coord in coords])) # part 1