# Probability and Statistics

**확률과 통계**

<br>

## 순열과 조합

**Permutation and Combination**

- 시행

  : 같은 조건에서 여러 번 반복할 수 있고, 그 결과가 우연에 의하여 결정되는 실험이나 관찰

- 사건

  : 어떤 시행에서 얻어지는 결과

  어떤 시행에서 일어날 수 있는 모든 경우의 집합을 S라고 할 때, S의 부분집합

- 경우의 수

  : 어떤 사건이 일어날 수 있는 가짓수

  - 경우의 수 합의 법칙 : 한 번의 시행에서 두 사건 A, B 가 동시에 일어나지 않고,
    사건 A, B 가 일어나는 경우의 수가 각각 m, n 이면, <u>한 번의 시행에서</u> 사건 A 또는 사건 B가 일어날 경우의 수는 **m + n**
  - 경우의 수 곱의 법칙 : 사건 A가 일어나는 경우의 수가 m이고, 그 각각에 대하여 사건 B가 일어나는 경우의 수가 n일 때, <u>두 번의 시행에서</u> 두 사건 A, B 가 연속으로 이어서 일어나는 경우의 수는 **m x n**

- 계승 or 차례곱

  : 1 부터 n 까지의 자연수를 차례로 곱한 것을 n 의 계승 또는 차례곱이라고 부름

  n! 으로 표기하고 'n 팩토리얼' 이라고 읽음, 이 때 0! = 1 로 정의

- **순열**(Permutation)

  : 서로 다른 n 개의 물건 중 r 개를 택하여 <u>일렬로 나열(순서를 생각)</u>하는 경우 <sub>n</sub>P<sub>r</sub>

   <img src="..\img\picture113.png" alt="png" style="zoom:80%;" />

  순열의 정의에 의해 <sub>n</sub>P<sub>n</sub> = n! ,  <sub>n</sub>P<sub>0</sub> = 1 이 성립

  - **원순열, (n-1)!**

    : 서로 다른 n 개를 원형으로 배열

  - **중복순열, <sub>n</sub>II<sub>r</sub> = n<sup>r</sup>**

    : 서로 다른 n 개에서 r 개를 택 

  - ?? 순열

    : n 개에서 서로 같은 것이 각각 p<sub>1</sub>, p<sub>2</sub>,  p<sub>3</sub>, ...  p<sub>k</sub>  개씩 있을 때, 이들을 모두 택하여 일렬로 나열

     <img src="..\img\picture116.png" alt="png" style="zoom:90%;" />

-  **조합**(Combination)

  : 서로 다른 n 개의 물건 중 <u>순서를 생각하지 않고</u> r 개를 택하는 경우

   <img src="..\img\picture114.png" alt="png" style="zoom:80%;" />

  - 조합의 도형 응용
    - 일직선 위에 있지 않은 서로 다른 n 개의 점에서 두 점을 이어 만든 직선의 개수 : <sub>n</sub>C<sub>2</sub> 
    - 일직선 위에 있지 않은 서로 다른 n 개의 점에서 세 점을 이어 만든 삼각형의 개수 : <sub>n</sub>C<sub>3</sub> 
    - m 개의 평행선과 n 개의 평행선이 만날 때 생기는 평행사변형의 개수 : <sub>m</sub>C<sub>2</sub> X <sub>n</sub>C<sub>2</sub> 
    
  - 조합의 성질
  
    - r 와 n 이 0 이상인 정수일 때 다음이 성립
  
       <img src="..\img\picture117.png" alt="png" style="zoom:90%;" />
  
  - **중복 조합, <sub>n</sub>H<sub>r</sub> = <sub>n+r-1</sub>C<sub>r</sub>**
  
    : 서로 다른 n 개에서 중복을 허락하여 r 개를 택하는 조합

- **집합의 분할,  S(n, k) = S(n-1, k-1) + k X S(n-1, k)**

  : 주어진 집합을 공집합이 아닌 몇 개의 서로소인 부분집합으로 나누는 것

    또한, 원소의 개수가 n인 집합을 k 개의 집합으로 분할하는 방법의 수

- 자연수의 분할

  : 자연수 n 을 <img src="..\img\picture118.png" alt="png" style="zoom:80%;" /> 로 나타내는 것

  -  자연수 n 을 k 개의 자연수의 합으로 나타내는 방법의 수 **P(n, k)**

- 이항정리

   <img src="..\img\picture119.png" alt="png" style="zoom:90%;" />

- 이항계수의 성질

   <img src="..\img\picture120.png" alt="png" style="zoom:90%;" />

## 대푯값과 산포도

 **representative value and degree of scattering**

- **대푯값**

  : 자료 전체의 중심적인 경향이나 특성을 하나의 수로 나타내어 자료 전체를 대표하는 값
  - 평균 :  어떤 값들의 집합의 적절한 특징을 나타내거나 요약하는 것

  - 중앙값 : 변량을 작은 것부터 큰 것 순으로 나열했을 때, 중앙에 위치하는 값

    단, 변량의 개수가 짝수인 경우 중앙에 있는 두 값의 중간값을 구함

  - 최빈값: 변량 중에서 가장 많이 등장하는 값

- **산포도**

  : 자료 전체가 대표값을 중심으로 흩어져 있는 정도

  - 평균편차, 표준편차 등

   <img src="..\img\picture121.png" alt="png" style="zoom:90%;" />
  분산의 또 다른 공식 <img src="..\img\picture122.png" alt="png" style="zoom:80%;" />

- 도수분포표에서의 평균과 분산

   <img src="..\img\picture123.png" alt="png" style="zoom:80%;" />