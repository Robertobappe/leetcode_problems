# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        p = None
        curr = head
    
        while curr:
            t = curr.next
            curr.next = p
            p = curr
            curr = t
        return p