class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1==s2:
            return True
        diff=[]
        n=len(s1)
        for i in range(n):
            if s1[i]!=s2[i]:
                diff.append(i)
        if len(diff)!=2:
            return False
        return s1[diff[0]]==s2[diff[1]] and s1[diff[1]]==s2[diff[0]]