class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans={}
        stack=[]

        for i in range(len(nums2)):
            while stack and nums2[stack[-1]]<nums2[i]:
                j=stack.pop()
                ans[nums2[j]]=nums2[i]
            stack.append(i)
        
        res=[]
        for i in nums1:
            if i not in ans:
                res.append(-1)
            else:
                res.append(ans[i])
        return res
sol=Solution()
sol.nextGreaterElement([4,1,2], [1,3,4,2])