from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        seen=defaultdict(int)
        seen[0]=1
        prefix=[nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i]+prefix[-1])
        ans=0
        for i in prefix:
            if i-k in seen:
                ans+=seen[i-k]
            else:
                seen[i]+=1
        
        return ans

sol=Solution()
sol.subarraySum([1,2,3], 3)