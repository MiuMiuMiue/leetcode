# Definition for singly-linked list.
from queue import PriorityQueue

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        head = pointer = ListNode(0)
        pq = PriorityQueue()

        for index, tempHead in enumerate(lists):
            if tempHead:
                pq.put((tempHead.val, index))

        while not pq.empty():
            value, index = pq.get()
            pointer.next = lists[index]
            pointer = pointer.next
            lists[index] = lists[index].next
            if lists[index]:
                pq.put((lists[index].val, index))

        return head.next

    def mergeKListsUsingDivideAndConquer(self, lists: list[ListNode]) -> ListNode:
        if lists == [] or (len(lists) == 1 and lists[0] == None):
            return None
        length = len(lists)
        interval = 1

        while interval < length:
            for i in range(0, length - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

if __name__ == "__main__":
    node_a = ListNode(1)
    node_b = ListNode(4)
    node_c = ListNode(5)
    node_a.next = node_b
    node_b.next = node_c
    head1 = node_a

    node_d = ListNode(1)
    node_e = ListNode(3)
    node_f = ListNode(4)
    node_d.next = node_e
    node_e.next = node_f
    head2 = node_d

    node_g = ListNode(2)
    node_h = ListNode(6)
    node_g.next = node_h
    head3 = node_g

    A = Solution()
    newHead = A.mergeKLists([head1, head2, head3])
