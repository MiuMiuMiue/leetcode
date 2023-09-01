# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k == 0:
            return head

        stack = []
        tail = head
        count = 0
        while tail:
            stack.append(tail)
            count += 1
            tail = tail.next
        k = k % count

        if k == 0:
            return head
        else:
            head = stack[-k]
            tail = stack[-(k + 1)]
            tail.next = None
            stack[-1].next = stack[0]
            return head

if __name__ == "__main__":
    node5 = ListNode(5, None)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    s = Solution()

    head = s.rotateRight(node1, 6)

    while head:
        print(head.val)
        head = head.next
