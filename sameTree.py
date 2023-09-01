# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue = [p]
        q_queue = [q]
        
        while p_queue and q_queue:
            node1 = p_queue.pop(0)
            node2 = q_queue.pop(0)
            if node1 == node2 == None:
                pass
            elif node1 == None or node2 == None:
                return False
            elif node1.val != node2.val:
                return False
            else:
                p_queue.append(node1.left)
                p_queue.append(node1.right)
                q_queue.append(node2.left)
                q_queue.append(node2.right)
    
        if p_queue or q_queue:
            return False
        else:
            return True

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(1)

    node3 = TreeNode(1)
    node4 = TreeNode(1)

    node1.left = node2
    node3.right = node4

    s = Solution()
    print(s.isSameTree(node1, node3))