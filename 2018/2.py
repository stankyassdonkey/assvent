file = open('2.txt', 'r')
input = file.read()
lines = input.split("\n")\

alplabets = "abcdefghijklmnopqrstuvwxyz" 
x = list(alplabets)

def compare(x,y):
    stat = [0]
    for i in range(26):
        if x[i-1] == y[i-1]:
            stat[0] += 1
    return int(stat[0])

for x in lines:
    for y in lines:
        if (compare(x,y)) == 25:
            print(x,y)
            break

