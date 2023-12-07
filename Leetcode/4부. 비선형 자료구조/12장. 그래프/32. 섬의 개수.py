https://leetcode.com/problems/number-of-islands/description/

200. Number of Islands : Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

  Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
  Output: 1
Example 2:

  Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
  Output: 3
 
Constraints:

  m == grid.length
  n == grid[i].length
  1 <= m, n <= 300
  grid[i][j] is '0' or '1'.

class Solution:
  
    '''
      완전 내 방식 bfs
    '''
  
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid), len(grid[0])
        v = [[0]*len(grid[0]) for _ in range(len(grid))]
        dx, dy = [0,0,1,-1], [1,-1,0,0]
        def bfs(x,y, cnt):

            q = collections.deque([(x,y)])
            v[x][y] = cnt
            while q:
                cx,cy = q.popleft()
                for i in range(4):
                    nx,ny = cx+dx[i], cy+dy[i]
                    if 0<=nx<n and 0<=ny<m and grid[nx][ny]=="1" and v[nx][ny]==0:
                        q.append((nx,ny))
                        v[nx][ny] = cnt


        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and v[i][j] == 0:
                    cnt += 1
                    bfs(i,j,cnt)
                    print(v)
        return cnt

  
    '''
      dfs, 책 풀이
    '''
  
    def numIslands(self, grid: List[List[str]]) -> int:
      '''
        def dfs(i,j):
          if 종료조건:    -> for문에다가 종료조건을 안달고, 아래 동서남북에서도 쓸 수 있도록 dfs에 종료조건 명시
            return
          g[i][j] = 0    -> visited 배열 만들지 않고 '1'이 아닌 아무것으로 grid배열 자체를 바꿔놓기 (공간 효율 up)

          dfs(동); dfs(서); 
          dfs(남); dfs(북);
      '''
      def dfs(i,j):
        if i<0 or i>=len(grid) or \
          j<0 or j>=len(grid[0]) or \
          grid[i][j]!='1':
          return
        grid[i][j] = '0'
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)

      cnt =0
      
      for i in range(len(grid)):
        for j in range(len(grid[0])):
          if grid[i][j]=='1':
            dfs(i,j)
            cnt+=1

      return cnt
      
    '''
      공간 효율 최대로 한 bfs
    '''
  
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid), len(grid[0])
        dx, dy = [0,0,1,-1], [1,-1,0,0]
        def bfs(x,y, cnt):

            q = collections.deque([(x,y)])
            grid[x][y] = cnt
            while q:
                cx,cy = q.popleft()
                for i in range(4):
                    nx,ny = cx+dx[i], cy+dy[i]
                    if 0<=nx<n and 0<=ny<m and grid[nx][ny]=="1":
                        q.append((nx,ny))
                        v[nx][ny] = cnt


        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    cnt += 1
                    bfs(i,j,cnt)
        return cnt
