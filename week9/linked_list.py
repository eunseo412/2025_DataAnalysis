class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head is None

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def printList(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')
    
    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:   # head 삽입
            new_node.next = self.head
            self.head = new_node
            return
        prev = self.head
        for _ in range(index-1):
            if prev is None:
                raise IndexError("Index out of range")
            prev = prev.next
        
        new_node.next = prev.next
        prev.next = new_node

    def delete(self, index):
        # linked list가 비어있나?
        if self.head is None:
            raise IndexError("Index out of range")
        
        # head를 삭제하는지?
        if index == 0:
            self.head = self.head.next
            return
        
        # 그렇지 않을 경우
        prev = self.head
        for _ in range(index-1):
            if prev is None:
                raise IndexError("Index out of range")
            prev = prev.next

        if prev.next is None:
            raise IndexError("Index out of range")
        
        prev.next = prev.next.next

    def get(self, index):
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next

        if current is None:
            raise IndexError("Index out of range")
        
        return current.data
    
    def update(self, index, data):
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
            
        if current is None:
            raise IndexError("Index out of range")
        
        current.data = data