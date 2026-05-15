# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        storing = []
        while head:
            storing.append(head.val)
            head = head.next
            
        noN = ListNode(0)
        current = noN
        for i in range(len(storing)):
            if n != len(storing) - i:
                current.next = ListNode(storing[i])
                current = current.next

        return noN.next