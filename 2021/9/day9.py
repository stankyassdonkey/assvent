file = open('day9.txt', 'r')
input = file.read()
lines = input.split("\n")

heightmap = []
for num in lines:
    heightmap.append([*num])

width = len(heightmap[0])
length = len(heightmap)

corners = [[0,0],[width-1,0],[0,length-1],[width-1,length-1]]
edges = [[0,length-1],[0,width-1]]
def location_type(y,x):
    #Corners 0TL 1TR 2BL 3BR
    if [x,y] in corners:
        return corners.index([x,y])
    #Left edge
    elif x == 0 :
        return 4
    #Right Edge
    elif x == (width -1) :
        return 5
    #Top Edge
    elif y == 0 :
        return 6
    #Bottom Edge
    elif y == (length -1) :
        return 7
    #Middle
    else :
        return 8

low_points=[[],[]]

def calc_risk(y,x,type):
    risk = 0
    height = int(heightmap[y][x])
    if type == 0 :
        if height < int(heightmap[0][1]) and height < int(heightmap[1][0]) :
            low_points[0].append([y,x])
            low_points[1].append(type)
    elif type == 1:
        if height < int(heightmap[0][width-2]) and height < int(heightmap[1][width-1]) :
            low_points[0].append([y,x])
            low_points[1].append(type)
    elif type == 2:
        if height < int(heightmap[length-2][0]) and height < int(heightmap[length-1][1]) :
            low_points[0].append([y,x])
            low_points[1].append(type) 
    elif type == 3:
        if height < int(heightmap[length-2][width-1]) and height < int(heightmap[length-1][width-2]) :
            low_points[0].append([y,x])
            low_points[1].append(type) 
    elif type == 4:
        if height < int(heightmap[y-1][0])  and height < int(heightmap[y+1][0])and height < int(heightmap[y][1]):
            low_points[0].append([y,x])
            low_points[1].append(type)
    elif type == 5:
        if height < int(heightmap[y-1][x])  and height < int(heightmap[y+1][x])and height < int(heightmap[y][x-1]):
            low_points[0].append([y,x])
            low_points[1].append(type)
    elif type == 6:
        if height < int(heightmap[0][x-1])  and height < int(heightmap[0][x+1])and height < int(heightmap[1][x]):
            low_points[0].append([y,x])
            low_points[1].append(type)
    elif type == 7:
        if height < int(heightmap[y][x-1])  and height < int(heightmap[y][x+1])and height < int(heightmap[y-1][x]):
            low_points[0].append([y,x])
            low_points[1].append(type)
    elif type == 8 :
        if height < int(heightmap[y-1][x])  and height < int(heightmap[y+1][x]) and height < int(heightmap[y][x+1]) and height < int(heightmap[y][x-1]):
            low_points[0].append([y,x])
            low_points[1].append(type)       

    # return risk

# print(calc_risk(2,2,8))

# total_risk = 0
for columns in range(length):
    for rows in range(width):
        calc_risk(columns,rows,location_type(columns,rows))


