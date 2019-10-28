# Linear algebra

## Table of Contents

-  [Linear algebra](#Linear-algebra)
- [벡터의 기초](#백터의-기초)
  - [벡터](#벡터(수의-순서쌍))
  - [벡터의 상등](#벡터의-상등)
  - [벡터의 덧셈 뺄셈](#벡터의-덧셈,-뺄셈)
  - [벡터의 실수배](#벡터의-실수배)
  - [벡터의 내적](#벡터의-내적)

## Linear algebra

- 행렬(Matrix)과 벡터(Vector)

- 어떤 함수가 선형(linear)일 때, 그 함수의 성질

  -   <img src="..\img\DRW000081982259.gif" alt="img" style="zoom:150%;" />
  -   <img src="..\img\DRW00008198225d.gif" alt="img" style="zoom:150%;" />  

## 벡터의 기초

### 벡터(수의 순서쌍)

- 순서를 정해서 수를 나열한 순서쌍
  - ex) 국영수 성적, Aaron = (90, 95, 90)
- 각각의 수를 벡터의 성분이라고 부름
- 벡터를 문자로 표현할 때는 a, b 문자 위에 화살표를 그려서 표기
- A={1, b, 5} 와 B={5, 1, b} 는 같은 집합이지만 벡터는 순서쌍이므로 순서가 매우 중요 --> a=(1, b, 5) 와 b=(5, 1, b) 는 다른 벡터
- 명칭
  - (2) : 스칼라(실수)
  - (1, a) : 2차원 벡터
  - (1, a, 4) : 3차원 벡터

### 벡터의 상등

- 두 벡터가 서로 같다는 것은 각각의 성분이 같다는 것을 의미, 순서, 차원 모두 같아야 함
  <img src="..\img\vector1.png" alt="png" />

### 벡터의 덧셈, 뺄셈

- 차원이 같은 벡터끼리만 연산이 가능
- (1, 2, 3) + (4, 5, 6) = (5, 7, 9)

<img src="..\img\vector2.png" alt="png" />

- 영벡터(0, 0, 0)는 벡터의 덧셈에 대한 항등원

- 덧셈이 가능한 벡터들에 적용되는 성질들

  <img src="..\img\vector3.png" alt="png" />

### 벡터의 실수배

- 정의
  <img src="..\img\vector4.png" alt="png" />

- 2 X (1, 2, 3) = (2, 4, 6)

- 덧셈이 가능한 벡터들에 적용되는 실수배 성질들

  <img src="..\img\vector5.png" alt="png" />

### 벡터의 내적

- 정의

  <img src="..\img\vector6.png" alt="png" />
  <img src="..\img\vector10.png" alt="png" />

- (1, 2, 3) . (10, 20, 30) = (10, 40, 90) = 10 + 40 + 90 = 140

- 벡터 내적의 결과는 벡터가 아닌 스칼라(=스칼라  곱(scalar product)) (=dot product)

- 벡터의 크기

  <img src="..\img\vector7.png" alt="png" />

- 직교(orthogonal)
  - 영벡터가 아닌 두 벡터의 내적이 0인 경우
    <img src="..\img\vector8.png" alt="png" />

- 내적의 성질
  <img src="..\img\vector9.png" alt="png" />

### 벡터와 좌표









<br>

<br>

>reference
>
>밝히리
>
> http://blog.daum.net/eigenvalue/10856412 

