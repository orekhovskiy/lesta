class CircularQueue:
    def __init__(self, max_size):
        self.queue = [] * max_size
        self.head = 0
        self.tail = 0
        self.max_size = max_size

    def enqueue(self, data):
        if self.size() == self.max_size - 1:
            return False
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.max_size
        return True

    def dequeue(self):
        if self.size() == 0:
            return None 
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.max_size
        return data

    def size(self):
        if self.tail >= self.head:
            return (self.tail - self.head)
        return (self.max_size - (self.head - self.tail))


if __name__ == "__main__":
    q = CircularQueue(8)
    print(q.enqueue(1))
    print(q.enqueue(2))
    print(q.enqueue(3))
    print(q.enqueue(4))
    print(q.enqueue(5))
    print(q.enqueue(6))
    print(q.enqueue(7))
    print(q.enqueue(8))
    print(q.dequeue())
    print(q.enqueue(9))
    print(q.dequeue())
    print(q.enqueue(9))
    print(q.dequeue())
    print(q.enqueue(9))
    print(q.dequeue())
    print(q.enqueue(9))
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
