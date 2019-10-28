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
	st = stack()
	result = ""
	for i in str:
		st.push(i)
	while st.isEmpty() != True:
		result += st.pop()
	return result

if __name__ == "__main__":
	print(reverseString("Hello"))