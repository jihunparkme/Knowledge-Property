# Sorting Algorithm 

<br>

## Bubble Sort

- 거품정렬
- 인접한 두 개의 원소를 비교하여 자리를 교환하는 방식
  - 첫 번째 원소부터 마지막 원소까지 반복하여 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬
- 구현이 간단하지만 비효율적

- time complexity

  - Best : O(n<sup>2</sup>)
  - Average : O(n<sup>2</sup>)
  - Worst : O(n<sup>2</sup>)

  ```python
  def bubbleSort(x):
  	length = len(x)-1
  	for i in range(length):
  		for j in range(length-i):
  			if x[j] > x[j+1]:
  				x[j], x[j+1] = x[j+1], x[j]
  	return x
  
  if __name__ == "__main__":
  	arr = [7, 9, 2, 10, 3, 8, 1, 4, 5, 6]
  	rst = bubbleSort(arr)
  	print(rst)
  ```

  ```
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  ```

## Selection Sort

- 선택정렬
- 전체 원소들 중 기준 위치에 맞는 원소를 선택하여 자리를 교환하는 방식
  1. 전체 원소 중 가장 작은 원소를 찾아 선택하여 첫 번째 원소와 교환
  2. 그 다음 두 번째 작은 원소를 찾아 선택하여 두 번째 원소와 교환
  3. 이 과정을 반복

- 구현이 간단하지만 비효율적

- time complexity

  - Best : O(n<sup>2</sup>)
  - Average : O(n<sup>2</sup>)
  - Worst : O(n<sup>2</sup>)

  ```python
  def selectionSort(x):
  	length = len(x)
  	for i in range(length-1):
  		for j in range(i+1, length):
  			if x[i] > x[j]:
  				x[i], x[j] = x[j], x[i]
  	return x
  
  if __name__ == "__main__":
  	arr = [7, 9, 2, 10, 3, 8, 1, 4, 5, 6]
  	rst = selectionSort(arr)
  	print(rst)
  ```

  ```
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  ```

## Insertion Sort

- 삽입정렬

- 정렬되어 있는 부분집합에 정렬할 새로운 원소의 위치를 삽입하는 방식
  -정렬된 부분집합(S), 정렬할 부분집합(U)

  1. 정렬되지 않은 U의 원소를 하나씩 꺼내서 이미 정렬되어있는 S의 마지막 원소부터 비교하면서 위치를 찾아 삽입
  2. 삽입 정렬이 반복되며 S의 원소는 하나씩 늘고, U의 원소는 하나씩 감소
  3. U가 공집합이 되면 정렬이 완성

- 구현이 간단하지만 비효율적

  - 정렬된 데이터에 새 값을 하나 넣을 때, 빠른 효능
  - 적은 데이터에 사용하기에 괜찮은 정렬 알고리즘

- time complexity

  - Best : O(n)
  - Average : O(n<sup>2</sup>)
  - Worst : O(n<sup>2</sup>)

  ```python
  def insertSort(x):
  	for i in range(1, len(x)):
  		j = i - 1
  		key = x[i]
  		while x[j] > key and j >= 0:
  			x[j+1]  = x[j]
  			j = j - 1
  		x[j+1] = key
  	return x
  
  if __name__ == "__main__":
  	arr = [7, 9, 2, 10, 3, 8, 1, 4, 5, 6]
  	rst = insertSort(arr)
  	print(rst)
  ```

  ```
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  ```

  





## 알고리즘 설명

- <img src="..\img\sort1.png" alt="png" />

  

