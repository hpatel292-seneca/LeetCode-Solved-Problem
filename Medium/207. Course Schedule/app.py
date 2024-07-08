class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites)==0:
            return True
        self.prereq_adj=[[] for _ in range(numCourses)]
        for i in prerequisites:
            self.prereq_adj[i[1]].append(i[0])
        
        self.visited=[False for _ in range(numCourses)]
        self.rec_stack=[False for _ in range(numCourses)]
        index=0
        for node in self.prereq_adj:
            if not self.visited[index]:
                if self.is_cycle(index):
                    return False
            index+=1
        return True

    def is_cycle(self, v):
        self.visited[v]=True
        self.rec_stack[v]=True

        for n in self.prereq_adj[v]:
            if not self.visited[n]:
                if self.is_cycle(n):
                    return True
            elif self.rec_stack[n]:
                return True
        
        self.rec_stack[v]=False
        return False

sol=Solution()
sol.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]])