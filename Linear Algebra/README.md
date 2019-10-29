##  Table of Contents

-  [Linear algebra](#Linear-algebra)

- [벡터의 기초](#백터의-기초)

  - [벡터](#벡터(수의-순서쌍))
  
- [행렬의 기초](#행렬의-기초)

  - [행렬](#행렬(=성적표))
  - [역행렬](#역행렬)
  - [대각합](#대각합(Trace))
  - [행렬식](#행렬식(Determinant))
  - [회전변환행렬 유도](#회전변환행렬-유도)

  <br>

##  **summary** 

- [역행렬](#역행렬)
  
   <img src="..\img\Matrix6.png" alt="png" />
- [행렬식](#행렬식(Determinant))
  
  마찬가지로 <img src="..\img\vector47.png" alt="png" /> 일 때, 선택 경우는 <img src="..\img\vector48.png" alt="png" />이고 <img src="..\img\vector49.png" alt="png" />
- [고유값과 고유벡터](#고유값과-고유벡터)
  - 고유값(eigenvalue)
    
    <img src="..\img\vector74.png" alt="png"  />
  - 고유벡터(eigenvector)
    
     <img src="..\img\vector75.png" alt="png" style="zoom:90%;" />

<Br>

## Linear algebra

- 행렬(Matrix)과 벡터(Vector)

- 어떤 함수가 선형(linear)일 때, 그 함수의 성질

   <img src="..\img\DRW000081982259.gif" alt="img" style="zoom:170%;" />,   
  
  <img src="..\img\DRW00008198225d.gif" alt="img" style="zoom:170%;" />  

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

- 행렬 A, B가 정사각행렬일 때,
  <img src="..\img\Matrix7.png" alt="png" />
  - 행렬 A, B의 역행렬이 존재할 때,
    <img src="..\img\Matrix8.png" alt="png" />

###  단위행렬, 거듭제곱, 역행렬의 공통점

- 단위행렬, 거듭제곱, 역행렬의 정의
  <img src="..\img\vector35.png" alt="png" />

- 공통점
  1. 모두 **정사각 행렬**이어야 함
  2. **단위행렬과**의 곱, 거듭제곱, 역행열과의 곱은 언제나 교환법칙이 성립
     - 교환법칙이 성립하는 경우
       <img src="..\img\vector36.png" alt="png" />
     - 행렬 식에서 등장 행렬이 <img src="..\img\vector37.png" alt="png" /> 밖에 없다면 교환법칙이 무조건 성립

### 대각합(Trace)

- 정사각행렬의 주대각성분의 합으로 정의
  <img src="..\img\vector39.png" alt="png" style="zoom: 67%;" />
- 행렬 A의 대각합은 tr(A) 로 표현
  <img src="..\img\vector38.png" alt="png" />

- 대각합의 성질
  <img src="..\img\vector40.png" alt="png" />

### 행렬식(Determinant)

- 정사각형에서만 정의, 그 결과는 수

- 먼저 치환에 대한 이해가  필요
  - 치환 : 임의의 두 수의 위치는 바꾸는 연산
    <img src="..\img\vector41.png" alt="png" />
  - odd permutation
    - 홀수번의 치환만을 해야 하는 수의 배열
  - even permutation
    - 짝수번의 치환만을 해야 하는 수의 배열	
  - 네 개의 수로 만들 수 있는 수의 배열은 4! = 24가지
    - 이 가운데 12가지는 even permutation, 나머지는 odd permutation
  - 치환 시 화살표와 같은 방향의 순서를 가지면 even, 반대방향의 순서를 가지면 odd
    <img src="..\img\vector42.png" alt="png" />

- 행렬식 

  - 행렬식 표현 기호
    <img src="..\img\vector46.png" alt="png" />

  - 행렬 <img src="..\img\vector43.png" alt="png" /> 에 대하여 세 수를 선택하여 곱하기 (단, 각 행과 열에서 한 수씩 선택)

    - 세 수를 선택하는 방법은 3! = 6 가지
      <img src="..\img\vector44.png" alt="png" />

    - permutation을 이용하여 행렬식 구하기

      -배열이 odd인 경우 세 수의 곱 결과에 -1을 곱하고, even인 경우 세 수의 곱 결과에 +1을 곱함

      -그 다음 여섯개의 수를 모두 합한 결과가 행렬 A의 행렬식
      <img src="..\img\vector45.png" alt="png" />

  - 마찬가지로 <img src="..\img\vector47.png" alt="png" /> 일 때, 선택 경우는 <img src="..\img\vector48.png" alt="png" />이고 <img src="..\img\vector49.png" alt="png" />
### 회전변환행렬 유도
- 기저 벡터인 (1,0)과 (0,1)를 θ만큼 회전
  <img src="..\img\vector50.png" alt="png" />
  -   (1,0)을 θ만큼 회전하면 (cosθ,sinθ), (0,1)을 θ만큼 회전하면 (−sin⁡θ,cos⁡θ)
  - 회전 행렬 R은 선형 변환이므로 다음이 성립
    <img src="..\img\vector51.png" alt="png" />
  -  R(1,0)과 R(0,1)이 (cos⁡θ,sin⁡θ), (−sinθ,cosθ)이므로, 대입하면 유도 
    <img src="..\img\vector52.png" alt="png" />
  - 3차원의 경우 회전축에 대해  <img src="..\img\vector53.png" alt="png" />
    <img src="..\img\vector54.png" alt="png" />

### 행렬식의 성질

- A, B가 같은 꼴의 정사각행렬일 때,

  1. <img src="..\img\vector55.png" alt="png" />
     <img src="..\img\vector56.png" alt="png" />

  2.  <img src="..\img\vector57.png" alt="png" />

  3.  <img src="..\img\vector58.png" alt="png" />
     행렬 A의 역행렬 A<sup>-1</sup>가 존재(Exist)하기 위한 필요충분조건
     <img src="..\img\vector59.png" alt="png" />

  4. A, B의 역행렬은 존재하고, P, Q의 역행렬은 존재하지 않을 때,
     <img src="..\img\vector60.png" alt="png" /> 일 때,
     <img src="..\img\vector61.png" alt="png" />

     -역행렬이 존재하는 행렬끼리의 곱한 행렬은 역행렬이 존재
     -역행렬이 존재하지 않는 행렬과 다른 행렬을 곱한 행렬은 역행렬이 존재하지 않는다

     - <img src="..\img\vector62.png" alt="png" />

### 행렬식의 기하학적 의미

- 2차 정사각행렬의 행렬식의 절대값 = 두 벡터로 이루어진 평행사변형의 넓이

  - <img src="..\img\vector64.png" alt="png" />

    <img src="..\img\vector63.png" alt="png" />

  - <img src="..\img\vector65.png" alt="png" />

- 3차 정사각행렬의 행렬식의 절대값 = 세 벡터로 이루어진 평행육면체의 부피

## 행렬의 응용

### 행렬과 연립일차방정식

- 연립일차방정식을 행렬로 취급할 수 있음
  -  <img src="..\img\vector66.png" alt="png" />
  -  <img src="..\img\vector67.png" alt="png" style="zoom:80%;" />
  - <img src="..\img\vector68.png" alt="png"  />

- 역행렬이 존재하지 않는 연립일차방정식
  - 역행렬이 존재하지 않다는 것은 해가 없거나, 해가 무수히 많거나 둘 중 하나
    - 두 식이 같으면, 해가 무수히 많음
      <img src="..\img\vector69.png" alt="png"  />
    - 두 식이 다르면, 해가 없음
      <img src="..\img\vector70.png" alt="png"  />
- 정리
  - <img src="..\img\vector71.png" alt="png"  />
  - 연립방정식의 해가 존재할 때,
    <img src="..\img\vector72.png" alt="png"  />
  - 연립방적식의 해가 존재하지 않을 때, 혹은 ~~이외의 해가 존재할 때,
    <img src="..\img\vector73.png" alt="png"  />

### 고유값과 고유벡터

- 고유값(eigenvalue)
  - <img src="..\img\vector74.png" alt="png"  />

- 고유벡터(eigenvector)
  -  <img src="..\img\vector75.png" alt="png" style="zoom:85%;" />

- 위 식에서 고유값은 3, 고유벡터는 <img src="..\img\vector76.png" alt="png"  />

### 닮음변환(=유사변환)

- similar transformation
- 행렬 A를 역행렬이 존재하는 행렬 P와 다음과 같이 곱하여 새로운 행렬 B를 만드는 과정
  - 이때, A와 B는 similar 하다고 함
    <img src="..\img\vector77.png" alt="png"  />
  - <img src="..\img\vector78.png" alt="png"  /> 일 경우, <img src="..\img\vector79.png" alt="png"  />
- 닮음변환의 성질
  <img src="..\img\vector80.png" alt="png"  />
- 대각행렬(diagonal matrix)
  <img src="..\img\vector81.png" alt="png"  /> 처럼 주대각성분 이외의 모든 성분이 0일 정사각행렬
  - 단위행렬이 대표적인 대각행렬
- 대각화(diagonalization)
  - 정사각행렬 A에 적당한 정사각행렬 P를 이용하여 닮음변환을 시켜 대각행렬을 만드는 과정을 대각화
- n차 정사각행렬의 행렬식은 고유값들의 곱과 같고, 대각합은 고유값들의 합과 같음
  <img src="..\img\vector82.png" alt="png"  />
  <img src="..\img\vector83.png" alt="png"  />

### 케일리-해밀턴 정리

- Cayley-Hamilton's Theorem

- 공식
  <img src="..\img\vector84.png" alt="png"  />

- 정체
  <img src="..\img\vector85.png" alt="png"  />
- 케일리-해밀턴 정리는 보통 높은 차수의 행렬에 관한 식을 낮은 차수로 변형시킬 때 사용
  - 복잡한 행렬의 곱(거듭제곱)에서 유용하게 사용

### 행렬과 함수

- 함수(function)

  <img src="..\img\vector86.png" alt="png"  />

  - 넓은 의미에서 함수는 **사상(mapping)**과 같은 뜻으로 사용

    좁은 의미에서는 X, Y가 수의 집합일 경우, 특히 X가 자연수의 집합일 경우에는 **수열(sequerence)** 

  - **변환(transformation)**

    - 사상 가운데 공간(space)에서 같은 공간을 대응하는 사상
    - 변환의 예로는 좌표평면에서 평행이동, 대칭이동, 회전변환, 확대･축소변환 등

  -  **연산자(operator)**

    - 사상 가운데 X, Y가 함수의 집합일 때
    - 연산자란 <img src="..\img\vector87.png" alt="png"  /> , 미분, 적분이 포함

  - 함수의 사용
     <img src="..\img\vector88.png" alt="png" style="zoom:90%;" />

  - 함수(변환)을 행렬로 표현할 수 있음

  - 함수의 합성과 행렬의 곱의 비교
    <img src="..\img\vector89.png" alt="png"  />

### 행렬과 일차변환

- linear transformation



<br>

<br>

>Reference
>
>밝히리
>
>http://blog.daum.net/eigenvalue/10856412 
>
>
>
>- 회전변환행렬 유도 : https://o-tantk.github.io/posts/derive-rotation-matrix/ 

