# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        dummy = ListNode(0)
        curr = dummy
        num1 = list1
        num2 = list2

        while num1 and num2:
            if num1.val <= num2.val:
                curr.next = num1
                num1 = num1.next
            else:
                curr.next = num2
                num2 = num2.next
            curr = curr.next
            
        if num1: curr.next = num1
        if num2: curr.next = num2
        
        return dummy.next