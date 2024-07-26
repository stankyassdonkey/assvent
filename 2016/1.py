import numpy as np

file = open('1.txt', 'r')
input = file.read()
lines = input.split(", ")


visited = []
hq = []

def check(coords):
    if coords in visited:
        hq.append(coords)
 
def move_xy(last_x, last_y, x_step, y_step,type):
    if type == "x" :
        sign = abs(x_step)/x_step
        for i in range(abs(x_step)) :
            next_x = last_x + sign*(i+1)
            check([int(next_x), last_y])
            visited.append([int(next_x), last_y])
    else:
        sign = abs(y_step)/y_step
        for i in range(abs(y_step)) :
            next_y = last_y + sign*(i+1)
            check([last_x, int(next_y)])
            visited.append([last_x, int(next_y)])


starting_dir = 0
directions = ["N", "E", "S", "W"]
multiplier = [1,1,-1,-1]

def main():
    x,y = 0,0
    current_dir = starting_dir
    for instructions in lines:
        dir = instructions[0]
        steps = int(instructions[1:])
        last_dir = directions[current_dir]

        if dir == "L" :
            current_dir -= 1
        elif dir == "R" :
            current_dir += 1

        if current_dir == 4 or current_dir == -5 :
            current_dir = 0

        index = directions.index(last_dir)

        if dir == "L" and  (last_dir == "N" or last_dir == "S") :
            move_xy(x, y, -1*steps*multiplier[index], 0, "x")
            x -= steps*multiplier[index]
 
        elif dir == "L" and  (last_dir == "E" or last_dir == "W") :
            move_xy(x, y, 0, steps*multiplier[index], "y")
            y += steps*multiplier[index]
 
        elif dir == "R" and  (last_dir == "N" or last_dir == "S") :
            move_xy(x, y, steps*multiplier[index], 0, "x")
            x += steps*multiplier[index]

        elif dir == "R" and  (last_dir == "E" or last_dir == "W") :
            move_xy(x, y, 0, -1*steps*multiplier[index], "y")
            y -= steps*multiplier[index]

        

main()


# print(visited)
print(hq)



