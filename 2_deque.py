from collections import deque
from typing import Iterable, Optional

class CircularQueue:
    def __init__(self, max_size: int) -> None:
        self.queue = deque(maxlen=max_size)

    def enqueue(self, data: Iterable) -> bool:
        if len(self.queue) == self.queue.maxlen:
            return False
        self.queue.append(data)
        return True

    def dequeue(self) -> Optional[Iterable]:
        if len(self.queue) > 0:
            return self.queue.popleft()
        return None


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
    print(q.enqueue(8))
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
