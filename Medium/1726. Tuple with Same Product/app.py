class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pairs=defaultdict(int)
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                pairs[nums[i]*nums[j]]+=1
        res=0
        for i in pairs.values():
            if i<=1:
                continue
            res+=((2*i)*(2*(i-1)))
        return res

