# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            level_arr = deque()
            for _ in range(level_size):
                node = queue.popleft()

                if left_to_right:
                    level_arr.append(node.val)
                else:
                    level_arr.appendleft(node.val)
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            res.append(list(level_arr))
            left_to_right = not left_to_right
        
        return res