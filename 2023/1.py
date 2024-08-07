import os

file = open('2023/1.txt', 'r')
input = file.read()
lines = input.split("\n")

def check(line):
    for digit in digit_list :
        if digit in line:
            return (digit_list.index(digit)) + 1
        
digit_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0

for text in lines:
    input = ""
    nums = ""
    for letters in text:

        if not letters.isnumeric() :
            input += letters
        else:
            nums += letters

        result = check(input)
        if type(result) == int :
            last_char = input[-1]
            input = last_char
            nums += str(result)
    values = int(nums[0] + nums[-1])
    sum += values
    print(values)
print(f"Sum : {sum}") 