# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max_depth = 0
        count = 0

        def visit(node, depth):
            nonlocal max_depth, count
            if node == None:
                if max_depth == 0:
                    max_depth = depth
                    count += 1
                elif max_depth == depth:
                    count += 1
                return depth
            else:
                depth_l = visit(node.left, depth + 1)
                if depth_l < max_depth:
                    return depth_l
                depth_r = visit(node.right, depth + 1)
                return depth_r

        visit(root, 0)

        total = count // 2
        total += (2 ** (max_depth - 1) - 1)
        
        return total

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6

    s = Solution()
    print(s.countNodes(node1))
