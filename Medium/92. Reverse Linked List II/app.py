# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or not head.next or left==right:
            return head
        dummyNode=ListNode(0, head)
        curr=dummyNode
        lp=None
        index=0
        while index<(left-1):
            curr=curr.next
            index+=1
        lp=curr
        curr=curr.next
        prev=0
        for _ in range(right-left+1):
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        temp=lp.next
        lp.next=prev
        temp.next=curr

        return dummyNode.next

    

arr5=ListNode(10, None)
arr4=ListNode(5, arr5)
arr3=ListNode(7, arr4)
arr2=ListNode(2, arr3)
arr1=ListNode(1, arr2)
arr=ListNode(4, arr1)
sol=Solution()
sol.reverseBetween(arr, 2, 5)