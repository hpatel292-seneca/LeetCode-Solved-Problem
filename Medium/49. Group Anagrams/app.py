from collections import defaultdict 

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group=defaultdict(list)
        for i in strs:
            key=sorted(i)
            group[key].append(i)
        
        return group.values()
    
sol=Solution()
sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])