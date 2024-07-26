file = open('1.txt', 'r')
input = file.read()
lines = input.split("\n")
import time
sums = []

t1 = time.time()

def loop(start):
    found = None
    for num in lines:
        start += int(num)
        if start not in sums:
            sums.append(start)
            found = False
        else:
            found = True
            t2 = time.time()
            print(start)
            print(t2-t1)
            break
    last = start
    if not found :
        loop(last)
 
loop(0)

