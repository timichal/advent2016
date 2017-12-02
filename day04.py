from collections import Counter, defaultdict
from string import ascii_lowercase as lc

rooms = []
with open("day04") as file:
	for line in file:
		rooms.append(line.strip())

idsum = 0

def decrypt(room_id, room_name):
	n = room_id % 26 
	rotshift = str.maketrans(lc, lc[n:] + lc[:n])
	return room_name.translate(rotshift)

for room in rooms:
	checksum = room[-6:-1]
	room_id = int(room[-10:-7])
	room_name = room[:-11] 

	most_common = Counter(''.join(room_name.split("-"))).most_common()
	common_dict = defaultdict(list)
	for key, value in most_common:
		common_dict[value].append(key)
	sortlst = []
	for item in common_dict.items():
		sortlst += sorted(item[1])
	if "".join(sortlst[:5]) == checksum:
		idsum += room_id
	
	# part 2
	if "north" in decrypt(room_id, room_name):
		print(room_id)

print(idsum)