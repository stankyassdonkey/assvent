file = open('2023/2.txt', 'r')
input = file.read()
lines = input.split("\n")


colours = ["red", "green", "blue"]


def add(col,num) :
    index = colours.index(col)
    cube_num[index].append(int(num))

sum = 0

for string in lines:
    cube_num = [[],[],[]]
    game_num, sets = string.split(':')[0].split(' ')[1], string.split(':')[1]

    for subsets in sets.split(';') :
        split_subsets = subsets.split(',')
        for col_num in split_subsets :
            col, num = col_num.split(' ')[2], col_num.split(' ')[1]

            add(col,num)

    product = 1
    for counts in cube_num :
        product *= max(counts)
    sum += product

print(sum)
