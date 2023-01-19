import sys


n = int(sys.argv[1])
m = int(sys.argv[2])

mas = []
for _ in range(m):
    mas.extend([i for i in range(1, n + 1)])

num = '1'
for i in range(m - 1, len(mas), m-1):
    if mas[i] != 1:
        num += str(mas[i])
    else:
        break

print(num)



