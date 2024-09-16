class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res=[]
        start=float('inf')
        end=float('inf')
        for i in range(len(nums)):
            if start==float('inf'):
                start=nums[i]
                continue
            else:
                if nums[i-1]+1==nums[i]:
                    end=nums[i]
                else:
                    if start!=float('inf') and end!=float('inf'):
                        res.append(str(start)+"->"+str(end))
                        end=float('inf')
                        start=nums[i]
                    else:
                        res.append(str(start))
                        start=nums[i]
                        end=float('inf')
        if start is not float('inf') and end is not float('inf'):
            res.append(str(start)+"->"+str(end))
            end=True
        else:
            res.append(str(start))
            end=True
        return res

sol=Solution()
sol.summaryRanges([0,2,3,4,6,8,9])