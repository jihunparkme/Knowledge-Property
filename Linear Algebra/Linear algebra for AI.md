#  before going in 

##  Elements in linear algebra

### Scalalr

- 하나의 숫자 

- 4.3

### Vector

- 순서가 정해진 list

  <img src="..\img\picture34.png" alt="png" style="zoom:80%;" /> 

- 순서가 정해지지 않은 list 는 set

### Matrix

- 행렬(2차원 배열)

  <img src="..\img\picture35.png" alt="png" style="zoom:80%;" /> 

- Column vector : 선형대수에서 기본적으로 쓰이는 벡터(열벡터)

  <img src="..\img\picture36.png" alt="png" style="zoom:80%;" /> 

- Row vector : 행벡터

   <img src="..\img\picture37.png" alt="png" style="zoom:80%;" />

- Matrix Notation (표기법)

  - Square matrix (rows = column) (정사각 행렬)

     <img src="..\img\picture41.png" alt="png"  />

  - Rectangular matrix (rows != columns) (직사각 행렬)

     <img src="..\img\picture40.png" alt="png"  />

  - Transpose of matrix (mirroring across the main diagonal)

    - main matrix에서 대각선을 기준으로 180 transpose 시킨 모양

     <img src="..\img\picture42.png" alt="png"  />

## Vector/Matrix Additions and Multiplications

### Element-wise addition

- C = A + B

   <img src="..\img\picture44.png" alt="png" style="zoom:80%;" />

  - 행렬 A, B, C 의 사이즈는 같아야 함

     <img src="..\img\picture43.png" alt="png"  />

### Scalar multiple of vector/matrix

- ca, cA

   <img src="..\img\picture45.png" alt="png"  />

### Matrix-matrix multiplicaton

- C = AB

   <img src="..\img\picture46.png" alt="png"  />

  - ex)

    <img src="..\img\picture47.png" alt="png"  />

   <img src="..\img\picture48.png" alt="png"  />

- Inner Product (내적)

  - 두 벡터를 곱하여 output으로 scalar를 만들어냄

   <img src="..\img\picture49.png" alt="png"  />

- Outer Product (외적)

  - 얇은 벡터들을 큰 형태의 숫자집합 형태로 만들어냄

     <img src="..\img\picture51.png" alt="png"  />

- Matrix multiplication의 properties

  - AB != BA : not commutative  (교환법칙 불가)
  - A(B+C) = AB+AC : Distributive (분배법칙)
  - A(BC) = (AB)C : Associative (결합법칙)
  - (AB)<sup>T</sup> = B<sup>T</sup>A<sup>T</sup> : property of transpose (전치)

<br>

# Linear System and Linear Transformation

## Linear Equation and Linear System

### Linear Equation

- 선형방정식

   <img src="..\img\picture52.png" alt="png"  />

  - b은 상수,  a<sub>n</sub>은 계수,  x<sub>n</sub>은 풀어야할 변수

  - 위 방적식은 내적을 통해 <img src="..\img\picture53.png" alt="png" style="zoom: 80%;" /> 로 쓸 수 있음

     <img src="..\img\picture54.png" alt="png" style="zoom:80%;" />

    - 참고: x(scaler) **x**(vector), X(matrix)

### Linear System : Set of Equation 

- 연립방정식

  = a system of linear equations = a linear system

   <img src="..\img\picture55.png" alt="png" style="zoom:80%;" />
  - Example

    <img src="..\img\picture56.png" alt="png" style="zoom:80%;" />

     <img src="..\img\picture57.png" alt="png" style="zoom:80%;" />

     <img src="..\img\picture58.png" alt="png" style="zoom:80%;" />

    - 내적을 통한 방적식

       <img src="..\img\picture59.png" alt="png" style="zoom:80%;" />

### Identity Matrix

- 항등 행렬

  - 정사각행렬에서의 대각요소는 1이고 나머지는 0으로 이루어진 행렬

  - 어떤 벡터와 곱해도 자기 자신이 결과

     <img src="..\img\picture61.png" alt="png" style="zoom:80%;" />

     <img src="..\img\picture60.png" alt="png" style="zoom:80%;" />

### Inverse Matrix

- 역행렬

  - 오직 정사각행렬에서만 존재

  - det A = 0 으로, 역행렬이 존재할 때, 근은 무조건 한 개 존재

     <img src="..\img\picture62.png" alt="png" style="zoom:80%;" />

     <img src="..\img\picture63.png" alt="png" style="zoom:80%;" />

  - 2 x 2 matrix 에서의 역행렬 공식

      <img src="..\img\picture66.png" alt="png" style="zoom:80%;" />

     <img src="..\img\picture64.png" alt="png" style="zoom:80%;" />

    - 역행렬을 활용하여 Ax = b 방정식을 푸는 과정

       <img src="..\img\picture67.png" alt="png" style="zoom:80%;" />

  - 2 x 2 이상의 matrix는 Gaussian Elimination 을 공부할 필요가 있음

