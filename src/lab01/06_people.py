N = int(input())

y = 0
n = 0
i = 1

for i in range(N):
    line = input().split()
    if line[-1].upper() == "TRUE":
        y += 1
    else:
        n += 1

print(y, n)
