# Algorithm

<br>

## stack

- 먼저 들어간 자료가 나중에 나오는 자료구조 (후입선출)

- 자료를 넣는 push 함수와 자료를 빼는 pop 함수 (empty, full 등 ..)

- stack 구현

  ```python
  class stack:
      def __init__(self):
          self.stack_items = []
  
      # pop
      def pop(self):
          item_length = len(self.stack_items)
          # 스택이 비어있을 경우
          if item_length < 1:
              print("Stack is empty!")
              return False
          # else 가장 위에 있는 item을 반환하며 삭제
          result = self.stack_items[item_length - 1]
          del self.stack_items[item_length - 1]
          return result
  
      # push
      def push(self, x):
          self.stack_items.append(x)
  
      # isEmpty
      def isEmpty(self):
          return not self.stack_items
  
  # test
  test = stack()
  test.push(1)
  test.push(3)
  test.push(5)
  print(test.stack_items)
  print(test.pop())
  print(test.pop())
  print(test.pop())
  print(test.isEmpty())
  ```

  ```[1, 3, 5]
  5
  3
  1
  True```
  ```

- stack class

  ```python
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
  ```

  ```
  olleH
  ```

  

