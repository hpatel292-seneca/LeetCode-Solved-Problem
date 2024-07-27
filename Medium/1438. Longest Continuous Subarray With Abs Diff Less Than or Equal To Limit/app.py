import collections
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        if not nums:
            return 0
        left=0
        max_subarray=0
        d_queue=collections.deque()
        i_queue=collections.deque()
        for right in range(len(nums)):
            while d_queue and d_queue[-1]<nums[right]:
                d_queue.pop()
            d_queue.append(nums[right])

            while i_queue and i_queue[-1]>nums[right]:
                i_queue.pop()
            i_queue.append(nums[right])

            while abs(d_queue[0]-i_queue[0])>limit:
                if d_queue[0]==nums[left]:
                    d_queue.popleft()
                if i_queue[0]==nums[left]:
                    i_queue.popleft()
                left+=1
            
            max_subarray=max(max_subarray, right-left+1)
        
        return max_subarray

