# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        elif head.next == None:
            return head

        newHead = head.next
        head.next = head.next.next
        newHead.next = head

        tempPre = newHead
        tempPost = newHead.next.next

        count = 1
        while tempPost != None:
            if count % 2 == 0:
                tempPre.next.next = tempPost.next
                tempPost.next = tempPre.next
                tempPre.next = tempPost

                tempPost = tempPost.next
                tempPost = tempPost.next
                tempPre = tempPre.next

                count += 1
            else:
                tempPre = tempPre.next
                tempPost = tempPost.next

                count += 1

        return newHead

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

    head = node1
    while head:
        print(head.val, end=' ')
        head = head.next
    print()

    A = Solution()
    newHead = A.swapPairs(node1)

    while newHead:
        print(newHead.val, end=' ')
        newHead = newHead.next
    print()
