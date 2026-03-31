class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        n,m = len(grid),len(grid[0])
        visited =set()
        def dfs(r,c):
            if(r<0 or r>=n or c<0 or c>=m or grid[r][c]=='0' or (r,c) in visited):
                return 
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        count=0
        for r in range(n):
            for c in range(m):
                if grid[r][c]=='1' and (r,c) not in visited:
                    dfs(r,c)
                    count+=1
        return count