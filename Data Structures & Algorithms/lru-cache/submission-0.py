class Node:
    def __init__(self, key=None, val=None, next=None, prev=None):
        self.key = key
        self.val = val

        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mpp = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

    def insertAtFront(self, node):    
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.mpp:
            return -1
        node = self.mpp[key]
        self.remove(node)
        self.insertAtFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mpp:
            node = self.mpp[key]
            node.val = value
            self.remove(node)
            self.insertAtFront(node)
        else:
            if len(self.mpp) == self.cap:
                node = self.tail.prev
                self.remove(node)
                self.mpp.pop(node.key)
            node = Node(key, value)
            self.insertAtFront(node)
            self.mpp[key] = node
