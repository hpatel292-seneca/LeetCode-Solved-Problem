class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr=[0]*2
        left=0
        length=0
        for right in nums:
            arr[right]+=1
            if right-left+1 <2:
                continue
            while arr[0]!=arr[1]:
                arr[left]-=1
                left+=1
                if right-left+1<2:
                    break
            if right-left+1>=2:
                length=max(length, right-left+1)
        return length
        
sol=Solution()
sol.findMaxLength([0,1])
