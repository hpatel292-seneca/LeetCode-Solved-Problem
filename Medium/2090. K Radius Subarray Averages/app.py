class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        prefix=[nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i]+prefix[-1])

        res=[-1]*len(nums)
        if k==0:
            return nums
        start=k
        end=len(nums)-k

        while start<end:
            start_index=0
            if start-k>0:
                start_index=start-k
                res[start]=(prefix[start+k]-prefix[start_index-1])//(2*k+1)
            else:
                res[start]=prefix[start+k]//(2*k+1)
            start+=1
        

        return res

Sol=Solution()
print(Sol.getAverages([7,4,3,9,1,8,5,2,6], 3))