from collections import defaultdict
class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cal=defaultdict(int)
        n=len(nums)
        for i in range(n):
            cal[i-nums[i]]+=1
        good_pairs=0
        for v in cal.values():
            if v>1:
                good_pairs+=((v*(v-1))/2)
        return (n*(n-1))/2-good_pairs

sol=Solution()
sol.countBadPairs([4,1,3,3])

# Time Complexity: O(n)
# Space Complexity: O(n)
