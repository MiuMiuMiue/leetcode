# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = 0
        num2 = 0
        count = 0
        add1 = True
        add2 = True
        while True:
            if add1:
                num1 += l1.val * (10 ** count)
            if add2:
                num2 += l2.val * (10 ** count)
            if (l1.next == None) and (l2.next == None):
                break
            if l1.next != None:
                l1 = l1.next
            elif l1.next == None:
                add1 = False
            if l2.next != None:
                l2 = l2.next
            elif l2.next == None:
                add2 = False
            count += 1
        sum = num1 + num2
        sumList = list(str(sum))
        result = ListNode(int(sumList[len(sumList) - 1]), None)
        start = result
        for index in range(len(sumList) - 2, -1, -1):
            newNode = ListNode(int(sumList[index]), None)
            start.next = newNode
            start = start.next
        return result

if __name__ == "__main__":
    head = ListNode(9, None)
    start = head
    for x in range(6):
        newNode = ListNode(9, None)
        start.next = newNode
        start = start.next
    head2 = ListNode(9, None)
    start2 = head2
    for y in range(3):
        newNode = ListNode(9, None)
        start2.next = newNode
        start2 = start2.next
    a = Solution()
    a.addTwoNumbers(head, head2)
