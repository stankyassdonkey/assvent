file = open('12.txt', 'r')
input = file.read()
lines = input.split("\n")

input = []
for rows in lines:
     input.append(rows.split("-"))

Start_caves, End_caves, Large_caves, Small_caves = [],[],[],[]

for paths in input:
    Start_caves.append(paths[1-(paths.index("start"))]) if "start" in paths else None
    End_caves.append(paths[1-(paths.index("end"))]) if "end" in paths else None
    for Cave in paths:
        if Cave.isupper() and Cave not in Large_caves :
            Large_caves.append(Cave)
        elif Cave.islower() and (Cave != "start" and Cave != "end") and Cave not in Small_caves :
            Small_caves.append(Cave)

data = [Start_caves,End_caves,Large_caves,Small_caves]

def pathfinder(node):
    available_nodes = []
    for paths in input:
        if node in paths :
            pair = paths[1-(paths.index(node))]
            available_nodes.append(pair) if (pair not in ["start", "end"]) else None
    return available_nodes
        
print(pathfinder("A"))
