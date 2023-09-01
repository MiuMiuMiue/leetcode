# Definition for a Node.
from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old = head
        new = None
        newHead = None

        while old:
            if not new:
                new = Node(old.val, None, None)

                random = old.random
                if random == None:
                    new.random = None
                else:
                    step = 0
                    cur = head
                    while cur != random:
                        cur = cur.next
                        step += 1

                    new.random = step
                newHead = new
            else:
                new.next = Node(old.val, None, None)
                new = new.next

                random = old.random
                if random == None:
                    new.random = None
                else:
                    step = 0
                    cur = head
                    while cur != random:
                        cur = cur.next
                        step += 1

                    new.random = step

            old = old.next
        
        new = newHead
        while new:
            if new.random != None:
                step = new.random
                cur = newHead
                while step > 0:
                    cur = cur.next
                    step -= 1
                new.random = cur
            new = new.next
        return newHead

if __name__ == "__main__":
    s = Solution()
    five = Node(1, None, None)
    four = Node(10, five, None)
    three = Node(11, four, None)
    two = Node(13, three, None)
    one = Node(7, two, None)
    
    one.random = None
    two.random = one
    three.random = five
    four.random = three
    five.random = one

    head = s.copyRandomList(one)
    print("----")
    while head:
        print(head.val)
        if head.random == None:
            print("no random")
        else:
            print(head.random.val)
        print("==================================")
        head = head.next