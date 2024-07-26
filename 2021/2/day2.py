file = open('day2.txt', 'r')
input = file.read()
lines = input.split("\n")
print(lines)

X = 0
Y = 0
aim = 0

for instuction in lines:
    if instuction[0] == "f" :
        X += int(instuction[-1])
        Y += aim*(int(instuction[-1]))
    elif instuction[0] == "u" :
        # Y -= int(instuction[-1])
        aim -= int(instuction[-1])
    else :
        # Y += int(instuction[-1])
        aim += int(instuction[-1])

print(X,Y)
print(X*Y)