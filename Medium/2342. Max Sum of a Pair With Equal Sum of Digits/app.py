from collections import defaultdict
class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        groups=defaultdict(list)
        for i in nums:
            total=sum(int(digit) for digit in str(i))
            groups[total].append(i)
        res=-1
        for values in groups.values():
            if len(values) >=2:
                values.sort(reverse=True)
                res=max(res, values[0]+values[1])
        
        return res
                
sol=Solution()
sol.maximumSum([229,398,269,317,420,464,491,218,439,153,482,169,411,93,147,50,347,210,251,366,401])