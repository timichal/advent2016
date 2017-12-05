from collections import Counter 

codes = []
with open("day06") as file:
	for line in file: 
		codes.append(line.strip())

for char in list(zip(*codes)):
	print(Counter(char).most_common()[-1][0], end="") #[0][0] for part 1
print()