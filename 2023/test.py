string = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"

game_num, sets = string.split(':')[0], string.split(':')[1]


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

valid = True
for subsets in sets.split(';') :
    if check(subsets) == False :
        valid = False
print(valid)