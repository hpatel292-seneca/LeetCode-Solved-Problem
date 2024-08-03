# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        arr1=[]
        arr2=[]

        def dfs1(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                arr1.append(node.val)
            dfs1(node.left)
            dfs1(node.right)
        
        def dfs2(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                arr2.append(node.val)
            dfs2(node.left)
            dfs2(node.right)
        
        dfs1(root1)
        dfs2(root2)

        return arr1==arr2

# Time Complexity is O(n) 
# Space Complexity is O(n)