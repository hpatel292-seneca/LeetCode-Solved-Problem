import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans=[]
        queue=collections.deque()

        for i in range(len(nums)):
            while queue and nums[i]>nums[queue[-1]]:
                queue.pop()
            
            queue.append(i)

            while queue[0]<i-k+1:
                queue.popleft()
            
            if i+1>=k:
                ans.append(nums[queue[0]])

        return ans
    
sol=Solution()
sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)