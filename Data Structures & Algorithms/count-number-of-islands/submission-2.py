class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set()
        island = 0

        def bfs(grid,r,c):
            queue = collections.deque()
            visited.add((r,c))
            queue.append((r,c))
            while queue:
                ro,co = queue.popleft()
                directions = [[0,-1],[0,1],[1,0],[-1,0]]
                for dr,dc in directions:
                    nr,nc = ro+dr,co+dc
                    if (0<=nr<row) and (0<=nc<col) and grid[nr][nc]=="1" and (nr,nc) not in visited:
                        
                        queue.append((nr,nc))
                        visited.add((nr,nc))

        for r in range(0,row):
            for c in range(0,col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(grid,r,c)
                    island+=1
        return island
        