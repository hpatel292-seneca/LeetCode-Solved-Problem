class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=curr_zero=0
        max_len=0
        for right in range(len(nums)):
            if nums[right]==0:
                curr_zero+=1

            while curr_zero>k:
                if nums[left]==0:
                    curr_zero-=1
                left+=1
            
            max_len=max(max_len, right-left+1)
        
        return max_len

sol=Solution()
sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)