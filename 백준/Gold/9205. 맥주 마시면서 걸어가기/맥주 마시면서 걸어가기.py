import sys
from collections import deque
input = sys.stdin.readline
def calc_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [tuple(map(int, input().strip().split())) for i in range(n+2)]
    # print(n,arr)
    def bfs():
        q = deque([arr[0]])
        v = [0]*(n+2)
        v[0] = 1
        result = 0

        while q:
            x,y = q.popleft()
            if (x,y) == arr[-1]:
                result = sum(v)
                break
            # 선형검색
            for i in range(n+2):
                if v[i]==0 and calc_dist(x,y,arr[i][0],arr[i][1])<=1000:
                    q.append((arr[i][0],arr[i][1]))
                    v[i] = 1

        return result

    result = bfs()
    if result == 0:
        print('sad')
    else:
        print('happy')