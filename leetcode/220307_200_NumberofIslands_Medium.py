# Graph, BFS, DFS, Union Find

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

class Solution:
    def dfs(self, grid, visit, y, x):
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not 0<=ny<len(grid) or not 0<=nx<len(grid[0]) or visit[ny][nx]:
                continue
            if grid[ny][nx] == '0':
                continue

            visit[ny][nx] = True
            self.dfs(self,grid, visit, ny, nx)

    def numIslands(self, grid: List[List[str]]) -> int:
        cnt_island = 0
        visit = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1' and not visit[y][x]:
                    visit[y][x] = True
                    self.dfs(grid, visit, y, x)
                    cnt_island += 1
