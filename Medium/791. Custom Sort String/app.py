class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        seen={}
        for i in s:
            if i not in seen:
                seen[i]=0
            seen[i]+=1
        
        arr=[]
        for i in order:
            if i not in seen:
                continue
            arr.append(i)
            seen[i]-=1
        for key, values in seen.items():
            for i in range(values):
                arr.append(key)
        
        return "".join(arr)
    
sol=Solution()
print(sol.customSortString("bcafg", "abcd"))