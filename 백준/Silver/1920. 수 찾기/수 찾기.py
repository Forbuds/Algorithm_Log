import sys
input = sys.stdin.readline

n = int(input())
a = set(map(int, input().strip().split()))
m = int(input())
b = list(map(int, input().strip().split()))

# print(n,a,m,b)
for k in b:
    if k in a:
        print(1)
    else:
        print(0)