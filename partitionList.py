# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first = ListNode(-1, None)
        f_head = first
        second = ListNode(-1, None)
        s_head = second

        while head:
            if head.val >= x:
                second.next = head
                second = second.next
            else:
                first.next = head
                first = first.next
            head = head.next

        first.next = s_head.next
        second.next = None

        return f_head.next
