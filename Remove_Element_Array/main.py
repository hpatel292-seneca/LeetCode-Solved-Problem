class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        j=len(nums)-1
        while j>i:
            if nums[j]==val:
                del nums[j]
                j=j-1
            else:
                if nums[i]==val:
                    nums[i], nums[j]=nums[j], nums[i]
                    del nums[j]
                    i=i+1
                    j=j-1
                else:
                    i=i+1
        if nums[i]==val:
            i=i-1
        return i+1
        
# leetcode link: https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
# Time Complexity = O(n)