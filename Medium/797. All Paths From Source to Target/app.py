class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.visited=[]
        self.res=[]
        self.findPath(graph, 0, len(graph)-1)
        return self.res
    
    def findPath(self, graph, start, target):
        self.visited.append(start)
        if start==target:
            self.res.append(list(self.visited))
        else:
            for i in graph[start]:
                self.findPath(graph, i, target)
        self.visited.pop()