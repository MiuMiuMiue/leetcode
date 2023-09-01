# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def maxPathSum(self, root) -> int:
        self.maxSum = -99999
        self.nodeMax(root)
        return self.maxSum

    def nodeMax(self, root):
        if root == None:
            return 0

        right = max(self.nodeMax(root.right), 0)
        left = max(self.nodeMax(root.left), 0)

        current = root.val + right + left

        self.maxSum = max(current, self.maxSum)

        return root.val + max(right, left)
