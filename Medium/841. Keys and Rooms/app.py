class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        # BFS solution.
        self.res=set()
        self.bfs(rooms, 0, self.res)
        return len(rooms)==len(self.res)

    def bfs(self, graph, start, res=set()):
        visited=[]
        visited.append(start)

        while visited:
            start=visited[0]
            visited.pop(0)
            res.add(start)

            for i in graph[start]:
                if i not in res:
                    visited.append(i)

