# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIndex = 0

        def arrayToTree(left, right):
            nonlocal preIndex
            if left > right:
                return None

            rootValue = preorder[preIndex]
            root = TreeNode(rootValue)
            preIndex += 1

            root.left = arrayToTree(left, inorderMap[rootValue] - 1)
            root.right = arrayToTree(inorderMap[rootValue] + 1, right)

            return root

        inorderMap = {}
        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i

        return arrayToTree(0, len(preorder) - 1)
        

if __name__ == "__main__":
    import numpy as np
    test = np.array([[[1, 2, 3],
                      [3, 3, 3],
                      [4, 4, 4]]])
    test = np.add(test, test)
    print(test)
