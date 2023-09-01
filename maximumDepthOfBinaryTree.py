# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def findMaxDepth(node, depth):
            if node == None:
                return depth
            else:
                depth1 = findMaxDepth(node.left, depth + 1)
                depth2 = findMaxDepth(node.right, depth + 1)
                return max(depth1, depth2)
        
        result = findMaxDepth(root, 0)

        return result        