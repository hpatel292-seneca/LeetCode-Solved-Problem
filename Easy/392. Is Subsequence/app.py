class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i=0
        j=0
        if len(s)==0:
            return True
        elif len(t)==0:
            return False
        while j < len(t):
            if s[i]==t[j]:
                j+=1
                i+=1
                if i==len(s):
                    return True
            else:
                j+=1
        
        return i==len(s)