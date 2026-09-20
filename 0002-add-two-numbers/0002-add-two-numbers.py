# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        curr = dummy
        num1 = l1
        num2 = l2
        carry = 0

        while num1 or num2 or carry:
            val1 = num1.val if num1 else 0
            val2 = num2.val if num2 else 0

            total_sum = val1 + val2 + carry
            carry = total_sum // 10

            curr.next = ListNode(total_sum % 10)
            curr = curr.next

            if num1: num1 = num1.next
            if num2: num2 = num2.next
        
        return dummy.next



        