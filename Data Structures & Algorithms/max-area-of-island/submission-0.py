class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 0
        n,m = len(grid),len(grid[0])
        visited =set()
        def dfs(r,c):
            if(r<0 or r>=n or c<0 or c>=m or grid[r][c]==0 or (r,c) in visited):
                return 0
            visited.add((r,c))
            return(1+dfs(r+1,c)+dfs(r,c+1)+dfs(r-1,c)+dfs(r,c-1))
            
            
            
        max_area=0
        for r in range(n):
            for c in range(m):
                if grid[r][c]==1 and (r,c) not in visited:
                    area=dfs(r,c)
                    max_area=max(max_area,area)
        return max_area