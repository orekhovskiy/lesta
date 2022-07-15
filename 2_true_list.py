class CircularQueue:
    def __init__(self, max_size):
        self.queue = [] * max_size
        self.max_size = max_size

    def enqueue(self, data):
        if len(self.queue) == self.max_size:
            return False
        self.queue.append(data)
        print(self.queue)
        return True

    def dequeue(self):
        if len(self.queue) == 0:
            return None 
        return self.queue.pop(0)


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
