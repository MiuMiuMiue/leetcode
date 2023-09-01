# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def arrayToTree(left, right):
            nonlocal in_map

            if left > right:
                return None
            
            root_val = postorder.pop()
            root = TreeNode(root_val)

            root.right = arrayToTree(in_map[root_val] + 1, right)
            root.left = arrayToTree(left, in_map[root_val] - 1)

            return root

        in_map = {key: value for value, key in enumerate(inorder)}

        return arrayToTree(0, len(inorder) - 1)
