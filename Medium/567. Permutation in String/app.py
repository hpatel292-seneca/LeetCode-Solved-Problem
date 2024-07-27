class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        hash_1=defaultdict(int)
        hash_2=defaultdict(int)
        def is_same():
            for i in s1:
                if hash_1[i]!=hash_2[i]:
                    return False
            return True
        for i in range(len(s1)):
            hash_1[s1[i]]+=1
            hash_2[s2[i]]+=1
        left=0
        for right in range(len(s1), len(s2)):
            if is_same():
                return True
            hash_2[s2[right]]+=1
            hash_2[s2[left]]-=1
            left+=1
        if is_same():
                return True
        return False
            