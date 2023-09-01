# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return None

        Find = False
        count = 0

        befRemove = head
        remove = head.next
        node = head

        while node:
            if count == n + 1:
                Find = True
            elif Find == True:
                befRemove = befRemove.next
                remove = remove.next
                node = node.next
            elif Find == False:
                node = node.next
            count += 1
        if count == n:
            return head.next
        else:
            befRemove.next = remove.next

        return head

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    temp = node1
    while temp:
        print(temp.val, end='')
        temp = temp.next
    print()

    A = Solution()
    newHead = A.removeNthFromEnd(node1, 2)

    temp = newHead
    while temp:
        print(temp.val, end='')
        temp = temp.next
    print()

