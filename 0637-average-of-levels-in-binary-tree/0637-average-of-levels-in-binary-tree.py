# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            curr_sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                curr_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            avg = curr_sum / level_size
            res.append(avg)
        
        return res

