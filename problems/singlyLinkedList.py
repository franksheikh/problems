# 1 -> 
# 2 -> 1

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        if index < 0:
            return -1e
        
        ref = self.head
        
        for i in range(index):
            if ref:
                ref = ref.next
            else:
                return -1
            
        if ref:
            return ref.value
        else:
            return -1

            

    def insertHead(self, val: int) -> None:
        node = Node(val)
        
        if not self.head:
            self.head = self.tail = node
        else:                
            node.next = self.head
            self.head = node
        
    def insertTail(self, val: int) -> None:
        node = Node(val)
        
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
    def remove(self, index: int) -> bool:
        # 1 -> 2 -> 3
        
        if index < 0 or not self.head:
            return False
        
        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return True
        
        ref = self.head
        
        for i in range(index - 1):
            if not ref.next:
                return False
            ref = ref.next
        
        if ref.next == self.tail:
            self.tail = ref
        
        if ref.next:
            ref.next  = ref.next.next
            return True
        else:
            return False
        

    def getValues(self) -> List[int]:
        l = []
        ref = self.head
        while ref:
            l.append(ref.value)
            ref = ref.next
        return l
        