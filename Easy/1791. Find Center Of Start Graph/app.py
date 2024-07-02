class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        first=edges[0][0]
        second=edges[0][1]
        third=edges[1][0]
        forth=edges[1][1]
        if third==first or forth==first:
            return first
        else:
            return second