# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        def collect_nums(node, num):
            nonlocal nums
            if node.left and node.right:
                collect_nums(node.left, num + str(node.val))
                collect_nums(node.right, num + str(node.val))
            elif node.left:
                collect_nums(node.left, num + str(node.val))
            elif node.right:
                collect_nums(node.right, num + str(node.val))
            else:
                nums.append(int(num + str(node.val)))

        collect_nums(root, "")

        return sum(nums)