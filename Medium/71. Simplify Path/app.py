class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        index=0
        while index<len(path):
            if path[index]=='/':
                index+=1
                continue
            else:
                temp=[]
                while path[index]!='/':
                    temp.append(path[index])
                    index+=1
                index+=1
                s="".join(temp)
                if s==".":
                    continue
                elif s=="..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(s)
        res=[]
        if len(stack)==0:
            return '/'
        else:
            for i in stack:
                res.append('/')
                res.append(i)
        
        return "".join(res)

sol=Solution()
sol.simplifyPath("/.../a/../b/c/../d/./")