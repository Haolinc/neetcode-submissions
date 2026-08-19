class LinkedList:
    class Node:
        def __init__(self, val: int):
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self):
        self.size = 0
        self.head = self.Node(0)
        self.tail = self.Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, index: int) -> int:
        if index >= self.size: return -1
        currentNode = self.head.next
        while index > 0:
            currentNode = currentNode.next
            index -= 1
        return currentNode.val
        
    def insertHead(self, val: int) -> None:
        newNode = self.Node(val)
        temp = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = temp
        temp.prev = newNode
        self.size += 1
        

    def insertTail(self, val: int) -> None:
        newNode = self.Node(val)
        temp = self.tail.prev
        self.tail.prev = newNode
        newNode.next = self.tail
        newNode.prev = temp
        temp.next = newNode
        self.size += 1
        

    def remove(self, index: int) -> bool:
        if index >= self.size: return False
        currentNode = self.head.next
        while index > 0:
            currentNode = currentNode.next
            index -= 1
        temp = currentNode.prev
        temp.next = currentNode.next
        currentNode.next.prev = temp
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        val = []
        currentNode = self.head.next
        while currentNode is not self.tail:
            val.append(currentNode.val)
            currentNode = currentNode.next
        return val
        
