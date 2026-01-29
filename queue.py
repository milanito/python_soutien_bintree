# queue.py

class Queue:
    def __init__(self):
        self._data = []
        self._head = 0  # index of current front element

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        if self.isempty():
            raise IndexError("dequeue from empty queue")

        e = self._data[self._head]
        self._head += 1

        # Optional cleanup to avoid memory growth
        if self._head > 64 and self._head * 2 >= len(self._data):
            self._data = self._data[self._head :]
            self._head = 0

        return e

    def isempty(self):
        return self._head >= len(self._data)

    def __len__(self):
        return len(self._data) - self._head
