class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        seen={}
        seen[tuple([0, 0])]=1
        x=0
        y=0
        for i in path:
            if i=='N':
                x+=1
            elif i=='S':
                x-=1
            elif i=='E':
                y+=1
            else:
                y-=1
            if tuple([x,y]) in seen:
                return True
            else:
                seen[tuple([x,y])]=1
        return False 
    
sol=Solution()
sol.isPathCrossing("NESWW")