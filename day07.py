import re

with open("day07") as file:
    strings = [line.strip() for line in file]

def isabba(part):
    if part[0] == part[3] and part[1] == part[2] and part[0] != part[1]:
        return True

def getaba(part):
    if part[0] == part[2] and part[0] != part[1]:
        return part[1]+part[0]+part[1]

def stringcheck(string, puzzle_part):
    string_outside = re.sub('\[.*?\]', ' ', string).split()
    string_inside = re.findall('\[.*?\]', string)
    
    if puzzle_part == 1:
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

    if puzzle_part == 2:
        is_ssl = 0
        for part in string_outside:
            if len(part) >= 3:
                for i in range(len(part)-2):
                    if getaba(part[i:i+3]):
                        for subpart in string_inside:
                            if getaba(part[i:i+3]) in subpart:
                                return True
        return False

print(sum([stringcheck(string, 1) for string in strings]))
print(sum([stringcheck(string, 2) for string in strings]))