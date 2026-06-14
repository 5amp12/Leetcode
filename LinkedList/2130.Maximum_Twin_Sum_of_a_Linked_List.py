# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        currentNode = head
        store = []
        largestVal = 0

        while currentNode:
            store.append(currentNode.val)
            currentNode = currentNode.next

        l, r = 0, len(store)-1
        while l < r:
            if largestVal < store[l] + store[r]:
                largestVal = store[l] + store[r]
            l+=1
            r-=1

        return largestVal