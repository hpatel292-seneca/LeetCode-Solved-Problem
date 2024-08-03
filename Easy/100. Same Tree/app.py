# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack=[]
        stack.append((p,q))
        while stack:  
            p,q=stack.pop()
            if p==None and q==None:
                continue
            
            if p==None or q==None:
                return False
            
            if p.val!=q.val:
                return False
            
            stack.append((p.left, q.left))
            stack.append((p.right, q.right))
            
        return True

# Time complexity is O(n) as while loop will once for each node and O(1) work will be done at each node
# Space complexity is O(n) in worst case as the stack with store all elements of the tree.
            