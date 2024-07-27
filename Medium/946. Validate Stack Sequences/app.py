class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack=[]
        for element in pushed:
            if popped and element==popped[0]:
                popped.remove(element)
                while popped and stack and stack[-1]==popped[0]:
                    popped.remove(stack[-1])
                    stack.pop()
            else:
                stack.append(element)
        
        for element in popped:
            if element==stack[-1]:
                stack.pop()
            else:
                return False
        return True