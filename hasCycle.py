# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        set_nodes = set()
        c = 0

        while len(set_nodes) == c:
            if head is None:
                return False

            set_nodes.add(head)
            c += 1
            head = head.next
        return True