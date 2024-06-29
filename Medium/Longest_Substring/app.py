class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        j=0
        length=1
        for index in range(1, len(s)):
            substring = s[i:j+1]
            if s[index] in substring:
                subIndex=substring.index(s[index])
                i=i+subIndex+1
                j=j+1
                if j-i+1 > length:
                    length=j-i+1
            else:
                j=j+1
                length=length+1
        
        return length

s="abcabcbb"
l = Solution()
l.lengthOfLongestSubstring(s)