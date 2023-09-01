# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preOrder(node):
    if node is not None:
        print(node.val)
        preOrder(node.left)
        preOrder(node.right)

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root

        stack = [root]
        prev = None
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            if prev == None:
                prev = node
            else:
                prev.left = None
                prev.right = node
                prev = node

        return root
