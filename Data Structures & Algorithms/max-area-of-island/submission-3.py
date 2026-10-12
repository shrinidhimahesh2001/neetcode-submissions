class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        length = 0
        totlen = [0]
        visited = set()
        def bfs(grid,r,c):
            queue = collections.deque()
            queue.append((r,c))
            visited.add((r,c))
            length = 1
            while queue:
                ro,co = queue.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    nr = ro+dr
                    nc = co+dc
                    if (0<=nr<rows and 
                    0<=nc<columns and 
                    grid[nr][nc] == 1 
                    and (nr, nc) not in visited):
                        queue.append((nr,nc))
                        visited.add((nr,nc))
                        length+=1
            totlen.append(length)
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r,c) not in visited:
                    bfs(grid,r,c)
        return max(totlen)
        