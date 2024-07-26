file = open('day1.txt', 'r')
input = file.read()
lines = input.split("\n")



sum = []
for i in range(len(lines)-2):
    wun = int(lines[0+i])
    too = int(lines[1+i])
    fee = int(lines[2+i])
    sum.append(wun+too+fee)


count = 0
old = 69420
for ass in sum:
    new = int(ass)
    if new>old :
        count+=1
    old = new
print(count)