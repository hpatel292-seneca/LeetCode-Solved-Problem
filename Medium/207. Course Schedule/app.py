class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        prereq_adj=[[] for _ in range(numCourses)]
        for i in prerequisites:
            prereq_adj[i[1]].append(i[0])

        stack=[]
        visited=set()
        stack.append(0)
        arr=[]
        while stack:
            curr=stack.pop()
            visited.add(curr)
            arr.append(curr)
            for i in prereq_adj[curr]:
                if i in visited:
                    return False
                elif i not in visited:
                    stack.append(i)
        
        return numCourses==len(arr)
    
sol=Solution()
sol.canFinish(5, [[1,4],[2,4],[3,1],[3,2]])