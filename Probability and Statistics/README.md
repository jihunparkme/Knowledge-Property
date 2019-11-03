# Probability and Statistics

**확률과 통계**

<br>

## 순열과 조합

**Permutation and Combination**

- **시행**

  : 같은 조건에서 여러 번 반복할 수 있고, 그 결과가 우연에 의하여 결정되는 실험이나 관찰

- **사건**

  : 어떤 시행에서 얻어지는 결과

  어떤 시행에서 일어날 수 있는 모든 경우의 집합을 S라고 할 때, S의 부분집합

- **경우의 수**

  : 어떤 사건이 일어날 수 있는 가짓수

  - 경우의 수 합의 법칙 : 한 번의 시행에서 두 사건 A, B 가 동시에 일어나지 않고,
    사건 A, B 가 일어나는 경우의 수가 각각 m, n 이면, <u>한 번의 시행에서</u> 사건 A 또는 사건 B가 일어날 경우의 수는 **m + n**
  - 경우의 수 곱의 법칙 : 사건 A가 일어나는 경우의 수가 m이고, 그 각각에 대하여 사건 B가 일어나는 경우의 수가 n일 때, <u>두 번의 시행에서</u> 두 사건 A, B 가 연속으로 이어서 일어나는 경우의 수는 **m x n**

- **계승 or 차례곱**

  : 1 부터 n 까지의 자연수를 차례로 곱한 것을 n 의 계승 또는 차례곱이라고 부름

  n! 으로 표기하고 'n 팩토리얼' 이라고 읽음, 이 때 0! = 1 로 정의

- **순열(Permutation)**

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

-  **조합(Combination)**

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

## 확률의 뜻과 기본 성질

- **표본공간**

  : 어떤 시행에서 일어날 수 있는 모든 가능한 결과의 집합

  - 시행 : 같은 조건에서 여러 번 반복할 수 있고, 그 결과가 우연에 의하여 결정되는 실험이나 관찰

- **사건** (어떤 시행에서 얻어지는 결과)

  : 표본공간의 부분집합
  - **근원사건**

    : 표본공간의 부분집합(사건) 중에서 한 개의 원소로 이루어진 사건

  - **전사건**

    : 반드시 일어나는 사건, 즉 표본공간 자신의 집합

  - **공사건, ϕ** 

    : 절대로 일어나지 않는 사건,  

  - **합사건, A ∪ B**

    : 사건 A 또는 B 가 일어나는 사건

  - **곱사건, A ∩ B**

    : 사건 A 와 B 가 동시에 일어나는 사건

  - **배반사건**

    : 사건 A 와 B 가 동시에 일어나지 않을 때, 즉 A 와 B 가 서로소일 때 A 와 B 를 서로 배반이라고 하고, 서로 배반인 두 사건을 배반사건이라고 부름

  - **여사건, A<sup>c</sup>**

    : 사건 A 가 일어나지 않을 사건

- **확률, P(A)**

  : 어떠한 시행에서 사건 A가 일어날 가능성을 수로 나타낸 것
  - **수학적 확률** : 각 사건이 발생하는 확률이 같을 경우(e.g.주사위), <sup>K</sup>/<sub>N</sub>

    어떤 시행에서 표본공간 S가 m 개의 근원사건으로 이루어져 있고, 각 근원사건이 일어날 가능성이 모두 같은 정도로 기대될 때, 사건 A 가 r 개의 근원사건으로 이루어져 있을 경우

     <img src="..\img\picture125.png" alt="png" style="zoom:80%;" />

  - **통계적 확률** : 같은 시행을 n 번 반복하여 사건 A가 일어날 횟수를 r<sub>n</sub> 이라할 경우,

      <img src="..\img\picture124.png" alt="png" style="zoom:80%;" />
  
  - **기하적 확률** : 연속적인 변량의 크기로 갖는 표본공간 역역 S 안에서 각각의 점을 잡을 가능성이 같은 정도로 기대될 때, 영역 S 에 포함되어 있는 영역 A 에 대하여 영역 S 에서 임의로 잡은 점이 영역 A 에 속할 확률
  
       <img src="..\img\picture127.png" alt="png" style="zoom:80%;" />
  
  - 확률의 성질
  
       <img src="..\img\picture129.png" alt="png" style="zoom:70%;" />
  
     - '적어도 ~인 사건', '~ 이상인 사건', '~ 이하인 사건', '~가 아닌 사건' 을 구할 때, 여사건을 사용하면 편리

## 사건의 독립과 종속

- 조건부 확률

  : 어떠한 사건이 일어났다는 가정 하에 또다른 사건이 일어날 확률

  (확률이 0이 아닌 사건 A에 대하여, 사건 A가 일어났을 때 사건 B가 일어날 확률)

   <img src="..\img\picture130.png" alt="png" style="zoom:70%;" />

- 확률의 곱셈 정리

   <img src="..\img\picture131.png" alt="png" style="zoom:70%;" />

