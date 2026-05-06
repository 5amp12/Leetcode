# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycle = set()
        while head:
            origLen = len(cycle)
            cycle.add(head)
            if origLen == len(cycle):
                return True
            head = head.next
        return False