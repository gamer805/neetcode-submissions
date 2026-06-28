# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next and n == 1:
            return None
        
        curr = head
        l = 0
        while curr:
            l += 1
            curr = curr.next
        target = l - n
        if target == 0:
            return head.next
        first, second = head, head.next
        m = 0
        while second and second.next and m < target - 1:
            first = first.next
            second = second.next
            m += 1
        first.next = second.next
        return head


        

        