- [Insertion Sort]( https://www.youtube.com/watch?v=ROalU379l3U&t=111s )

  - 

- [Shell Sort]( https://www.youtube.com/watch?v=CmPA7zE8mx0 )

  - 일정한 간격으로 떨어져있는 자료들끼리 부분집합을 구성(간격별 비교)하고 각 부분집합에 있는 원소들에 대해 삽입 정렬을 수행하는 작업을 반복하는 방식
    (전체 원소에 대해서 삽입 정렬을 수행하는 것보다 부분집합으로 나누어 삽입 정렬을 하게 되면 비교적 비교 연산과 교환 연산이 감소할 수 있는 점에서 착안)
    1. 부분집합의 기준이 되는 간격을 interval에 저장
    2. 한 단계가 수행될 따마다 interval의 값을 감소시키고 쉘 정렬을 순환 호출
    3. invertal가 1이 될 때까지 반복 (interval 값은 보통 원소 개수의 1/2로 사용)

- [Quick Sort]( https://www.youtube.com/watch?v=ywWBy6J5gz8&t=153s )

  - 정렬할 전체 원소에 대해서 정렬을 수행하지 않고, 기준 값을 중심으로 왼쪽 부분 집합과 오른쪽 부분 집합으로 분할하여 정렬하는 방식
    (기준값은 pivot, 일반적으로 전체 원소 중 가운데 위치한 원소를 선택)
    1. 왼쪽 부분 집합에는 기준 값보다 작은 원소들을 이동시키고, 오른쪽 부분 집합에는 기준 값보다 큰 원소들을 이동 
    2. 분할(divid) : 정렬할 자료들을 기준 값 중심으로 2개의 부분집합으로 분할
    3. 정복(conquer) : 부분집합의 원소들 중에서 기준 값보다 작은 원소들은 왼쪽 부분집합으로, 기준 값보다 큰 원소들은 오른쪽 부분집합으로 정렬 
    4. 부분집합의 크기가 1이하로 충분히 작지 않으면 순환 호출을 이용하여 다시 분할 
  - 복잡하지만 효율적

- [Heap Sort]( https://www.youtube.com/watch?v=Xw2D9aJRBY4&t=49s )

  - 최대 힙 트리나 최소 힙 트리를 구성해 정렬하는 방법
    (내림차순 정렬 : 최대 힙, 오름차순 정렬 : 최소 힙을 구성)
    1. n개의 노드에 대한 완전 이진 트리를 구성, 이때 루트 부노드, 왼쪽 자노드, 오른쪽 자노드 순으로 구성 
    2. 최대 힙(부노드가 자노트보다 큰 트리) 구성, 아래부터 루트까지 올라오며 순차적으로 정렬
    3. m번째 정렬이 끝이 나면 가장 큰 수(루트에 위치)를 마지막 노드와 교환, 여기서 가장 큰 수는 트리에서 나옴
    4. 2, 3의 과정을 반복
  - 복잡하지만 효율적

- [Merge Sort](https://www.youtube.com/watch?v=XaqR3G_NVoo)

  -  2개 이상의 자료를 오름차순이나 내림차순으로 재 배열하는 것(여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 정렬)
  -  부분집합으로 분할(divide), 각 부분집합에 대해서 정렬 작업을 완성(conquer) 한 후, 정렬된 부분집합들을 다시 결합(combine)하는 분할 정복(divide and conquer) 기법 사용
  -  n-way 병합 : n 개의 정렬된 자료의 집합을 결합하여 하나의 집합으로 만드는 병합 방법 
     1. 분할(divide) : 입력 자료를 같은 크기의 부분집합 2개로 분할
     2. 정복(conquer) : 부분집합의 원소들을 정렬. 부분집합의 크기가 충분히 작지 않으면 순환 호출을 이용하여 다시 분할 정복 기법을 적용 
     3. 결합(combine) : 정렬된 부분집합들을 하나의 집합으로 결합 
     4. 1, 2, 3의 과정을 반복 수행하면서 정렬을 완성 
  -  복잡하지만 효율적

- Radix Sort (기수 정렬)

  - 원소의 키값을 나타내는 기수를 이용한 정렬
  - 정렬할 원소의 키값에 해당하는 버킷에 원소를 분배하였다가 버킷의 순서대로 원소는 꺼내는 방법을 반복하면서 정렬 
    1. 키값의 일의 자리에 대해서 기수 정렬을 수행
    2. 다음 단계에서는 키값의 십의 자리에 대해서 정렬을 수행
    3. 그리고 그다음 단계에서는 백의 자리에 대해서 정렬을 수행
    4. 1, 2, 3에서 진행되었던 것처럼 자릿수만큼 반복하여 정렬을 수행
  - 복잡하지만 효율적