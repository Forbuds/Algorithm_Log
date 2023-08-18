import sys
input = sys.stdin.readline

n = int(input())
arr = [ list(map(str,input().strip().split()))+[i] for i in range(n)]
# print(n,arr)
arr = sorted(arr, key = lambda x: (int(x[0]),x[2]))
for i in range(n):
    print(arr[i][0],arr[i][1])