### Non-Invertible Matrix

- 역행렬이 존재하지 않을 경우

   <img src="..\img\picture68.png" alt="png" style="zoom:80%;" />

  - **det A** (determinant, 판별식)이 0 인 경우,

    **ad - bc = 0**

    ad = bc

    a : b = c : d

  - 역행렬이 존재하지 않는다면,

    - 해가 무수히 많거나
    - 해가 하나도 없거나

- 참고. 3 x 3 matrix 에서의 역행렬 공식

  -  3차 정사각행렬<img src="..\img\picture69.png" alt="png" style="zoom:80%;" /> 의 판별식은

     <img src="..\img\picture71.png" alt="png"  /> -<img src="..\img\picture72.png" alt="png"  />

     <img src="..\img\picture70.png" alt="png" style="zoom:80%;" />

- Rectangular Matrix 에서의 해
  - m = 방정식, n = 변수 라고 가정했을 때,
    - m < n (,데이터 개수 < 변수) 경우 under-determined system : 해가 무수히 많아짐
    - m > n (,데이터 개수 > 변수) 경우  over-determined system : 해가 하나도 없음 

## Linear Combinations

### Linear Combinations

- 선형 결합

  - 벡터와 스칼라의 결합

    c<sub>1</sub>v<sub>1</sub> + c<sub>2</sub>v<sub>2</sub> + ... + c<sub>p</sub>v<sub>p</sub> 

  - 행렬 방정식으로 쓰였던 <img src="..\img\picture58.png" alt="png" style="zoom:80%;" /> 이 식이

    벡터 방정식 <img src="..\img\picture73.png" alt="png" style="zoom:80%;" /> 으로 쓰일 수 있음

- Span

  - 유한한 개수의 벡터들로 만들 수 있는 가능한 모든 선형 결합을 모아 놓은 벡터들의 집합

     <img src="..\img\picture74.png" alt="png"  />

  - 벡터가 한 개라고 했을 때, 벡터들의 집합은 선(line)이 될 수 있음
  - 벡터 방정식 <img src="..\img\picture73.png" alt="png" style="zoom:80%;" /> 을 다시 생각해보면, 
    결과 b는 위의 3개의 벡터로 만들 수 있는 벡터들의 집합 안에 포함되어 있다고 말할 수 있음
    
    - 여기서, 방정식의 개수가 벡터들의 original 차원을 의미하고, 주어진 벡터(재료 벡터)는 운용할 수 있는 미지수의 개수를 의미
    - 또한, 해를 구하기 위해서는 <img src="..\img\picture75.png" alt="png" style="zoom: 67%;" /> 가 만족해야 함
  - 차원 문제를 방정식으로 해결하면 굉장히 편하게 해를 찾을 수 있음

- 선형 결합의 시각으로 Matrix Multiplications 를 보기

  1. A**x** 를 선형 결합으로 보기

     <img src="..\img\picture82.png" alt="png" style="zoom:80%;" />

  2. 선형 결합과 span 개념을 가지고 다시 Multiplications as Column combinations 을 시도

     - One column on the right

        <img src="..\img\picture78.png" alt="png" style="zoom:80%;" />

     - Multi-columns on the right

        <img src="..\img\picture79.png" alt="png" style="zoom:80%;" />

       - 여기서도 **x** 는 3 개의 벡터로 만들 수 있는 벡터들의 집합 안에 포함되어 있음 

  3. 마찬가지로 Multiplications as Row combinations 을 시도

     - One row on the left

        <img src="..\img\picture80.png" alt="png" style="zoom:80%;" />

     - Multiple rows on the left

       <img src="..\img\picture81.png" alt="png" style="zoom:80%;" />

  4.  Matrix Multiplications as Sum of (Rank-1) Outer Products 

     -  (Rank-1) outer product 

        <img src="..\img\picture84.png" alt="png" style="zoom:80%;" />

     -  Sum of (Rank-1) outer products 

        <img src="..\img\picture85.png" alt="png" style="zoom:80%;" />

## Linear Independence and Linear Dependence

### Linear Independence

