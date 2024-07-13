class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr=0
        left=0
        right=0
        res=0
        for i in range(k):
            right+=1
            curr+=nums[i]
        res=curr
        for right in range(len(nums)):
            curr+=nums[right]-nums[left]
            left+=1
            res=max(res, curr)
        return res/k
    
sol=Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))