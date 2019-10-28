class stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def peek(self):
		return self.items[-1]

	def size(self):
		return len(self.items)

	def pop(self):
		return self.items.pop()


def reverseString(str):
	s = stack()
	result = ""
	for i in str:
		s.push(i)
	while s.isEmpty() != True:
		result += s.pop()
	return result

print(reverseString("Hello"))