import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().strip().split()))
arr = sorted(arr)
x = int(input())

s,e = 0,n-1
cnt =0
# print(arr)
while s<e and e<n:
    result = arr[s] + arr[e]
    # print(s,e)
    if result == x :
        cnt += 1
    if result < x :
        s +=1
        continue
    e -=1

print(cnt)