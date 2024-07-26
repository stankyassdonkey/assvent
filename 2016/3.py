file = open('3.txt', 'r')
input = file.read()
lines = input.split("\n")


possible = 0

col1 = []
col2 = []
col3 = []

for lengths in lines:

    lengths = lengths.split()
    lengths = [int(sides) for sides in lengths]

    col1.append(lengths[0])
    col2.append(lengths[1])
    col3.append(lengths[2])

possible = 0

def calc(lst):
    for i in range(int(len(lst)/3)):
        nums = [lst[i*3],lst[i*3+1] ,lst[i*3+2]]
        nums.sort()
        print(nums)
        if nums[0] + nums[1] > nums[2] :
            global possible
            possible += 1


calc(col1)
calc(col2)
calc(col3)

print(possible)


