# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        d = ListNode()
        d_new = d

        while list1 and list2:
            if list1.val <= list2.val:
                d_new.next = list1
                list1 = list1.next
            else:
                d_new.next = list2
                list2 = list2.next
            d_new = d_new.next
            
        if list1:
            d_new.next = list1
        if list2:
            d_new.next = list2

        return d.next
