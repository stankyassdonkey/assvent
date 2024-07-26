import numpy as np
file = open('day5.txt', 'r')
input = file.read()
lines = input.split("\n")

def get_xy(line):
    x1 = (line[0].split(","))[0]
    y1 = (line[0].split(","))[1]
    x2 = (line[1].split(","))[0]
    y2 = (line[1].split(","))[1]
    return [x1,y1,x2,y2]

def calc_vector(line_segments):
    instructions = []
    for line_segment in line_segments:
        [x1,y1,x2,y2] = get_xy(line_segment)
        if int(x2)-int(x1) == 0:
            instructions.append([x1,y1,(int(y2)-int(y1)),"Y"])
            # print(f"({x1},{y1}),Y :{int(y2)-int(y1)}")

        elif int(y2)-int(y1) == 0:
            instructions.append([x1,y1,(int(x2)-int(x1)),"X"])
            # print(f"({x1},{y1}),X :{int(x2)-int(x1)}")

        elif abs((int(y2)-int(y1))/(int(x2)-int(x1))) == 1:
            instructions.append([x1,y1,(int(x2)-int(x1)),(int(y2)-int(y1))])
            # print(f"({x1},{y1}),{(int(x2)-int(x1))},{(int(y2)-int(y1))}")

    return instructions
    # print(instructions)

def filter_mi(line_segments):
    index = 0
    moved = 0
    for line_segment in line_segments:
        [x1,y1,x2,y2] = get_xy(line_segment)
        if not (x1 == x2 or y1 == y2 or abs(int(y2)-int(y1))/(int(x2)-int(x1)) == 1) :
            line_segments.pop(index)
            line_segments.insert(0,line_segment)
            moved += 1
        index +=1 
    # del line_segments[0:moved]
    # print(line_segments)

def make_diagram():
    xVal = [] 
    yVal= []
    for line_segment in ass:
        [x1,y1,x2,y2] = get_xy(line_segment)
        xVal.extend((int(x1),int(x2)))
        yVal.extend((int(y1),int(y2)))
    diagram = np.zeros((int(max(xVal)-min(xVal)+1),int(max(yVal)-min(yVal))+1))
    return [diagram,int(min(xVal)),int(min(yVal))]
    # print(diagram)

def update_diagram(diagram,vectors):
    xMin = (diagram[1])
    yMin = (diagram[2])
    diagram = diagram[0]
    for instructions in vectors:
        x = int(instructions[0]) -xMin
        y = int(instructions[1]) -yMin
        step = int(instructions[2])
        direction = (instructions[3])
        # X Right
        if direction == "X" and step > 0:
            for i in range(step+1):
                diagram[y,x+i] += 1
        # X Left
        elif direction == "X" and step < 0:
            for i in range(abs(step)+1):
                diagram[y,x+i+step] += 1
        # Y up
        elif direction == "Y" and step > 0 :
            for i in range(step+1):
                diagram[y+i,x] +=1
        # Y down
        elif direction == "Y" and step < 0:
            for i in range(abs(step)+1):
                diagram[y+i+step,x] +=1
        elif isinstance(direction, int):
            for i in range(abs(step)+1):
                # D++
                if step > 0 and direction > 0:
                    diagram[y+i,x+i] +=1
                # D+-
                elif step > 0 and direction < 0:
                    diagram[y-i,x+i] +=1
                # D--
                elif step < 0 and direction < 0:
                    diagram[y+i+step,x+i+direction] +=1
                # D-+  
                elif step < 0 and direction > 0:
                    diagram[y+i,x-i] +=1
    print(diagram)
    points = 0
    for columns in diagram:
        for nums in columns:
            if nums >= 2:
                points +=1
    print(points)

ass = []
for segments in lines:
    ass.append(segments.split(" -> "))

# print(ass)  
filter_mi(ass)
calc_vector(ass)
make_diagram()
update_diagram(make_diagram(),calc_vector(ass))
