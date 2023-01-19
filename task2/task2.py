import sys


with open(sys.argv[1], 'r') as file:
    center = [float(num) for num in file.readline().split()]
    r = float(file.readline())**2

with open(sys.argv[2], 'r') as file:
    for line in file:
        point = [float(num) for num in line.split()]
        distance = (center[0] - point[0])**2 + (center[1] - point[1])**2
        if distance == r:
            print(0)
        elif distance < r:
            print(1)
        elif distance > r:
            print(2)
