file = open('day4.txt', 'r')
input = file.read()
lines = input.split("\n\n")


def check_num(board ,number, board_num):       
    for columns in board :
        for nums in columns :
            if nums == number :
                mark_num(board_num,columns.index(nums),board.index(columns))
                # print(board.index(columns),columns.index(nums))
                # print(board)
                break

def mark_num(board_num,row,columns):
    score[board_num][columns][row] = "%"


def check_bingo(board_num,num):
    column_score=[0,0,0,0,0]
    for columns in score[board_num]:
        num_index = 0
        row_points = 0
        for nums in columns:
            if nums == "%":
                # output += "X"
                column_score[num_index] += 1
                # print(columns.index(nums))
                row_points += 1
                # print(board_num, column_score)
            if (row_points == 5 and board_num not in bingoed) or (5 in column_score and board_num not in bingoed):
                bingoed.append(board_num)
                print("Board:",board_num, "Num:",num)
                calc_points(board_num,num)

            num_index += 1

def calc_points(board_num,num):
    points = 0
    for columns in score[board_num]:
        for nums in columns:
            if nums != "%" :
                points+= int(nums)
    print(points*int(num))

bingoed = []
score = []

for num in (lines[0].split(",")):
    for board_num in range(len(lines)-1):
        bingo_matrix =[[0]*5,[0]*5,[0]*5,[0]*5,[0]*5,]
        bingo = (lines[board_num+1].split("\n"))
        x = 0
        y = 0
        for columns in range(len(bingo)):
            split_bingo = bingo[columns].split(" ")
            for numbers in split_bingo :
                if numbers.isnumeric() == False :
                    split_bingo.remove(numbers)
            for numbers in split_bingo :
                # print(numbers,y,x)
                bingo_matrix[y][x] = numbers
                if x == 4 :
                    x = 0
                else:
                    x += 1
            y += 1
        if len(score) < len(lines)-1 :
            score.append(bingo_matrix)
        check_num(bingo_matrix,num,board_num)
        check_bingo(board_num,num)
    
        