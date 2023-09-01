# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        if root == None:
            return True
        else:
            if self.checkLeft(root, root.left) and self.checkRight(root, root.right):
                return self.isValidBST(root.left) and self.isValidBST(root.right)
            else:
                return False

    def checkLeft(self, root, check):
        if check == None:
            return True

        if root.val > check.val:
            return self.checkLeft(root, check.left) and self.checkLeft(root, check.right)
        else:
            return False

    def checkRight(self, root, check):
        if check == None:
            return True

        if root.val < check.val:
            return self.checkRight(root, check.left) and self.checkRight(root, check.right)
        else:
            return False

if __name__ == "__main__":
    node = TreeNode(2)
    node2 = TreeNode(1)
    node3 = TreeNode(3)
    node.left = node2
    node.right = node3
    A = Solution()
    print(A.isValidBST(node))
