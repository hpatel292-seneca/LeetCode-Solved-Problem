class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        j=len(s)-1
        res=[""]*len(s)
        while i<=j:
            if 33>ord(s[i])>122:
                
                res[i]=s[i]
                i+=1
            elif 33>ord(s[j])>122:
                res[j]=s[j]
                j-=1
            else:
                abc=ord(s[i])
                res[i], res[j]=s[j], s[i]
                i+=1
                j-=1
        return "".join(res)
    
sol=Solution()
sol.reverseOnlyLetters("a-bC-dEf-ghIj")