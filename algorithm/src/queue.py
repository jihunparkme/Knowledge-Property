class queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

if __name__ == "__main__":
    test = queue()
    test.enqueue(1)
    test.enqueue(3)
    test.enqueue(5)
    print('size : ', test.size())
    print(test.dequeue())
    print(test.dequeue())
    print(test.dequeue())
    print(test.isEmpty())