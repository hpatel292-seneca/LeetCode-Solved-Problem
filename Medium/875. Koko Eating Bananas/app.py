from math import ceil
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def check(num):
            total=0
            for i in piles:
                total+=ceil(i/num)
                # total+=1
            return total
        
        left=0
        right=max(piles)
        curr=float('inf')
        while right>=left:
            mid=(right+left)//2
            totalHours=check(mid)
            if totalHours<=h:
                curr=min(curr, mid)
                right=mid-1
            else:
                left=mid+1
        
        return curr

sol=Solution()
sol.minEatingSpeed([3, 6, 7, 11], 8)