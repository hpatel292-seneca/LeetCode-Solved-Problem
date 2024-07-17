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
        dummy=dummyNode
        arr_end=subArr_start=subArr_end=arr_start=None
        index=0
        while dummy:
            if index==left-1:
                arr_end=dummy
                subArr_start=dummy.next
            if index==right:
                arr_start=dummy.next
                subArr_end=dummy
            dummy=dummy.next
            index+=1
            
        curr=subArr_start
        prev=None
        while curr!=arr_start:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        arr_end.next=subArr_end
        subArr_start.next=arr_start

        return head

    

arr5=ListNode(10, None)
arr4=ListNode(5, arr5)
arr3=ListNode(7, arr4)
arr2=ListNode(2, arr3)
arr1=ListNode(1, arr2)
arr=ListNode(4, arr1)
sol=Solution()
sol.reverseBetween(arr, 2, 5)