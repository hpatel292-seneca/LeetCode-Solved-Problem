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
    
# Using Fast and slow pointers for sloving this problem with constant time complexity

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
        if head==None or head.next==None or head.next.next==None:
            return False
        p1=head.next
        p2=p1.next

        while p2!=None:
            if p1==p2:
                return True
            else:
                p1=p1.next
                if p2.next == None or p2.next.next==None:
                    return False
                else:
                    p2=p2.next.next
