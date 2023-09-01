# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def traditionalReverseLinkedList(head: ListNode):
    if head.next == None:
        return head
    last = traditionalReverseLinkedList(head.next)
    head.next.next = head
    head.next = None
    return last

class Solution:
    def reverseBetween(self, head: [ListNode], left: int, right: int) -> [ListNode]:
        if left == 1:
            successor = None
            def reverseFirstN(head, n):
                global successor
                if n == 1:
                    successor = head.next
                    return head
                last = reverseFirstN(head.next, n - 1)
                head.next.next = head
                head.next = successor
                return last
            return reverseFirstN(head, right)

        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    head = node1
    while head:
        print(head.val)
        head = head.next

    print('------------------------')

    head = node1
    newHead = traditionalReverseLinkedList(head)
    while newHead:
        print(newHead.val)
        newHead = newHead.next
