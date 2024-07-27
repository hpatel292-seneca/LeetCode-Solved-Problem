class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        group={}
        for i in range(len(grid)):
            mul=0
            for j in range(len(grid[i])):
                mul+=((j+1)*grid[i][j])
            group[mul]=1
        res=0
        for i in range(len(grid)):
            mul=0
            for j in range(len(grid[i])):
                mul+=((j+1)*grid[i][j])
            if mul in group:
                res+=1
        return res

sol=Solution()
sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])