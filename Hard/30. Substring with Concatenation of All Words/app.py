from collections import Counter, defaultdict
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ans=[]
        n=len(s)
        m=len(words[0])
        words_len=len(words)
        total_words_len=m*len(words)
        words=Counter(words)
        for i in range(n-total_words_len+1):
            left=i
            right=i+m
            counter=defaultdict(int)
            for i in range(words_len):
                curr_str=s[left:right]
                left+=m
                right+=m
                counter[curr_str]+=1   
            if words==counter:
                ans.append(i)
        return ans            
sol=Solution()
sol.findSubstring("barfoothefoobarman", ["foo","bar"])