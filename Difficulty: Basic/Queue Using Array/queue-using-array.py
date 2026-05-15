class myQueue:
    def __init__(self, n):
        self.front = 0
        self.rear = -1
        self.capacity = n
        self.size = 0
        self.queue = [None] * n
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def enqueue(self, x):
        if self.isFull():
            return 
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = x
        self.size += 1
    
    def dequeue(self):
        if self.isEmpty():
            return -1
        val = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return val
    
    def getFront(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]
    
    def getRear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]