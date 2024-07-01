# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr=head
        if ptr==None or ptr.next==None:
            return head
        ptr2=head.next
        while ptr2 != None:
            temp=ptr2.next
            ptr2.next=ptr
            ptr=ptr2
            ptr2=temp
        head.next=None
        return ptr
            