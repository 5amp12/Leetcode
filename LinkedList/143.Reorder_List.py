# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        storing = []
        curr = head
        while curr:
            storing.append(curr.val)
            curr = curr.next

        l, r = 0, len(storing)-1
        for i in range(len(storing)):
            if i%2 == 0:
                head.val = storing[l]
                l+=1
            else:
                head.val = storing[r]
                r-=1
            head = head.next
