# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        tempHead = ListNode(-1, None)
        temp = tempHead

        countNode = head
        count = 1
        cur = head.next

        while cur:
            if cur.val != countNode.val:
                if count == 1:
                    temp.next = ListNode(countNode.val, None)
                    temp = temp.next
                countNode = cur
                count = 1
            elif cur.val == countNode.val:
                count += 1

            cur = cur.next

        if count == 1:
            temp.next = ListNode(countNode.val, None)
        
        return tempHead.next

if __name__ == "__main__":
    seven = ListNode(5, None)
    six = ListNode(4, seven)
    five = ListNode(4, six)
    four = ListNode(3, five)
    three = ListNode(3, four)
    two = ListNode(2, three)
    one = ListNode(1, two)

    s = Solution()

    head = s.deleteDuplicates(one)

    print("==========================================")

    while head:
        print(head.val)
        head = head.next
