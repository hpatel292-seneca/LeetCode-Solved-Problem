class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if abs(ord(i)-ord(stack[-1]))==32:
                    stack.pop()
                else:
                    stack.append(i)
        return "".join(stack)