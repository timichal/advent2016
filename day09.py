import re
with open("day09") as file:
    string = file.readline().strip() 

def decompress(string):
    pos = 0
    newstring = ""
    while True:
        exprs = re.search(r"\(\d+x\d+\)", string)
        if exprs:
            newstring += string[pos:exprs.start(0)]
            length, times = int(exprs.group(0).split("x")[0][1:]), int(exprs.group(0).split("x")[1][:-1])
            newstring += string[exprs.end(0):exprs.end(0)+length] * times
            pos = exprs.end(0) + length
            string = string[pos:]
            newstring += string.split("(")[0]
        else:
            break
    return newstring

def decompress2(string):
    while True:
        expression = re.search(r"\(\d+x\d+\)", string)
        if expression:
            length, times = int(expression.group(0).split("x")[0][1:]), int(expression.group(0).split("x")[1][:-1])
            subexpression = string[expression.end(0):expression.end(0)+length]
            if "(" in str(subexpression):
                while "(" in str(subexpression):
                    subexpression = decompress2(subexpression)
                try:
                    subexpression = sum(int(i) for i in subexpression.split())
                except:
                    pass
            else:
                return string[:expression.start(0)] + str(length * times) + " " + string[expression.end(0)+length:]
            if type(subexpression) == int:
                string = string[:expression.start(0)] + " " + str(times * subexpression) + " " + string[expression.end(0)+length:]
        else:
            result = 0
            for part in string.split():
                try:
                    result += int(part)
                except:
                    result += len(part)
            return result

print(len(decompress(string)))
while type(string) != int:
    string = decompress2(string)
print(string)