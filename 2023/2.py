file = open('2023/2.txt', 'r')
input = file.read()
lines = input.split("\n")

colours = ["red", "green", "blue"]
constrain = [12, 13, 14]

def check(subsets):
    valid = True
    for i, color in enumerate(colours) :
        if color in subsets :
            index = subsets.index(color)
            value = int(subsets[index-2])
            if value == 0:
                value = int(subsets[index-3])*10
            else:
                value = int(subsets[index-2])

            if value > constrain[i]:
                valid = False
    return valid

sum = 0
for games in lines :
    game_num, sets = games.split(':')[0].split('Game')[1], games.split(':')[1]

    valid = True
    for subsets in sets.split(';') :
        if check(subsets) == False :
            valid = False
    if valid :
        print(game_num)
