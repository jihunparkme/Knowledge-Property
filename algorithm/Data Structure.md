#  Data structure 

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

- 선형 자료구조가 아닌 모든 자료구조

### 그래프

- 객체들 사이의 관계를 정점(vertex)과 간선(edge)로 나타낸 그림

### 깊이 우선 탐색(DFS)

- Depth First Search

- 방문한 정점으로부터 깊게 들어가며 탐색한 후, 되돌아 나오다가 탐색하지 않은 노드를 탐색하는 방식 

- 깊이가 너무 Depth가 너무 큰 경우, 런타임 에러 발생 우려

- 실행 과정

  1.  정점을 방문
  2. 인접한 정점 중 아직 방문하지 않은 정점을 방문(한 길로 쭉 파고 들어간다)
  3. 더 이상 들어갈 길이 없을 때(인접한 모든 정점이 이미 방문한 정점일 때), 방문하지 않은 인접한 정점을 찾을 때까지 들어간 길을 돌아나옴
  4. 위 과정을 반복

   <img src="..\img\dfs.png" alt="img" style="zoom: 20%;" />
  
  ```python
  def dfs(v):		# 정점 v부터 탐색
      global rst
      if v == 'A':
          visited[v] = True
          rst += v + ' -> '
      for i in Graph[v]:
          if not visited[i]:
              visited[i] = True
              rst += i + ' -> '
              dfs(i)
  
  if __name__ == "__main__":
      Graph = {
          'A': ['B'],
          'B': ['A', 'C', 'H'],
          'C': ['B', 'D', 'G'],
          'D': ['C', 'E'],
          'E': ['D', 'F'],
          'F': ['E'],
          'G': ['D'],
          'H': ['B', 'I', 'J', 'M'],
          'I': ['H'],
          'J': ['H', 'K'],
          'K': ['J', 'L'],
          'L': ['K'],
          'M': ['H']
      }
      visited = dict(zip([v for v in Graph], [False for _ in Graph])) # 방문 여부 체크
      rst = ''
  
      dfs('A')
      print(visited)
      print(rst)
  ```
  ```
  {'A': True, 'B': True, 'C': True, 'D': True, 'E': True, 'F': True, 'G': True, 'H': True, 'I': True, 'J': True, 'K': True, 'L': True, 'M': True}
  
  A -> B -> C -> D -> E -> F -> G -> H -> I -> J -> K -> L -> M
  ```

###  너비 우선 탐색(BFS)

-  Breadth First Search 

-  넓게 퍼져가며 정점을 방문 

- 실행 과정

  1. 첫 정점을 방문
  2. 아직 방문하지 않은 인접한 정점들을 큐에 넣음
  3. 큐에 있는 정점들을 순서대로 방문
  4. 큐에 있는 정점에 대해 인접하면서 아직 방문하지 않은 정점들로 새로운 큐를 구성
  5. 위 과정을 반복

   <img src="..\img\dfs.png" alt="img" style="zoom: 20%;" />

  ```python
  def bfs(v):
      global rst
      visited[v] = True
      queue = [v]
      while queue:
          now = queue.pop(0)
          rst += now + ' -> '
          for i in Graph[now]:
              if not visited[i]:
                  visited[i] = True
                  queue.append(i)
  
  if __name__ == "__main__":
      Graph = {
          'A': ['B'],
          'B': ['A', 'C', 'H'],
          'C': ['B', 'D', 'G'],
          'D': ['C', 'E'],
          'E': ['D', 'F'],
          'F': ['E'],
          'G': ['D'],
          'H': ['B', 'I', 'J', 'M'],
          'I': ['H'],
          'J': ['H', 'K'],
          'K': ['J', 'L'],
          'L': ['K'],
          'M': ['H']
      }
      visited = dict(zip([v for v in Graph], [False for _ in Graph]))
      rst = ''
  
      bfs('A')
      print(visited)
      print(rst)
  ```

  ```
  {'A': True, 'B': True, 'C': True, 'D': True, 'E': True, 'F': True, 'G': True, 'H': True, 'I': True, 'J': True, 'K': True, 'L': True, 'M': True}
  
  A -> B -> C -> H -> D -> G -> I -> J -> M -> E -> K -> F -> L
  ```

### 트리

- 그래프의 일종
- 정점(node)과 간선(branch)로 이루어짐
- 2진 트리 : 모든 노드의 차수가 2 이하인 트리
  - 전 이진 트리 : 모든 노드의 차수가 0 또는 2인 트리 
  - 포화 이진 트리 : 모든 단말 노드의 깊이가 같은 이진 트리. 
  - 완전 이진 트리 : 모든 단말 노드의 깊이의 최댓값과 최솟값의 차이가 0 또는 1인 이진 트리 

- 트리 순회 알고리즘
  - 전위 순회
  - 중위 순회
  - 후위 순회

### 이진 검색 트리

- 일자로 나열된 정렬된 데이터에서 원하는 데이터를 빠르게 찾는 방법 

- 구성
  - 일렬로 나열된 데이터들 중 가장 중앙에 위치한 하나의 데이터를 M이라고 하고, 
    M 왼쪽에 위치한 데이터들을 L, 오른쪽에 위치한 데이터를 R 이라고 가정
  - L과 R이 M을 부모로 가지는 트리를 구성
  - L과 R에 대해서도 각각 같은 방법으로 트리를 구성

- 이진 검색

  - 이분 탐색과 동일한 알고리즘

  -  이진 검색 트리의 루트 노드부터 방문하며, 다음 순서에 따라 노드를 방문

  - 과정

    - 방문한 노드가 찾는 값이라면 검색 성공

    - 방문한 노드가 단말노드이고 찾는 값이 아니라면 검색 실패

    - 방문한 노드가 단말노드가 아니고 찾는 노드가 아니면

      1. 방문한 노드의 값을 x, 찾는 값을 v라고 할 때, x < v

         -방문한 노드의 오르쪽 자식을 방문

      2. x > v

         -방문한 노드의 왼쪽 자식을 방문