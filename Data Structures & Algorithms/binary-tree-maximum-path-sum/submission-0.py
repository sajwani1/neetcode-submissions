# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # global variable storing max sum
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            # Get the max of the left and right subtrees
            # without splitting
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            # Account for negative values by taking max with 0
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Get the max of everything with splitting
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # Return without a split but update res with
            # a split if that is greater
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]

    # Time Complexity: O(n)
    # Space Complexity: O(n)
        