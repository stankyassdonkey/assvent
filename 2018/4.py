file = open('4.txt', 'r')
input = file.read()
lines = input.split("\n")


for records in lines:
    print(records)