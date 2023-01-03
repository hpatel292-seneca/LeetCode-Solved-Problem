class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        max = 0

        while right > left:
            diff = right - left
            a = diff * min(height[left], height[right])
            max = a if a > max else max
            if height[left] > height[right]: right -= 1
            else: left+= 1
        return max

