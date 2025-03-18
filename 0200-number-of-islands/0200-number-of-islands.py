class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        island=0
        rows=len(grid)
        cols=len(grid[0])
        directions=[(0,-1),(0,1),(-1,0),(1,0)]
        def bfs(i,j):
            queue=deque([(i,j)])
            grid[i][j]="-1"
            while queue:
                row,col=queue.popleft()
                for dr,dc in directions:
                    nr=row+dr
                    nc=col+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=="1":
                        queue.append((nr,nc))
                        grid[nr][nc]=-1
        for i in range(0,rows):
            for j in range(0,cols):
                if grid[i][j]=="1":
                    island+=1
                    bfs(i,j)
        return island
        

        