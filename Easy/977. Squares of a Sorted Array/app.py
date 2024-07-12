class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[0]*len(nums)
        z=len(nums)-1
        i=0
        j=len(nums)-1
        while i <= j:
            if nums[i]*nums[i] > nums[j]*nums[j]:
                res[z]=nums[i]*nums[i]
                z-=1
                i+=1
            else:
                res[z]=nums[j]*nums[j]
                j-=1
                z-=1
        return res