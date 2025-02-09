class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rev(num):
            s=str(num)
            s=s[::-1]
            return int(s)
        pairs=defaultdict(int)
        for i in nums:
            pairs[i-rev(i)]+=1
        res=0
        for v in pairs.values():
            if v>1:
                res+=v*(v-1)/2
        return res % (10**9 + 7)