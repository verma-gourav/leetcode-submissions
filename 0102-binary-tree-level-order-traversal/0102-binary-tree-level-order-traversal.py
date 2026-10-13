# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            level_arr = []
            for _ in range(level_size):
                node = queue.popleft()
                level_arr.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level_arr)
        
        return res