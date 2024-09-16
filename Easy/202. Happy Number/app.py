class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def helper(number):
            res=0
            s=str(number)
            for i in range(len(s)):
                res+=int(i)*int(i)
            return res
        nums=set()
        while True:
            if n==1:
                return True
            if n in nums:
                return False
            nums.add(n)
            n=helper(n)
            


sol=Solution()
sol.isHappy(11)
