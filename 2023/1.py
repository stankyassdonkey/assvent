import os

file = open('2023/1.txt', 'r')
input = file.read()
lines = input.split("\n")

for text in lines:
    for char in text:
        if char.isnumeric() :
            print(char)