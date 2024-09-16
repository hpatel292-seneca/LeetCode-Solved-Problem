from collections import defaultdict, Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left=0
        res=""
        t=Counter(t)
        have=0
        need=len(t)
        l=0
        r=float('inf')
        counter=defaultdict(int)
        for right in range(len(s)):
            counter[s[right]]+=1
            if counter[s[right]]==t[s[right]]:
                have+=1
            while have==need:
                if right-left < r-l:
                    r=right
                    l=left
                if counter[s[left]]==t[s[left]]:
                    have-=1
                counter[s[left]]-=1
                left+=1
        if right!=float('inf'):
            return ""
        return s[l:r+1]



sol=Solution()
sol.minWindow("ADOBECODEBANC", "ABC")