# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        storing = []
        
        while head:
            storing.append(head.val)
            head = head.next
        print(storing)
        rev = ListNode(0)
        current = rev
        for val in reversed(storing):
            current.next = ListNode(val)
            current = current.next
        
        return rev.next

