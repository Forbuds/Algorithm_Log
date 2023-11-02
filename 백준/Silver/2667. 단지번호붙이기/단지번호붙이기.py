import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
g = []
for i in range(n):
    g.append(list(map(int,list(input().strip()))))
v = [[0]*(n) for i in range(n)]
cnt = 1   # v 에 넣어줄 껀데 헷갈리지 않기 위해 1부터 넣어준다.
dx = [0,0,1,-1]
dy = [1,-1,0,0]
s = []

def bfs(i,j,cnt):
    q = deque([(i,j)])      # BFS는 큐로
    result = 1
    v[i][j] = cnt           # 큐에 넣고, v 채우고
    while q:
        x, y = q.popleft()
        for i in range(4):  # 4방을 돌아간다.
            nx, ny = x + dx[i],y + dy[i]
            if (0 <= nx < n and 0 <= ny < n) and v[nx][ny] == 0 and g[nx][ny] == 1 :
                # 제1 조건: 범위 내에 있는가
                # 제2 조건: 방문하지 않았는가
                # 제3 조건: 단지인가
                q.append((nx,ny))        # 큐에 넣고, v 채우고
                result += 1              # 단지에 있는 아파트 개수
                v[nx][ny] = cnt          # 몇 번째 단지인지
    s.append(result)

for i in range(n):
    for j in range(n):
        if v[i][j] ==0 and g[i][j]==1: # 단지 돌면서 1을 만나면 바로 bfs를 돌아간다
            bfs(i,j,cnt)               # 몇 번째 단지인지
            cnt+=1
# print(v)
print(cnt-1)
print('\n'.join(map(str,sorted(s))))
