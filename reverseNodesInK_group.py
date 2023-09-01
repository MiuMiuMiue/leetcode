# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseLinkedList(self, head, k):

        # Reverse k nodes of the given linked list.
        # This function assumes that the list contains
        # atleast k nodes.
        new_head, ptr = None, head
        while k:
            # Keep track of the next node to process in the
            # original list
            next_node = ptr.next

            # Insert the node pointed to by "ptr"
            # at the beginning of the reversed list
            print(new_head)
            ptr.next = new_head
            new_head = ptr

            # Move on to the next node
            ptr = next_node

            # Decrement the count of nodes to be reversed by 1
            k -= 1

        # Return the head of the reversed list
        return new_head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        left = None
        right = None
        prev = None
        next = None
        result = None
        first = True
        last = None

        node = head
        count = 0
        while node:
            turn = True
            if count == 0:
                left = node
            elif count == k - 1:
                temp = left
                right = node
                if first == True:
                    result = right
                    first = False
                else:
                    last.next = right
                next = left.next
                left.next = right.next
                prev = left
                left = next

                i = 0
                while i < k - 1:
                    next = left.next
                    left.next = prev
                    prev = left
                    left = next
                    i += 1

                last = temp
                node = left
                count = 0
                turn = False
            if turn:
                node = node.next
                count += 1

        return result

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node5

    temp = node1
    while temp:
        print(temp.val, end="")
        temp = temp.next
    print()

    A = Solution()
    head = A.reverseLinkedList(node1, 2)

    while head:
        print(head.val, end="")
        head = head.next
    print()
