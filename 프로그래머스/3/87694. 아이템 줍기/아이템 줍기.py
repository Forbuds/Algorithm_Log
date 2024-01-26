# https://jyeonnyang2.tistory.com/247

def solution(rectangle, characterX, characterY, itemX, itemY):
    from collections import deque
    answer = 0
    dx, dy = [-1,1,0,0], [0,0,1,-1]
    itemX, itemY = itemX*2, itemY*2
    # 모든 좌표값을 두 배로!
    field = [[-1] * 102 for i in range(102)]
    for r in rectangle:
        lx, ly, rx, ry = map(lambda x: x*2,r)
        for i in range(lx,rx+1):
            for j in range(ly,ry+1):
                if lx<i<rx and ly<j<ry:
                    field[i][j] = 0
                elif field[i][j] != 0:     # 다른 직사각형의 내부도 아니면서(0이 아님) 현재 직삭각형의 내부도 아닐 때 (테두리)
                    field[i][j] = 1
    
    q = deque([(characterX*2, characterY*2)])
    visited = [[1] * 102 for i in range(102)]
    visited[characterX * 2][characterY * 2] = 0
    
    while q:
        cx, cy = q.popleft()
        if cx ==itemX and cy == itemY:
            answer = visited[cx][cy] // 2
            break
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            # 현재 좌표가 테두리이고 아직 방문하지 않은 곳이라면 q에 추가 후 visited를 최단거리로 갱신
            if field[nx][ny] ==1 and visited[nx][ny]==1:
                q.append((nx,ny))
                visited[nx][ny] = visited[cx][cy] +1
    
    return answer