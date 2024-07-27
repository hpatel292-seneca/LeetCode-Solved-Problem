# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        k1=k2=None
        index=1
        ptr=head
        while ptr:
            if index==k:
                k1=ptr
            index+=1
            ptr=ptr.next
        index-=1
        ptr=head
        while index:
            if index==k:
                k2=ptr
                break
            index-=1
            ptr=ptr.next
        k1.val, k2.val=k2.val, k1.val
        return head

arr5=ListNode(10, None)
arr4=ListNode(5, None)
arr3=ListNode(4, arr4)
arr2=ListNode(3, arr3)
arr1=ListNode(2, arr2)
arr=ListNode(1, arr1)
sol=Solution()
sol.swapNodes(arr, 2)