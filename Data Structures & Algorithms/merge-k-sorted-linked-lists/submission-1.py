# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            curr_l1 = l1
            curr_l2 = l2
            l3 = ListNode(None)
            curr_l3 = l3
            while curr_l1 and curr_l2:
                if curr_l1.val < curr_l2.val:
                    curr_l3.next = ListNode(curr_l1.val)
                    curr_l1 = curr_l1.next
                else:
                    curr_l3.next = ListNode(curr_l2.val)
                    curr_l2 = curr_l2.next
                curr_l3 = curr_l3.next
            if curr_l1:
                curr_l3.next = curr_l1
            if curr_l2:
                curr_l3.next = curr_l2
            return l3.next
        
        if not lists:
            return None
        
        for i in range(1, len(lists)):
            lists[i] = mergeTwoLists(lists[i], lists[i-1])

        return lists[-1]


        