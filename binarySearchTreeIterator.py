# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []
        self.pointer = None

        current = root
        while current:
            self.stack.append(current)
            current = current.left
        
        self.pointer = self.stack[-1].val

    def next(self) -> int:
        result = self.pointer
        node = self.stack.pop()

        if node.right:
            self.stack.append(node.right)
            current = node.right.left

            while current:
                self.stack.append(current)
                current = current.left
        if self.stack:
            self.pointer = self.stack[-1].val

        return result

    def hasNext(self) -> bool:
        if self.stack:
            return True

        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

if __name__ == "__main__":
    def test():
        for i in range(10):
            yield i
    
    for i in test:
        print(i)