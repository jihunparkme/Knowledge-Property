class queue():
    def __init__(self):
        self.item = []

    def dequeue(self):
        if len(self.item) == 0:
            return -1
        return self.item.pop(0)

    def enqueue(self, n):
        self.item.append(n)
        pass

    def printQueue(self):
        print(self.item)


if __name__ == "__main__":
    lq = queue()
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    lq.enqueue(4)
    lq.enqueue(5)
    lq.printQueue()
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    lq.printQueue()