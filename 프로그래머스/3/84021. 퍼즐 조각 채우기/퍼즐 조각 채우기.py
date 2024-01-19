# https://backtony.github.io/algorithm/2022-03-16-algorithm-programmers-level3-24/
def solution(game_board, table):
    from collections import deque
    answer = 0
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    n = len(table)
    
    def rotation(g):
        return list(map(list,zip(*g[::-1])))
    def bfs(x,y,what,flag):
        q = deque([(x,y)])
        x_min, x_max = x,x
        y_min, y_max = y,y
        parts = []
        while q:
            cx, cy = q.popleft()
            parts.append((cx,cy))
            for i in range(4):
                nx, ny = cx+dx[i], cy + dy[i]
                if 0<=nx<n and 0<=ny<n and what[nx][ny]==flag and v[nx][ny]==0:
                    v[nx][ny] = 1
                    x_min, x_max = min(nx,x_min), max(nx,x_max)
                    y_min, y_max = min(ny,y_min), max(ny,y_max)
                    q.append((nx,ny))
                    
        parts = [(a-x_min,b-y_min) for a,b in sorted(parts)]            
        return parts,x_min,y_min
    
    def is_match(parts,blank):
        
        return blank in parts
    
    v = [[0]*n for _ in range(n)]
    parts = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and v[i][j]==0:
                v[i][j] = 1
                parts.append(bfs(i,j,table,1)[0])
    # print('p',parts)
    def printg(g):
        for i in range(len(g)):
            print(g[i])
    
    for k in range(4):
        if k>0:
            game_board = rotation(game_board)
        v = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if game_board[i][j] == 0 and v[i][j]==0:
                    # print('here')
                    v[i][j] = 1
                    blank,x,y = bfs(i,j,game_board,0)
                    # print('b',blank)
                    
                    if is_match(parts,blank):
                        # print('before')
                        # printg(game_board)
                        answer += len(blank)
                        parts.remove(blank)
                        
                        # print('hhh',parts)
                        for a,b in blank:
                            game_board[a+x][b+y]=1
                        # printg(game_board)
        
    return answer