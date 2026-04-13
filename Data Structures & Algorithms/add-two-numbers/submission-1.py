# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2

        dummy = ListNode()
        head = dummy

        rem = 0
        while curr1 or curr2 or rem:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0

            total = val1 + val2 + rem
            rem = total // 10
            total_to_add = total % 10 

            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None

            temp = ListNode(total_to_add)
            head.next = temp
            head = head.next

        return dummy.next
















        