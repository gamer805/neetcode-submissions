"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        random_hash = {}
        
        curr = head
        while curr:
            random_hash[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            if curr.next:
                random_hash[curr].next = random_hash[curr.next]
            if curr.random:
                random_hash[curr].random = random_hash[curr.random]
            curr = curr.next
        
        return random_hash[head]
        