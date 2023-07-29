d = [int(input()) for a in range(5)]
if len(d) == 5 and all(1 <= d[i] < d[i + 1] <= 31 for i in range(4)):
    for i in range(4):
        print(d[i + 1] - d[i])