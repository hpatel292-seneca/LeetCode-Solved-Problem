# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        curr=slow.next
        prev=None
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        slow.next=prev
        printList(head)

def printList(list):
    head=list
    while head:
        print(head.val)
        head=head.next


arr5=ListNode(10, None)
arr4=ListNode(5, arr5)
arr3=ListNode(7, arr4)
arr2=ListNode(2, arr3)
arr1=ListNode(1, arr2)
arr=ListNode(4, arr1)
sol=Solution()
sol.pairSum(arr)

