file = open('day10.txt', 'r')
input = file.read()
lines = input.split("\n")

pairs = ["([{<",")]}>"]
points = [3,57,1197,25137]

# for symbols in lines[0] :
sym = []
for symbol in lines:
    sym.append([*symbol])


def list_to_string(list):
    output = ""
    for symbols in (list) :
        output += symbols
    return output

def filter(line,state):
    filtereded = 0
    line_copy = line
    index = 0
    moved = 0
    if state > 0:
        for symbols in line_copy:
            if symbols in pairs[1] and (line_copy[index-1] == pairs[0][pairs[1].index(symbols)]):
                # print(line_copy[index-1],line_copy[index])
                state += 69
                line_copy.pop(index)
                line_copy.pop(index-1)
                line_copy.insert(0,"6")
                moved += 1
                filtereded += 1
                # print(state)
            else:
                # print(line_copy[index-1],line_copy[index])
                # print(symbols,symbols in pairs[1])
                # print(symbols)
                state -= 1
            index += 1
        # print(filtereded)
        del line_copy[0:moved]
        return filter(line_copy,state)
    else:
        # print(state)
        output = list_to_string(line_copy)
        return (output)


corrupt = [0]*4
corrupt_lines = []
def find_corrupt(filtered,line_num):
    index = 0
    for symbols in filtered:
        if symbols in pairs[1] and (filtered[index-1] != pairs[0][pairs[1].index(symbols)]):
            corrupt[pairs[1].index(symbols)] += 1
            corrupt_lines.append(i)
            break
        index +=1

    
for i in range(len(sym)):
    filtered = filter(sym[i],1)
    find_corrupt(filtered,i)

def calc_points(corrupted):
    syntax = 0
    for boom in range(len(corrupted)):
        syntax += corrupted[boom]*points[boom]
    return syntax

# print(calc_points(corrupt))

# print(corrupt_lines)
autofill_points = [1,2,3,4]

def autofill(input):
    score = 0
    for symbols in input:
        score = score*5 + (autofill_points[pairs[0].index(symbols)])
    return score

scores = []
for lines in range (len(sym)) :
    if lines not in corrupt_lines :
        scores.append(autofill((sym[lines])[::-1]))
        # print(list_to_string(sym[lines]),list_to_string(sym[lines])[::-1])

scores.sort()
print(scores[int((len(scores)-1)/2)])
