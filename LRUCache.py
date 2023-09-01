class LRUCache:
    class Node:
        def __init__(self, key, val, next=None, prev=None):
            self.next = next
            self.prev = prev
            self.key = key
            self.val = val

    def __init__(self, capacity: int):
        self.head = self.Node(None, None)
        self.tail = self.Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dic = {}

        self.cap = capacity
        self.total = 0
    
    def add_node(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
    
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.remove_node(node)
            self.add_node(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node = self.dic[key]
            self.remove_node(old_node)
            new_node = self.Node(key, value)
            self.add_node(new_node)
            self.dic[key] = new_node
        else:
            if self.total == self.cap:
                self.dic.pop(self.head.next.key)
                self.remove_node(self.head.next)
                node = self.Node(key, value)
                self.add_node(node)
                self.dic[key] = node
            else:
                node = self.Node(key, value)
                self.add_node(node)
                self.dic[key] = node
                self.total += 1



if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    print(lRUCache.get(1))
    lRUCache.put(3, 3)
    print(lRUCache.get(2))
    lRUCache.put(4, 4)
    print(lRUCache.get(1))
    print(lRUCache.get(3))
    print(lRUCache.get(4))