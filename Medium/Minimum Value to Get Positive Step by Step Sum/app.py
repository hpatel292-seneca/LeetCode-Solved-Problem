class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_value=nums[0]
        prefix=[nums[0]]
        for i in range(1, len(nums)):
            min_value=min(min_value, nums[i]+prefix[-1])
            prefix.append(nums[i]+prefix[-1])
        if min_value>0:
            return 1
        else:
            return abs(min_value)+1
        
sol=Solution()
print(sol.minStartValue([-3,2,-3,4,2]))