- b 가 Span{a<sub>1</sub>,a<sub>2</sub>,a<sub>3</sub>) 에 속할 때 해가 존재

  <img src="..\img\picture73.png" alt="png" style="zoom:80%;" /> 

  - a<sub>1</sub>,a<sub>2</sub>,a<sub>3</sub> 의 해가 unique 할 때, linear independence (선형 독립)
  - a<sub>1</sub>,a<sub>2</sub>,a<sub>3</sub>  의 해가 무수히 많을 때, linear dependence (선형 의존)
    - 세 벡터가 한 평면에 존재

- Practical Definition

  - 벡터들을 하나씩 순차적으로 추가해가면서 Span을 생각해 보았을 때

    - 추가된 벡터가 이전 Span에 포함되어있지 않는 경우(Span이 점차적으로 계속 늘어나는 경우)

      => 선형 독립 (해가 unique)

    - 혹은, 벡터가 추가되기 전 Span에 포함되어 Span을 추가하지 않아도 되는 경우

      => 선형 의존 (해가 무수히 많음)

- Formal Definition

  - 상수 b를 **O**(영벡터)라고 생각할 때,

     <img src="..\img\picture86.png" alt="png" style="zoom:80%;" />

    - 무조건 최소 하나의 solution을 찾을 수 있음 (Because 영벡터는 모든 재료 벡터의 Span 안에 포함)
    - 이 solution은 너무 쉽고 사소한? 이유로 trivial solution 이라고 불리움

  - 이 solution이 유일한 해결책일 경우, linear independence (선형 독립)

  - 이 솔루션 외에 다른 nontrivaial solution이 존재할 경우(e.g. 영벡터에서 적어도 하나의 element가 0이 아닐 때), linear dependence (선형 의존) 

- [Linear Combinations 의 Span 부분 참고](#Linear-Combinations)

## Basis and Dimension

### Span and Subspace

- Subspace는 Span 과 유사한 개념

  - Span에 포함된 두 벡터에 어떠한 가중치를 곱하여 선형 결합으로 만든 결과 벡터는 해당 Span 안에 포함되어 있음

- 선형 결합에 닫혀있는 Subset(부분집합)을 Subspace 라고 칭함 

  - Subset(부분집합)에서, 두 벡터를 뽑은 후 적당한 선형 결합으로 만든 결과 벡터가,

    해당 부분 집합에 포함되어 있을 때, 이 부분 집합이 ''선형 결합에 닫혀있다' 라고 말할 수 있음 

    단, 어떠한 가중치를 사용하더라도 다 해당 부분 집합 안에 포함이 되어 있어야 함 

- 닫혀있다 라는 의미,

  - 부분 집합 S = { 1, 2, 4...} 에서 임의의 두 수를 뽑아(중복 가능) 곱한 결과가 S에 포함되어 있을 경우,

    이 부분 집합은 곱셈에 닫혀있는 부분 집합이라고 말할 수 있음

- 결국, Subspace는 항상 Span으로 표현될 수 있음

- column space
  -  column 벡터들로 이루어진 span

### Basis of a Subspace

- A Basis (기저 벡터) of a Subspace 를 만족하려면
  - Subspace의 벡터들이 Fully spans 해야 함

  - 중복되는 span을 허용하지 않는 Linearly independenct (선형 독립) 해야 함

    e.g. 3개의 벡터가 한 평면에 모두 있는 경우, span이 중복될 수 있음

- 기저 벡터는 unique 하지 않음
  - 서로 다른 기저 벡터를 사용했을 때, 특정 점을 표현할 수 있는 다른 solution이 존재

### Dimension of Subspace

- Dimension (차원)
  - 어떤 Subspace가 주어져 있을 때, 그 Subspace의 기저 벡터 개수

### Rank of Matrix

- column space의 dimension

   <img src="..\img\picture87.png" alt="png" style="zoom:80%;" />

  - column들이 span하는 subspace의 기저 벡터 개수

- matrix에서 rank가 작다고 하는 것은 feature들 간의 중복이 많은 경우를 의미할 수 있음
  - feature 개수가 많더라도 v<sub>1</sub>을 통해 v<sub>2</sub>, v<sub>3</sub> ... 의 값을 알 수 있다면, feature의 개수에 반해 많은 정보를 가지고 있지 않음
  - 즉, feature는 100개 있지만 쓸모있는 핵심 feature은 5개? 밖에 없을 경우 rank가 작다 라고 할 수 있음









#  **Least Square**

# eigenvalue decomposition

- 고유값 분해

# specific value decomposition

- 특이값 분해







> Reference
>
> <br>
>
> Numpy tutorial :  [Python Numpy Tutorial](http://cs231n.github.io/python-numpy-tutorial/)
>
> Linear algebra :  [Linear algebra cheat sheet for deep learning](https://towardsdatascience.com/linear-algebra-cheat-sheet-for-deep-learning-cd67aba4526c)