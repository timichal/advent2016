import re
strings = []
with open("day07") as file:
	for line in file:
		strings.append(line.strip())

def isabba(part):
	if part[0] == part[3] and part[1] == part[2] and part[0] != part[1]:
		return True

def stringcheck(string):
	string_outside = re.sub('\[.*?\]', ' ', string).split()
	string_inside = re.findall('\[.*?\]', string)
	
	is_abba = 0
	for part in string_outside:
		if len(part) >= 4:
			for i in range(len(part)-3):
				if isabba(part[i:i+4]):
					is_abba = 1

	for part in string_inside:
		if len(part) >= 4:
			for i in range(len(part)-3):
				if isabba(part[i:i+4]):
					is_abba = 0
	if is_abba:
		return True
	else:
		return False
print(sum([stringcheck(string) for string in strings]))