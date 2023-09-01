# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if root == None:
            return []

        queue = [root, '#']
        result = []
        temp = []
        turn = True
        while queue:
            top = queue[0]
            queue = queue[1:]
            if top == '#':
                if turn == True:
                    result.append(temp)
                    turn = False
                elif turn == False:
                    temp.reverse()
                    result.append(temp)
                    turn = True
                temp = []
                if queue:
                    queue.append('#')
            else:
                if top.left != None:
                    queue.append(top.left)
                if top.right != None:
                    queue.append(top.right)
                temp.append(top.val)

        return result

if __name__ == "__main__":
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5
    A = Solution()
    print(A.zigzagLevelOrder(node1))
