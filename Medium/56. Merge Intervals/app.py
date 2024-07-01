class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Sorting intervals based on the start (0th index) of intervals
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd= result[-1][1]

            if start <= lastEnd:
                result[-1][1]=max(lastEnd, end)
            else:
                result.append([start, end])
        return result

        


intervals = [[1,3],[8,10],[15,18], [2,6]]
sol = Solution()
print(sol.merge(intervals))