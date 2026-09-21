"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        old_to_new = {}
        curr = head

        while curr:
            old_to_new[curr] = ListNode(curr.val)
            curr = curr.next
        
        dummy = ListNode(0)
        curr = dummy
        old_curr = head

        while old_curr:
            cloned_node = old_to_new[old_curr]

            curr.next = cloned_node

            if old_curr.random:
                cloned_node.random = old_to_new[old_curr.random]
            else:
                cloned_node.random = None
            
            curr = curr.next
            old_curr = old_curr.next
        
        return dummy.next


        