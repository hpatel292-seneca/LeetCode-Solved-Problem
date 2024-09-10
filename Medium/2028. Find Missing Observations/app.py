class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        total_rolls=len(rolls)+n
        total=total_rolls*mean
        remaining_total=total-sum(rolls)
        if remaining_total<n or remaining_total>6*n:
            return []
        
        ans=[]
        def backtrack(curr):
            if len(curr)==n:
                if sum(curr)==remaining_total:
                    ans=curr[:]
                return
            elif sum(curr)>remaining_total:
                return
            last=curr[-1]
            for i in range(last, 7):
                curr.append(i)
                backtrack(curr)
                curr.pop()
        
        for i in range(1, 7):
            if ans!=[]:
                break
            backtrack([i])
        return ans
            
sol=Solution()
sol.missingRolls([3,2,4,3], 4, 2)