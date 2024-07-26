from math import comb
file = open('10.txt', 'r')
input = file.read()
lines = input.split("\n")

for i in range (len(lines)):
    lines[i] = int(lines[i])

lines.sort()
diff = []

index = []

for i in range(len(lines) - 1):
    num = (lines[i+1] - lines[i])
    # diff.append(num)

    if num == 1 :
        index.append(i)

# result = dict((i, diff.count(i)) for i in diff)
# print((result[1]+1)*(result[3]+1))
# print(result)

print(index)

def check(indx,lst):
    if (indx+1 < len(lst)) and ((lst[indx+1]-lst[indx]) == 2):
        return 1
    else :
        return 0

row = []
indx = []

def in_a_row(lst):
    consec = 0
    count = 0
    for i in range(len(lst)):
        if (i+1 < len(lst)) and ((lst[i+1]-lst[i]) == 1):
            consec += 1
        else:
            if consec != 0 :
                # indx.append(i)
                count += check(i,lst)
                row.append(consec)
                consec = 0
    print(row,count)
    calc(row,count)

def calc(rows,counts):
    sum_1 = 1
    for i in rows:
        sum_1 *= 2**(i)
    sum = sum_1 #* 2*counts
    print(sum)


in_a_row(index)