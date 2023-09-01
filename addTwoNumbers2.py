# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        x = 0
        node = None
        while stack1 and stack2:
            num1 = stack1.pop()
            num2 = stack2.pop()
            if node == None:
                node = ListNode((num1 + num2 + x) % 10)
            else:
                tempNode = node
                node = ListNode((num1 + num2 + x) % 10)
                node.next = tempNode
            x = (num1 + num2 + x) // 10

        while stack1:
            num = stack1.pop()
            tempNode = node
            node = ListNode((num + x) % 10)
            node.next = tempNode
            x = (num + x) // 10

        while stack2:
            num = stack2.pop()
            tempNode = node
            node = ListNode((num + x) % 10)
            node.next = tempNode
            x = (num + x) // 10

        if x > 0:
            tempNode = node
            node = ListNode(x)
            node.next = tempNode

        return node
