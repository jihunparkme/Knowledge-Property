#  **Data structure** 

<br>

## 선형 자료구조

- 한 종류의 데이터가 선처럼 길게 나열된 자료구조
- 모든 자료에 O(1)으로 접근이 보장되는 자료구조에는 배열과 해시(key:value)가 있음
- 파이썬에서는 (배열=리스트), (해시=딕셔너리)
- 하단부터는 모든 자료에 O(1) 접그이 보장되지 않는 자료구조를 설명

<br>

### Stack

- 먼저 들어간 자료가 나중에 나오는 자료구조 (후입선출)

- 자료를 넣는 push 함수와 자료를 빼는 pop 함수 (empty, full 등 ..)

- 시간 복잡도

  - push : O(1)
  - pop : O(1)

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
  	st = stack()
  	result = ""
  	for i in str:
  		st.push(i)
  	while st.isEmpty() != True:
  		result += st.pop()
  	return result
  
  if __name__ == "__main__":
  	print(reverseString("Hello"))
  ```

  ```
  olleH
  ```


- stack 구현

  ```python
  class stack:
      def __init__(self):
          self.items = []
  
      # pop
      def pop(self):
          item_length = len(self.items)
          # 스택이 비어있을 경우
          if item_length < 1:
              print("Stack is empty!")
              return False
          # else 가장 위에 있는 item을 반환하며 삭제
          result = self.items[item_length - 1]
          del self.items[item_length - 1]
          return result
  
      # push
      def push(self, x):
          self.items.append(x)
  
      # isEmpty
      def isEmpty(self):
          return not self.items
  
  if __name__ == "__main__":
      # test
      test = stack()
      test.push(1)
      test.push(3)
      test.push(5)
      print(test.items)
      print(test.pop())
      print(test.pop())
      print(test.pop())
      print(test.isEmpty())
  ```

  ```[1, 3, 5]
  5
  3
  1
  True
  ```

<br>

### Queue

- 먼저 들어간 자료가 먼저 나오는 자료구조 (선입선출)

- 자료를 넣는 Enquueu 함수와 자료를 빼는 Dequeue 함수

- 시간 복잡도

  - enqueue : O(1)
  - dequeue : O(N)

- Queue class

  ```python
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
  ```

  ```
  size : 3
  1
  3
  5
  True
  ```

- Queue 구현

  ```python
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
  ```

<br>

### Deque

- stack가 queue의 융합
- 양쪽 끝에서 삽입과 삭제가 모두 가능
- 보통 입력이나 출력 중 하나를 한 쪽 입구만 가능하게 제한하는 형태가 많이 쓰임

<br>

### Linked list

- = 연결 리스트, 값과 다음 노드를 가짐

- 중간에서 삽입 삭제 가능

- 원소들이 흩어져있어 구현체의 속도가 느리기 때문에 잘 사용되지는 않는 편

  ```python
  # Node
  class Node(object):
      def __init__(self, data):
          self.data = data
          self.next = None
  
  # Singly linked list
  class LinkedList():
      def __init__(self):
          self.head = None
          self.tail = None
  
      # Add new node at the end of the linked list
      def enqueue(self, node):
          if self.head == None:
              self.head = node
              self.tail = node
          else:
              self.tail.next = node
              self.tail = self.tail.next
  
      def dequeue(self):
          if self.head == None:
              return -1
  
          v = self.head.data
          self.head = self.head.next
  
          if self.head == None:
              self.tail = None
          return v
  
      # print
      def print(self):
          obj = self.head
          string = ""
          while obj:
              string += str(obj.data)
              if obj.next:
                  string += " -> "
              obj = obj.next
          print(string)
  
  
  if __name__ == "__main__":
      list = LinkedList()
      # Add object
      list.enqueue(Node(1))
      list.enqueue(Node(2))
      list.enqueue(Node(3))
      list.enqueue(Node(4))
      list.print()  # 1->2->3->4
      # Delete object
      print(list.dequeue())
      print(list.dequeue())
      list.print()  # 3->4
  ```

  ```
  1 -> 2 -> 3 -> 4
  1
  2
  3 -> 4
  ```

  <br>

### 선형 구조의 자료 탐색법

- 순차 탐색

  - 시작점부터 순차적으로 탐색
  - 모든 데이터를 탐색할 경우 O(n)

- 이분 탐색

  - 순차 탐색보다 더 빠르속도를 기대, O(log<sub>2</sub>N)

  - 중간값에서 시작하여 매번 일정한 조건에 따라 어떤 방향의 중간값으로 탐색할지 결정

  - 특수한 기준으로 정렬되어있는 상태에서 사용 가능

    ```python
    import math
    
    def binarySearch(arr, n):
        start = 0
        end = len(arr)-1
        while end-start >= 0:
            mid = math.ceil((start+end)/2)
            # 어떤 방향의 중간값으로 탐색할지 결정
            if arr[mid]==n:
                return mid+1
            if arr[mid]<n:
                start = mid+1
            else:
                end = mid-1
        return -1;
    
    if __name__ == "__main__":
        arr = [1,3,4,6,7,9,13,15]
        num = 3
        print(binarySearch(arr, num))
    ```

    ```
    2
    ```

    

<br>

## 비선형 자료구조