- 사건의 독립

  : 두 사건 A, B 에 대하여 사건 A 가 (일어나거나 일어나지 않는 것이) 사건 B 가 일어날 확률에 영향을 미치지 않을 때,  <img src="..\img\picture132.png" alt="png" style="zoom:60%;" /> 일 때, 두 사건 A 와 B 는 **서로 독립** 이라고 하고, 서로 독립인 두 사건을 **독립사건** 이라고 함

  - 독립의 조건

    P(A) > 0 , P(B) > 0 일 때, 두 사건 A, B 가 서로 독립이기 위한 필요충분조건

     <img src="..\img\picture134.png" alt="png" style="zoom:70%;" />

  - 두 사건 A, B 가 서로 독립일 때,

     <img src="..\img\picture135.png" alt="png" style="zoom:70%;" />

- 독립시행의 확률

  : 동일한 시행을 여러 번 반복할 때, 각 시행에서 일어나는 사건이 서로 독립인 경우

  1회의 시행에서 사건 A가 일어날 확률이 p일 때, n 회의 독립시행에서 사건 A 가 r 회 일어날 확률

   <img src="..\img\picture136.png" alt="png" style="zoom:70%;" />

  - e.g. 한 개의 주사위를 4번 던져서 1의 눈이 3번 나올 확률

     <img src="..\img\picture137.png" alt="png" style="zoom: 70%;" />

- 사건의 종속

  : 두 사건 A, B 가 서로 독립이 아닐 때, <img src="..\img\picture133.png" alt="png" style="zoom:60%;" /> 일 때, 두 사건 A 와 B 는 **서로 종속** 이라 하고, 서로 종속인 두 사건을 **종속사건**이라고 부름

  - 두 사건이 배반 사건 -> 사건이 동시에 일어나지 않으므로 한 사건이 일어날 때 다른 사건이 일어날 수 없음 -> 두 사건이 서로 일어날 확률에 영향을 미침 -> 종속
  - 두 사건이 독립 -> 한 사건은 다른 사건이 일어날 확률에 영향을 주지 않으모로 -> 두 사건이 동시에 일어날 수 있음 -> 배반사건이라 할 수 없음

## 이산확률변수와 확률분포

**discrete probability distribution and probability distribution** 

- 확률변수

  : 어떤 시행의 결과에 따라 표본공간의 각 원소에 하나의 실숫값을 대응시키고, 그 값에 확률이 각각 주어지는 변수. 확률변수 X가 어떤 값 x 를 취할 확률을 <img src="..\img\picture138.png" alt="png" style="zoom:60%;" /> 로 나타냄

- 확률분포

  : 확률변수 X가 취하는 값과 그 값을 취할 확률 사이의 대응 관계

- 이산확률변수

  : 확률변수 X가 취할 수 있는 값이 유한개이거나 자연수와 같이 셀 수 있을 때 

- 확률질량함수 <img src="..\img\picture139.png" alt="png" style="zoom:65%;" />

  - 이산확률 X 가 취할 수 있는 값이 <img src="..\img\picture140.png" alt="png" style="zoom:70%;" /> 일 때, X의 각 값에 X가 그 값을 취할 확률 <img src="..\img\picture141.png" alt="png" style="zoom:70%;" /> 을 대응시키는 함수

  - 이산확률변수 X의 확률질량함수가 <img src="..\img\picture139.png" alt="png" style="zoom:65%;" /> 일 때,

     <img src="..\img\picture142.png" alt="png" style="zoom:75%;" />

- 평균, 분산, 표준편차의 성질

  <img src="..\img\picture143.png" alt="png" style="zoom:80%;" /> 

- 이항분포 (binomial distribution)

  : 한 번의 시행에서 사건 A 가 일어날 확률이 p 로 일정할 때, n 번의 독립시행에서 사건 A 가 일어나는 횟수를 확률변수 X 라 하면 X 의 확률질량함수는 <img src="..\img\picture144.png" alt="png" style="zoom: 67%;" /> (단, q = 1-p)

  기호로 <img src="..\img\picture145.png" alt="png" style="zoom: 67%;" />
  - 이 때, 평균, 분산, 표준편차

     <img src="..\img\picture146.png" alt="png" style="zoom:75%;" />

- 큰 수의 법칙

  : 어떤 시행에서 사건 A가 일어날 확률이 p일 때, n번의 독립시행에서 사건 A가 일어나는 획수를 X라 하면 임의의 양수 h에 대하여

   <img src="..\img\picture147.png" alt="png" style="zoom:80%;" />

## 연속확률변수와 확률분포

 **continuous probability distribution and  probability distribution**

- **정규분포**

  : 자연 현상이나 사회 현상을 관찰하여 얻은 자료의 상대도수를, 계급의 크기를 작게하여 히스토그램으로 나타내면 자료의 개수가 커질수록 어떤 값을 중심으로 대칭적으로 분포하고, 중심에서 멀어질수록 도수가 작아지는 종 모향의 곡선에 가까워짐

   <img src="..\img\picture148.png" alt="png" style="zoom:90%;" />
  - **연속확률변수** 

    : 확률변수 X가 어떤 구간에 속하는 모든 실숫값을 취할 때, X를 연속확률변수라고 부름

  - **확률밀도함수** : 

    <img src="..\img\picture149.png" alt="png" style="zoom:80%;" /> 

     <img src="..\img\picture150.png" alt="png" style="zoom:80%;" />

  - 

