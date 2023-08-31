# https://www.acmicpc.net/problem/1654
import sys
input = sys.stdin.readline
arr = []
k, n = map(int,input().strip().split())
for i in range(k):
    arr.append(int(input().strip()))
# print(k,n,arr)
s = 1    # 0으로 시작하면 안됨: 나누기 0 안됨
e = max(arr)
while s<=e:  # 같아도 멈춰야 함
    mid = (s+e)//2
    result = 0
    for x in arr:
        result += x//mid
    # print(s, mid, e, result)
    if result >= n:      #mid가 너무 작음   # 같아도 해줘야 하는게, 같다 해서 최대길이는 또 아님
        s = mid +1
    else:
        e = mid -1

print(e)   # 최대를 봐야 하기에


