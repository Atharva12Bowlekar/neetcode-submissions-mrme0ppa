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
        old_to_copy = {None: None}

        # First Pass only making nodes and mapping to hash map
        curr = head
        while curr:
            new = Node(curr.val)
            old_to_copy[curr] = new
            curr = curr.next

        # 2nd Pass adding the random and next pointer

        curr = head
        while curr:
            new = old_to_copy[curr]
            new.next = old_to_copy[curr.next]
            new.random = old_to_copy[curr.random]
            curr = curr.next

        return old_to_copy[head]

        





















