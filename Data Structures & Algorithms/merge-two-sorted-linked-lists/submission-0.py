# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1 
        ptr2 = list2

        dummy = ListNode(0)
        curr = dummy

        while ptr1 and ptr2:

            val1 = ptr1.val
            val2 = ptr2.val

            if val1 <= val2:
                curr.next = ptr1
                ptr1 = ptr1.next
            else:
                curr.next = ListNode(val2)
                ptr2 = ptr2.next
            curr = curr.next
        
        if ptr1:
            curr.next = ptr1

        if ptr2:
            curr.next = ptr2

        return dummy.next