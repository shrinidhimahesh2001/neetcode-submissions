class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        row = len(grid)
        col = len(grid[0])
        visited = set()
        def bfs(r,c):
            queue = collections.deque()
            queue.append((r,c))
            visited.add((r,c))
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            while queue:
                ro,co = queue.popleft()
                for dr,dc in directions:
                    if (ro+dr in range(row) and co+dc in range(col) and grid[ro+dr][co+dc] == "1" and (ro+dr,co+dc) not in visited):
                        visited.add((ro+dr,co+dc))
                        queue.append((ro+dr,co+dc))
            return visited

        for r in range(row):
            for c in range(col):
                if (grid[r][c] =="1" and (r,c) not in visited):
                    bfs(r,c)
                    island+=1
                    #visited.add((r,c])
        return island
        