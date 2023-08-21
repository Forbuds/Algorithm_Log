import sys
input = sys.stdin.readline
n,m = map(int, input().strip().split())

arr_l = set([str(input().strip()) for _ in range(n)])
arr_s = set([str(input().strip()) for _ in range(m)])

# print(n,m,arr_l,arr_s)
arr = sorted(list(arr_l & arr_s))
print(len(arr))
print('\n'.join(arr))