class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in nums:
            i=abs(i)
            if nums[i-1] > 0:
                nums[i-1]= -(nums[i-1])
        index=1
        for i in nums:
            if i >0:
                res.append(index)
            index+=1
        return res
    
nums = [4,3,2,7,8,2,3,1]
sol = Solution()
sol.findDisappearedNumbers(nums)