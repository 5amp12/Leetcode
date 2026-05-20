# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Str = ""
        l2Str = ""
        while l1 or l2:
            if l1:
                l1Str += str(l1.val)
                l1 = l1.next
            if l2:
                l2Str += str(l2.val)
                l2 = l2.next
            
        l1Str = l1Str[::-1]
        l2Str = l2Str[::-1]
        val = int(l1Str) + int(l2Str)
        
        lis = ListNode(0)
        current = lis

        for num in reversed(str(val)):
            current.next = ListNode(int(num))
            current = current.next

        return lis.next