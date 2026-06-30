# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_l1 = l1
        curr_l2 = l2
        l3 = ListNode(None)
        curr_l3 = l3
        carry = 0
        while curr_l1 or curr_l2:
            if curr_l1 and curr_l2:
                value = curr_l1.val + curr_l2.val + carry
            elif curr_l1:
                value = curr_l1.val + carry
            elif curr_l2:
                value = curr_l2.val + carry
            carry = 0 if value < 10 else 1
            curr_l3.next = ListNode(value%10)
            if curr_l1:
                curr_l1 = curr_l1.next
            if curr_l2:
                curr_l2 = curr_l2.next
            curr_l3 = curr_l3.next
        if carry:
            curr_l3.next = ListNode(carry)
        
        return l3.next
        