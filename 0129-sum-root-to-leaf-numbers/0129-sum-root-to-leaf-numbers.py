# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:

        # def dfs(node: TreeNode | None, curr_sum: int):
        #     if not node:
        #         return 0

        #     curr_sum = curr_sum * 10 + node.val

        #     if not node.left and not node.right:
        #         return curr_sum
            
        #     return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
            
        # return dfs(root, 0)

        # ------------------------------------------------------------------ #

        if not root:
            return 0
        
        total_sum = 0
        stack = [(root, 0)]
        while stack:
            node, curr_sum = stack.pop()

            curr_sum = curr_sum * 10 + node.val

            if not node.left and not node.right:
                total_sum += curr_sum
            
            if node.right:
                stack.append((node.right, curr_sum))
            if node.left:
                stack.append((node.left, curr_sum))
        
        return total_sum