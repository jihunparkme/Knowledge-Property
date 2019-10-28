## Table of Contents

-  [Linear algebra](#Linear-algebra)

- [벡터의 기초](#백터의-기초)

  - [벡터](#벡터(수의-순서쌍))
  - [벡터의 상등](#벡터의-상등)
  - [벡터의 덧셈 뺄셈](#벡터의-덧셈,-뺄셈)
  - [벡터의 실수배](#벡터의-실수배)
  - [벡터의 내적](#벡터의-내적)

  <br>

## Linear algebra

- 행렬(Matrix)과 벡터(Vector)
- 어떤 함수가 선형(linear)일 때, 그 함수의 성질
<img src="..\img\DRW000081982259.gif" alt="img" style="zoom:150%;" />
  <img src="..\img\DRW00008198225d.gif" alt="img" style="zoom:150%;" />  

<br>

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

- 벡터의 표현법(3, 4) 과 좌표의 표현법 A(3, 4)
  <img src="..\img\vector11.png" alt="png" />

  <img src="..\img\vector13.png" alt="png" />

- 복소평면에서는 복소수를 좌표평면위에 나타내기 위해 x축을 실수축, y축을 허수축으로 잡음

  - (-3, 5) 는 복소수 z = -3 + 5i 

### 벡터와 복소수

- 벡터와 복소수의 관계
  <img src="..\img\vector14.png" alt="png" />

  <br>
  <img src="..\img\vector15.png" alt="png" />

- 2차원 벡터는 좌표평면 위의 한 점으로 생각할 수 있고, 복소평면위의 한 복소수로 생각할 수 있음

### 벡터와 함수

- 동형(isomorphic)
  - 이차함수의 실수배와 벡터의 실수배는 똑같은 연산이라는 표현
  - 이차함수의 연산
    <img src="..\img\vector17.png" alt="png" />
  - 벡터의 연산
    <img src="..\img\vector18.png" alt="png" />
  - 이와 같은 대응 관계를 동형사상(isomorphism)
- 함수의 연산과 벡터의 연산
  <img src="..\img\vector16.png" alt="png" />
  - 이차함수를 벡터로도 표현 가능

<br>

## 행렬의 기초

### 행렬(=성적표)

- 수를 직사각형 모양으로 배열한 것
- 각각의 수를 그 행렬의 성분으라고 부름
  - two by three matrix
    <img src="..\img\vector19.png" alt="png" />

- 행렬의 가로줄은 행(row), 세로줄은 열(column)
- 두 개의 행벡터를 세로로 쌓은 모양, 혹은 세 개의 열벡터를 옆으로 붙인 모양이라고 생각 가능

### 행렬의 상등

- 두 행렬이 같다 = 두 벡터가 같다
  - 행렬의 형태와 각각의 성분이 모두 같아야 함

### 행렬의 덧셈

- 형태가 같은 행렬끼리 연산 가능
  <img src="..\img\vector20.png" alt="png" />

- 덧셈이 가능한 행렬에 적용되는 성질
  <img src="..\img\vector21.png" alt="png" />

### 행렬의 실수배

- 벡터의 실수배와 유사
  <img src="..\img\vector22.png" alt="png" />

- 덧셈이 가능한 행렬에 적용되는 실수배 성질
  <img src="..\img\vector23.png" alt="png" />

### 행렬의 곱

- 벡터의 내적과 관련
- 일반적으로 행렬의 곱은 **교환법칙이 성립하지 않음**(곱하는 순서를 함부로 바꾸면 안됨)
- 앞 행렬의 열의 수와, 뒤 행렬의 행의 수가 같아야 연산 가능
  <img src="..\img\vector24.png" alt="png" />

- 행렬의 곱
  <img src="..\img\vector25.png" alt="png" />
  <img src="..\img\vector26.png" alt="png" />
  <img src="..\img\vector27.png" alt="png" />

- AB = C 일 때, C 의 성분 i, j 는
  <img src="..\img\vector28.png" alt="png" />

- 덧셈, 곱셈이 가능한 행렬에 적용되는 곱셈 성질
  <img src="..\img\vector29.png" alt="png" />

### 단위행렬

-  실수 1은 곱셈에 대한 항등원
  <img src="..\img\vector32.png" alt="png" />
- 마찬가지로 정사각행렬의 곱셈에 대한 항등원을 단위행렬이라고 불림
  - 기호
    <img src="..\img\Matrix2.png" alt="png" />
- 정사각행렬 A의 AE = EA = A 를 만족하는 단위행렬이 존재 
  - 단위행렬과의 곱은 예외로 언제나 교환법칙이 성립
  - 이차 단위행렬
    <img src="..\img\vector30.png" alt="png" />
  - 삼차 단위행렬
    <img src="..\img\vector31.png" alt="png" />

### 행렬의 거듭제곱

- 정사각행렬은 자기 자신끼리 곱셈이 가능

  <img src="..\img\vector33.png" alt="png" />

- 행렬의 거듭제곱은 교환법칙이 성립
  <img src="..\img\vector34.png" alt="png" />

- 지수법칙
  <img src="..\img\Matrix1.png" alt="png" />

- 행렬의 곱셉의 교환법칙
  - 교환법칙 성립 X
    <img src="..\img\Matrix3.png" alt="png" />
  - 정사각행렬의 거듭제곱과 단위행렬에 대해서는 교환법칙이 성립
    <img src="..\img\Matrix4.png" alt="png" />
  - 곱셈공식과 매우 유사
    <img src="..\img\Matrix5.png" alt="png" />

### 역행렬

- 서로 곱해서 단위행렬이 될 때, 한 행렬을 다른 행렬의 역행렬이라고 함
  = 행렬의 곱셈에 대한 역원

- 실수의 역수와 같은 의미
  - a는 실수,  ax=xa=1 을 만족하는 실수 x를 a의 역수라고 칭함
  - a!=0 일 경우, a의 역수 a<sup>-1</sup>가 존재, a<sup>-1</sup>=1/a

- 정사각행렬 A에 대하여 AX = XA = E를 만족하는 행렬 X가 존재할 때,
  - 행렬 X는 A의 역행렬 (=A inverse)
  - X = A<sup>-1</sup>
  - 반대로 A는 X의 역행렬이라고도 할 수 있음
- 공식
  <img src="..\img\Matrix6.png" alt="png" />

### 역행렬의 성질









<br>

<br>

>reference
>
>밝히리
>
> http://blog.daum.net/eigenvalue/10856412 

