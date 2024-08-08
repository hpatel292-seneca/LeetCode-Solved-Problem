class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])

        def isValid(x,y):
            return 0<=x<m and 0<=y<n and grid[x][y]==1
        
        directions=[(1,0), (-1,0), (0,1), (0,-1)]
        numOfFresh=0
        queue=deque()
        # first insert all rotten orange to queue
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    numOfFresh+=1
        
        if len(queue)==0 and numOfFresh>0:
            return -1
        elif len(queue)==0:
            return 0
        level=0
        while queue:
            length=len(queue)
            for _ in range(length):
                (x,y)=queue.popleft()
                for i,j in directions:
                    x1=x+i
                    y1=y+j
                    if isValid(x1,y1):
                        queue.append((x1,y1))
                        grid[x1][y1]=2
                        numOfFresh-=1
            if len(queue)>0:
                level+=1
        
        if numOfFresh==0:
            return level
        
        return -1

# Time complexity is O(m*n)
# Space complexity is O(m*n)