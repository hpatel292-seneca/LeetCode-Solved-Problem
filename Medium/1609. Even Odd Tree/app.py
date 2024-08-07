# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        level=0
        que=deque()
        que.append(root)
        while que:
            level_size=len(que)
            if level%2==0:
                last_val=float('-inf')
            else:
                last_val=float('inf')
            for i in range(level_size):
                node=que.popleft()
                if level%2==0:
                    if node.val % 2 == 0 or node.val<=last_val:
                        return False
                    last_val=node.val
                else:
                    if node.val % 2 != 0 or node.val>=last_val:
                        return False
                    last_val=node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            level+=1
        
        return True
                