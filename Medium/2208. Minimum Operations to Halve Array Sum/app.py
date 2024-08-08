import heapq
class Solution(object):
    def halveArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSum=sum(nums)
        targetSum=currSum/2.0

        iteration=0
        nums=[-num for num in nums]
        heapq.heapify(nums)

        while currSum>targetSum:
            highestNum=abs(heapq.heappop(nums))
            half=highestNum/2.0
            currSum-=half
            heapq.heappush(nums, -half)
            iteration+=1
        
        return iteration
