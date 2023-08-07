import sys
input = sys.stdin.readline
g = []
result = -100
r, c = -1, -1
for i in range(9):
    l = list(map(int, input().strip().split()))
    if result <= max(l):
        result =  max(l)
        r = i
        c = l.index(result)

print(f"{result}\n{r+1} {c+1}")