# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        result = ListNode(0, None)
        resultNode = result
        l1Copy = l1
        l2Copy = l2
        prev = None

        x = 0
        while l1Copy and l2Copy:
            current = l1Copy.val + l2Copy.val + x
            resultNode.val = current % 10
            x = current // 10
            resultNode.next = ListNode()
            prev = resultNode
            resultNode = resultNode.next
            l1Copy = l1Copy.next
            l2Copy = l2Copy.next

        if l1Copy == None:
            while l2Copy:
                resultNode.val = (l2Copy.val + x) % 10
                x = (l2Copy.val + x) // 10
                l2Copy = l2Copy.next
                resultNode.next = ListNode()
                prev = resultNode
                resultNode = resultNode.next
        elif l2Copy == None:
            while l1Copy:
                resultNode.val = (l1Copy.val + x) % 10
                x = (l1Copy.val + x) // 10
                l1Copy = l1Copy.next
                resultNode.next = ListNode()
                prev = resultNode
                resultNode = resultNode.next

        if x == 0:
            prev.next = None
        else:
            resultNode.val = x
        return result

if __name__ == "__main__":
    print(8 // 10)
