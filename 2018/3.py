import numpy as np

file = open('3.txt', 'r')
input = file.read()
lines = input.split("\n")

d = 1500
fabric = np.zeros((d,d), dtype=int)



def claim (coords, size, id):
    x,y = coords.split(",")[0] , coords.split(",")[1]
    w,h = size.split("x")[0] , size.split("x")[1]
    x = int(x)
    y = int(y)
    w = int(w)
    h =int(h)

    overlap = False

    for j in range(h):
        for i in range(w):
            fabric[x+i][y+j] += 1

gga = []

def check (coords, size, id):
    x,y = coords.split(",")[0] , coords.split(",")[1]
    w,h = size.split("x")[0] , size.split("x")[1]
    x = int(x)
    y = int(y)
    w = int(w)
    h = int(h)

    overlap = False
    for j in range(h):
        for i in range(w):
            if fabric[x+i][y+j] != 1 :
                overlap = True
    if not overlap:
        gga.append(id)


for claims in lines:
    id = claims.split("@")[0]
    coords = claims.split("@")[1].split(":")[0]
    size = claims.split("@")[1].split(":")[1]
    claim(coords,size, id)

for claims in lines:
    id = claims.split("@")[0]
    coords = claims.split("@")[1].split(":")[0]
    size = claims.split("@")[1].split(":")[1]
    check(coords,size, id)

def print_grid():
    for k in fabric:
        output = ""
        for num in k:
            output += str(num)
        print(output)

print(gga)

# def overlap(grid):
#     count = 0
#     for col in fabric:
#         for num in col :
#             if num >= 2:
#                 count += 1
#     print(count)

# overlap(fabric)

