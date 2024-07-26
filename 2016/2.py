import numpy as np

file = open('2.txt', 'r')
input = file.read()
lines = input.split("\n")

pad = [[1,2,3],
       [4,5,6],
       [7,8,9]]


pad2 = [[0, 0,  1, 0,  0],
        [0, 2,  3, 4,  0],
        [5, 6,  7, 8,  9],
        [0,"A","B","C",0],
        [0, 0, "D", 0, 0]]

directions = ["U","D","L","R"]
movements = np.array([(-1,0),(1,0),(0,-1),(0,1)])


old_coord = np.array([2,0]) 

for sequence in lines:

    for dir in sequence :
        index = directions.index(dir)
        new_coord = np.add(old_coord, movements[index])

        if (-1 in new_coord or 5 in new_coord) :
            None
        elif (pad2[new_coord[0]][new_coord[1]] == 0):
            None
        else:
            old_coord = new_coord

    old_coord = old_coord

    print(pad2[old_coord[0]][old_coord[1]], old_coord)

        

