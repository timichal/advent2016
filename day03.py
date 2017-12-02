triangles = []
with open("day03") as file:
	for line in file:
		triangles.append(line.strip().split())

triangles_vert = [num for col in list(zip(*triangles)) for num in col]
triangles_vert = [triangles_vert[i:i+3] for i in range(0, len(triangles_vert), 3)]

def is_triangle(a,b,c):
	a, b, c = int(a), int(b), int(c)
	if a + b > c and b + c > a and a + c > b:
		return True

valid_triangles = 0
for triangle in triangles_vert: # or triangles for part 1
 if is_triangle(*triangle):
 	valid_triangles += 1

print(valid_triangles)