# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 == None and list2 == None:
            return None
        elif list1 == None or list2 == None:
            return list1 if list2 == None else list2

        node1 = None
        node2 = None
        result = None

        if list1.val <= list2.val:
            node1 = list1
            node2 = list2
            result = list1
        else:
            node1 = list2
            node2 = list1
            result = list2

        while node1 != None:
            cond = False
            if node1.next == None:
                while node2 != None and node2.val >= node1.val:
                    newNode = ListNode(node2.val, node1.next)
                    node1.next = newNode
                    node1 = node1.next
                    node2 = node2.next
                    cond = True
            elif node1.next != None:
                maxVal = node1.next.val
                while node2 != None and node2.val >= node1.val and node2.val < maxVal:
                    newNode = ListNode(node2.val, node1.next)
                    node1.next = newNode
                    node1 = node1.next
                    node2 = node2.next
                    cond = True
            if cond == False:
                node1 = node1.next

        return result


class Solution2:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)

    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)

    node1.next = node2
    node2.next = node3

    node4.next = node5
    node5.next = node6

    A = Solution2()
    newHead = A.mergeTwoLists(node1, node4)

    while newHead:
        print(newHead.val, end=', ')
        newHead = newHead.next
    print()

