# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      
      #creating a new list means you need a dummy node
        dummy = ListNode(0)
        curr = dummy
        carry = 0


      #keep going through the numbers as long as there is something to add
        while l1 or l2 or carry:

            #you will get an error if you access null.val so make sure there is something there
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10

            curr.next = ListNode(digit)
            curr = curr.next


            #ptr.next throws an error if you are on null.next so make sure there is something there first
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
