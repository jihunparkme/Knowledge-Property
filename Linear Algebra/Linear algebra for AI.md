#  Elements in linear algebra

## Scalar, Vector, Matrix

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

# Linear system

## Linear Equation

- 선형방정식

   <img src="..\img\picture52.png" alt="png"  />

  - b은 상수,  a<sub>n</sub>은 계수,  x<sub>n</sub>은 풀어야할 변수

  - 위 방적식은 내적을 통해 <img src="..\img\picture53.png" alt="png" style="zoom: 80%;" /> 로 쓸 수 있음

     <img src="..\img\picture54.png" alt="png" style="zoom:80%;" />

    - 참고: x(scaler) **x**(vector), X(matrix)