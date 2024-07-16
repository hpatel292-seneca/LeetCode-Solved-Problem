class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m_sum=0
        curr=0
        left=0
        seen=defaultdict(int)
        for right in nums:
            while seen[right]!=0:  
                seen[nums[left]]-=1
                curr-=nums[left]
                left+=1
            seen[right]+=1
            curr+=right
            m_sum=max(m_sum, curr)
        return m_sum

# time complexity: O(n)
# => As we can see there is another while loop inside of the for loop but if we avg out that while 
#    loop run then it will only run n times for the whole algorithm so it will avg out O(1) this is call Amortized Analysis.

# Space complexirt: O(n)
# => This is worst case complexity as if there as all unique elements  then it will store all elements in hashmap.