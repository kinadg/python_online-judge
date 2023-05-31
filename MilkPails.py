X = eval(input("X: "))
Y = eval(input("Y: "))
M = eval(input("M: "))
i = M // Y
j = M // X
sum = 0

for i in range(0, i):
    for j in range(1, j):
        sum = (i * Y) + (j * X)
        j += 1
        if sum > M:
            break
            print(sum)


