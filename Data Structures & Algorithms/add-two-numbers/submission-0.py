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
        tail = dummy

        rem = 0
        while curr1 or curr2 or rem:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            total_val = val1 + val2 + rem

            print("val1", val1)
            print("val2", val2)
            print("total_val", total_val)

            rem = total_val // 10
            total_val = total_val % 10

            temp = ListNode(total_val)
            tail.next = temp
            tail = tail.next

            curr1 = curr1.next if curr1 else 0
            curr2 = curr2.next if curr2 else 0
            
        return dummy.next



















        