import sys
input = sys.stdin.readline
n = int(input())
# print(arr)
s,e = 1,1
total = 1
cnt = 0

while s<=e and e < n:
    # print(s,e)
    if total == n:
        cnt +=1
        e += 1
        total += e
    elif total < n:
        e +=1
        total += e
    elif total > n:
        total -= s
        s += 1

print(cnt +1)