import sys
from itertools import combinations
input = sys.stdin.readline
n,k = map(int, input().strip().split())
result = 0
s = [i+1 for i in range(n)]

# print(combinations(s,k))
for i in combinations(s,k):
    result+=1
print(result)