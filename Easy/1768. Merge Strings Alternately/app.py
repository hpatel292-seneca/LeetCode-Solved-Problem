class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n=len(word1)
        m=len(word2)
        res=[""]*(n+m)
        i=0
        j=0
        while i<n and i<m:
           res[j]=word1[i]
           j+=1
           res[j]=word2[i]
           j+=1
           i+=1
        while i<n:
            res[j]=word1[i]
            j+=1
            i+=1
        while i<m:
            res[j]=word2[i]
            j+=1
            i+=1
        return "".join(res)     