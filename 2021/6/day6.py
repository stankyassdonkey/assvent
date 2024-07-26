import math

file = open('day6.txt', 'r')
input = file.read()
lines = input.split(",")

multiplier = [0]*5
for num in lines:
    multiplier[int(num)-1] += 1

print(multiplier)

def mutate(nums):
    for i, num in enumerate(nums):
        if num == 0:
            nums[i] = 6
            nums.append(9)
        else:
            nums[i] -= 1

amount = []

for j in range(9):
    nums = []
    nums.append(j)
    count = [0]*9
    for i in range(128):
        mutate(nums)

    for num in nums:
        count[num] += 1

    amount.append(count)

def get_sum(number):
    return sum(amount[number])
    
summa = 0
for i in range(5):
    singlesum = 0
    for j in range(9):
        singlesum += get_sum(j)*amount[i+1][j]
    summa += singlesum*multiplier[i]

print(summa)