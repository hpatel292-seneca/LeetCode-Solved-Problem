# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=head
        fast=head.next
        dummyNode=ListNode(None, head)
        prev=dummyNode
        while fast:
            if fast and fast.val==slow.val:
                while fast and fast.val==slow.val:
                    fast=fast.next
                slow=fast
                fast=slow.next
            else:
                prev.next=slow
                prev=prev.next
                slow=fast
                fast=slow.next
        
        return dummyNode.next


arr5=ListNode(10, None)
arr4=ListNode(10, arr5)
arr3=ListNode(3, arr4)
arr2=ListNode(2, arr3)
arr1=ListNode(2, arr2)
arr=ListNode(1, arr1)
sol=Solution()
sol.deleteDuplicates(arr)