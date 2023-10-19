import sys
input = sys.stdin.readline
n = int(input())
# print(arr)
start,end = 1,1
total = 1
cnt = 0

while end < n:
    if total < n:
        end += 1
        total += end
    elif total > n:
        total -= start
        start += 1
    else:
        cnt += 1
        end += 1
        total += end

print(cnt +1)