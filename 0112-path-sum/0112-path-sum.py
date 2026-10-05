# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        
        # targetSum -= root.val
        
        # if not root.left and not root.right:
        #     return targetSum == 0
        
        # return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

        stack = [(root, targetSum - root.val)]

        while stack:
            node, curr_sum = stack.pop()

            if not node.left and not node.right and curr_sum == 0:
                return True
            
            if node.right:
                stack.append((node.right, curr_sum - node.right.val))
            if node.left:
                stack.append((node.left, curr_sum - node.left.val))
        
        return False



            
