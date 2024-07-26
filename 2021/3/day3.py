# file = open('day3.txt', 'r')
# input = file.read()
# lines = input.split("\n")
# zeros = [0,0,0,0,0,0,0,0,0,0,0,0]
# ones = [0,0,0,0,0,0,0,0,0,0,0,0]
# for binary in lines:
#     i = 0
#     for num in binary:
#         if num == "0":
#             zeros[i] += 1
#         else:
#             ones[i] += 1
#         i += 1
# gamma = ""
# epsilon = ""
# ccc (12):
#     if zeros[bits] > ones[bits]:
#         gamma += "0"
#         epsilon += "1"
#     else :
#         gamma += "1"
#         epsilon +="0"
# power = (int(gamma, 2))*(int(epsilon, 2))
# print(power)


    
file = open('day3.txt', 'r')
input = file.read()
CO2 = input.split("\n")
Oxygen = input.split("\n")

def check_bit (list ,bit, mode):
    zeros=[0]*(len(list[0]))
    ones=[0]*(len(list[0]))
    for binary in list:
        i = 0
        for num in binary:
            if num == "0":
                zeros[i] += 1
            else:
                ones[i] += 1
            i += 1

    if zeros[bit] <= ones[bit] :
        return mode
    else:
        return abs(mode-1)
           
def update_list(List,mode):
    for bits in range(len(List[0])) :
        if len(List) == 1:
            break
        else:
            index = 0
            moved = 0
            for binary in List :
                if int(binary[bits]) != check_bit(List,bits,mode) :
                    List.pop(index)
                    List.insert(0, binary)
                    moved +=1
                index +=1
            del List[0: moved]
    return List[0]

x = (int(update_list(Oxygen,1),2))
y = (int(update_list(CO2,0),2))

print(x*y)
