class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        balls={}
        colors=defaultdict(int)
        n=len(queries)
        res=[0]*n
        r=0
        for i in range(n):
            ball, color = queries[i]
            if ball in balls:
                colors[balls[ball]]-=1
                if colors[balls[ball]]==0:
                    r-=1
            balls[ball]=color
            if colors[color]==0:
                r+=1
            colors[color]+=1
            res[i]=r
        return res

# Time Complexity O(n)
# Space Complexity O(n)