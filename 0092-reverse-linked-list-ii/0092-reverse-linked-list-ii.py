# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        
        # dummy = ListNode(0, head)
        # curr = head
        # left_prev = dummy

        # for i in range(left - 1):
        #     temp = curr
        #     curr = curr.next
        #     left_prev = temp
        

        # prev = None
        # for i in range(right - left + 1):
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        
        # left_prev.next.next = curr
        # left_prev.next = prev

        # return dummy.next

        #---------------------------------#
        dummy = ListNode(0, head)
        prev = dummy

        for i in range(left - 1):
            prev = prev.next
        
        curr = prev.next

        for i in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        
        return dummy.next

        