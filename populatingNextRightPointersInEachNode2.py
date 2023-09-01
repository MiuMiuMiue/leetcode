# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Queue:
    class node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
    
    def put(self, val):
        if self.head == None:
            self.head = self.node(val)
            self.tail = self.head
        else:
            cur = self.node(val)
            self.tail.next = cur
            self.tail = self.tail.next
    
    def get(self):
        cur = self.head
        self.head = self.head.next
        return cur.val
    
    def view(self):
        return self.head.val

    def __bool__(self):
        if self.head == None:
            return False
        else:
            return True

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root

        queue = Queue()
        queue.put(root)
        queue.put("#")

        while queue:
            node = queue.get()
            next_element = queue.view()

            if next_element == None or next_element == "#":
                node.next = None
            else:
                node.next = next_element
            
            if node.left != None:
                queue.put(node.left)
            if node.right != None:
                queue.put(node.right)
            if next_element == "#":
                queue.get()
                if queue:
                    queue.put("#")

        return root

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node7 = Node(7)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node7

    s = Solution()
    s.connect(None)
    