ass = 0
def calc_riskV2(y,x,type):
    height = int(heightmap[y][x])
    if True:
        if type == 0 :
            if [y,x] not in coords :
                # right
                if (int(heightmap[0][1]) - height) == 1:
                    calc_riskV2(0,1,6)
                #down
                if (int(heightmap[1][0]) - height) == 1:
                    calc_riskV2(1,0,4)
                coords.append([y,x])

        elif type == 1:
            # Left
            if [y,x] not in coords :
                if (int(heightmap[0][width-2]) - height) == 1:
                    calc_riskV2(0,width-2,6)

                # down
                if (int(heightmap[1][width-1]) - height) == 1:
                    calc_riskV2(1,width-1,5)
                coords.append([y,x])
        elif type == 2:
            if [y,x] not in coords :
                # up
                if (int(heightmap[length-2][0]) - height) == 1:
                    calc_riskV2(length-2,0,4)

                # right
                if (int(heightmap[length-1][1]) - height) == 1:
                    calc_riskV2(length-1,1,7)
                coords.append([y,x])
        elif type == 3:
            if [y,x] not in coords :
            # up
                if (int(heightmap[length-2][width-1]) - height) == 1:
                    calc_riskV2(length-2,width-1,5)

                # left
                if (int(heightmap[length-1][width-2]) - height) == 1:
                    calc_riskV2(length-1,width-2,7)
                coords.append([y,x])
        elif type == 4:
            if [y,x] not in coords :
                if (int(heightmap[y-1][0]) - height) == 1:
                    if (y-1)== 0:
                        calc_riskV2(y-1,0,corners.index([0,y-1]))
                    else:
                        calc_riskV2(y-1,0,4)
                # down
                if (int(heightmap[y+1][0]) - height) == 1:
                    if (y+1) == 0:
                        calc_riskV2(y+1,0,corners.index([0,y+1]))
                    else:
                        calc_riskV2(y+1,0,4)

                # right
                if (int(heightmap[y][1]) - height) == 1:
                    calc_riskV2(y,1,8)
                coords.append([y,x])
        elif type == 5:
            if [y,x] not in coords :
            #up
                if (int(heightmap[y-1][x]) - height) == 1:
                    if [x,y-1] in corners:
                        calc_riskV2(y-1,x,corners.index([x,y-1]))
                    else:
                        calc_riskV2(y-1,x,5)
                # down
                if (int(heightmap[y+1][x]) - height) == 1:
                    if [x,y+1] in corners:
                        calc_riskV2(y+1,x,corners.index([x,y+1]))
                    else:
                        calc_riskV2(y+1,x,5)

                # left
                if (int(heightmap[y][x-1]) - height) == 1:
                    calc_riskV2(y,x-1,8)
                coords.append([y,x])
        elif type == 6:
            if [y,x] not in coords :
                #left
                if (int(heightmap[0][x-1]) - height) == 1:
                    if (x-1) == 0:
                        calc_riskV2(0,x-1,corners.index([x-1,0]))
                    else:
                        calc_riskV2(0,x-1,6)
                # right
                if (int(heightmap[0][x+1]) - height) == 1:
                    if [x+1,0] in corners:
                        calc_riskV2(0,x+1,corners.index([x+1,0]))
                    else:
                        calc_riskV2(0,x+1,6)
                # down
                if (int(heightmap[1][x]) - height) == 1:
                    calc_riskV2(1,x,8)
                coords.append([y,x])
        elif type == 7:
            if [y,x] not in coords :
                #left
                if (int(heightmap[y][x-1]) - height) == 1:
                    if [x-1,y] in corners:
                        calc_riskV2(y,x-1,corners.index([x-1,y]))
                    else:
                        calc_riskV2(y,x-1,7)
                # right
                if (int(heightmap[y][x+1]) - height) == 1:
                    if [x+1,y] in corners:
                        calc_riskV2(y,x+1,corners.index([x+1,y]))
                    else:
                        calc_riskV2(y,x+1,7)
                # up
                if (int(heightmap[y-1][x]) - height) == 1:
                    calc_riskV2(y-1,x,8)
                coords.append([y,x])
        
        elif type == 8 :
            if [y,x] not in coords :
            # up
                if (int(heightmap[y-1][x]) - height) == 1:
                    if (y-1) == 0:
                        calc_riskV2(y-1,x,6)   
                    else:
                        calc_riskV2(y-1,x,8)

                #down
                if (int(heightmap[y+1][x]) - height) == 1:
                    if (y+1) == (length-1):
                        calc_riskV2(y+1,x,7)   
                    else:
                        calc_riskV2(y+1,x,8)

                # right
                if (int(heightmap[y][x+1]) - height) == 1:
                    if (x+1) == (width-1):
                        calc_riskV2(y,x+1,5)   
                    else:
                        calc_riskV2(y,x+1,8)

                # left
                if (int(heightmap[y][x-1]) - height) == 1:
                    if (x-1) == 0:
                        calc_riskV2(y,x-1,4)   
                    else:
                        calc_riskV2(y,x-1,8)
                coords.append([y,x])
#0 TL 
# 1 TR 
# 2 BL 
# 3 BR
# 4 Left edge
# 5 Right edge
# 6 top edge 
# 7 bottom edge
# 8 middle



nums = []

for i in range(len(low_points[0])):
    coords = []
    y = low_points[0][i][0]
    x = low_points[0][i][1]
    type = low_points[1][i]
    calc_riskV2(y,x,type)
    for ass in range(100):
        for cord in coords:
            y = cord[0]
            x = cord[1]
            # if heightmap[y][x] == "9":
            #     coords.remove(cord)
                # print("e")
    nums.append(len(coords))
nums.sort()
print(nums)
output = nums[-1]*nums[-2]*nums[-3]
print(output)
print(len(nums))

# coords = []
# for i in range(len(low_points[0])):
#     y = low_points[0][i][0]
#     x = low_points[0][i][1]
#     type = low_points[1][i]
#     calc_riskV2(y,x,type)
#     for ass in range(100):
#         for cord in coords:
#             y = cord[0]
#             x = cord[1]
#             if heightmap[y][x] == "9":
#                 coords.remove(cord)
                # print("e")
    # nums.append(len(coords))
# nums.sort()
# print(nums)
# output = nums[-1]*nums[-2]*nums[-3]
# print(output)
nines = 0

# for y in range(length):
#     for x in range(width):
#         if heightmap[y][x] == "9":
#             nines+=1

# print(length*width)
# print(len(coords)+nines)


# calc_riskV2(2,2,8)
# print(coords)    
# for i in range(2)  :
#     for cord in coords:
#         y = cord[0]
#         x = cord[1]
#         if heightmap[y][x] == "9":
#             coords.remove(cord)

# import numpy as np

# matrix = np.zeros([width,length])
# for ass in range(len(coords)):
#     asss = (coords[ass])
#     matrix[asss[0],asss[1]] = 69


# for cord in coords:
#     y = cord[0]
#     x = cord[1]
#     print(heightmap[y][x])


# print(len(coords))
# print(matrix)