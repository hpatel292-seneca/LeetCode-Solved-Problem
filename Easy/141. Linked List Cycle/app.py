# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodeHash={}
        start=head
        while start!=None:
            if start in nodeHash:
                return True
            else:
                nodeHash[start]= True
                start=start.next
        return False