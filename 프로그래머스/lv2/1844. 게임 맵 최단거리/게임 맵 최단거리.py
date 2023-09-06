from collections import deque
def solution(maps):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque([(0,0)])
    n = len(maps)
    m = len(maps[0])
    v = [[0]*m for _ in range(n)]
    v[0][0] = 1
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            x_c, y_c = x +dx[i], y+dy[i]
            # if x_c == n-1 and y_c==m-1:
            #     v[n-1][m-1]= v[x][y]+1
            #     break
                # return v[n-1][m-1]
            if 0<=x_c<n and 0<=y_c<m and maps[x_c][y_c]==1 and v[x_c][y_c]==0:
                q.append((x_c,y_c))
                v[x_c][y_c]= v[x][y]+1
    
    # print(answer)
    if v[n-1][m-1]==0:
        return -1
    else:
        return v[n-1][m-1]
        