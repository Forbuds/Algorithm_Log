import sys
input = sys.stdin.readline
from itertools import combinations
m,n = map(int, input().strip().split())
arr = list(map(str, input().strip().split()))
arr_a = [k for k in arr if k in 'aeiou' ] # 두개 골라잡고 / 그다음에 한번에
arr_b = list(set(arr)-set(arr_a))
# print(arr_a)
# print(arr_b)
s = []
for i in range(m-3+1):
    # print(i + 1, m - 3 - i + 2)
    if i+1>len(arr_a) or m-3-i+2>len(arr_b):
        continue
    else:
        # print(i + 1, m - 3 - i + 2)
        for x in combinations(arr_a,i + 1):
            for y in combinations(arr_b,m - 3 - i + 2):
                s.append(''.join(sorted(x+y)))
for x in sorted(s):
    print(x)