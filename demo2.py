class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front =None
        self.rear = None
        self._size = 0

    def enqueue(self, item):
        new_node = Node(item)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            self._size += 1
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty") #this is to print a message if the queue is empty
            return None
        dequeued_item = self.front.data
        self.front = self.front.next
        self._size -= 1
        return dequeued_item
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty") #this is to print a message if the queue is empty
            return None
        return self.front.data
    
    def is_empty(self):
        return self.front is None
    
    def size(self):
        return self._size
    
ll_queue = LinkedListQueue() #this is to create a new queue
ll_queue.enqueue(1) #this is to add an item to the queue
ll_queue.enqueue(2) #this is to add another item to the queue
ll_queue.enqueue(3) #this is to add another item to the queue

print("Queue size:", ll_queue.size()) #this is to print the size of the queue
print("Front item:", ll_queue.peek()) #this is to print the item at the front of the queue
print("Dequeued item:", ll_queue.dequeue()) #this is to remove and return the item from the front of the queue and print it
print("Queue size after dequeue:", ll_queue.size()) #this is to print the size of the queue after dequeueing an item