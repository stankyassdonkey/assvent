file = open('day7.txt', 'r')
input = file.read()
lines = input.split(",")

numbers =(list(map(int, lines)))

total = []
for steps in range (min(numbers),max(numbers)+1):
    fuel = 0
    for x in numbers:
        fuel += (abs(x - steps))*(abs(x - steps)+1)/2
    total.append([fuel,steps])

least_fuel = []
for i in total:
    least_fuel.append(i[0])

print(min(least_fuel))
