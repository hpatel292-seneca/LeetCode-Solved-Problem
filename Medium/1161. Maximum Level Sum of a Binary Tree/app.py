# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level=0
        max_total=float('-inf')

        queue=deque()
        queue.append(root)
        curr_level=1
        while queue:
            curr_sum=0
            for i in range(len(queue)):
                node=queue.popleft()
                curr_sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if curr_sum>max_total:
                level=curr_level
                max_total=curr_sum
            curr_level+=1
        
        return level

# Time Complexity is O(n), n=num of node
    # Every node will get into loop once
# Space Complexity is O(m), where m is maximum width of tree at any level