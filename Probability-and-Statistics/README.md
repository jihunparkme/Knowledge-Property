#  Probability and Statistics

**확률과 통계**

<br>

## 공식 정리

#### **순열(Permutation)**

서로 다른 n 개의 물건 중 r 개를 택하여 <u>일렬로 나열(순서를 생각)</u>하는 경

 <img src="..\img\picture113.png" alt="png" style="zoom:60%;" />

- **원순열** (서로 다른 것을 원형으로 배열하는 순열)

   <img src="..\img\picture203.png" alt="png" style="zoom:90%;" />

- **중복순열** (서로 다른 n개에서 중복을 허락하여 r개를 선택하여 일렬로 나열하는 것)

   <img src="..\img\picture204.png" alt="png" style="zoom:90%;" />

- **중복이 있는 순열** (n개 중에 중복되는 수가 p개, q개, ..., r개 있을 때 n개를 일렬로 나열)

   <img src="..\img\picture205.png" alt="png" style="zoom:80%;" />

#### **조합(Combination)**

서로 다른 n 개의 물건 중 <u>순서를 생각하지 않고</u> r 개를 택하는 경우

 <img src="..\img\picture114.png" alt="png" style="zoom:60%;" />

- 중복조합 (서로 다른 n개에서 중복을 허락하여 r개를 선택)

   <img src="..\img\picture206.png" alt="png" style="zoom:80%;" />

#### **이항정리**

- 일반항

   <img src="..\img\picture207.png" alt="png" style="zoom:80%;" />

- 이항계수

   <img src="..\img\picture208.png" alt="png" style="zoom:80%;" />

- 이항계수의 성질

   <img src="..\img\picture209.png" alt="png" style="zoom:80%;" />

- 파스칼의 삼각형

   <img src="..\img\picture210.png" alt="png" style="zoom:80%;" />

#### **확률(Probability)**

어떤 시행에서 사건 A가 일어날 가능성을 나타낸 것, **P(A)**

- 용어 정리1

   <img src="..\img\picture211.png" alt="png" style="zoom:70%;" />

- 용어 정리2

   <img src="..\img\picture212.png" alt="png" style="zoom:70%;" />

- 수학적 확률

  - 어떤 시행에서 표본공간의 원소 개수를 n(S), 사건 A의 원소 개수 n(A)일 경우, 사건 A가 발생할 확률

     <img src="..\img\picture213.png" alt="png" style="zoom:80%;" />

- 통계적 확률

  - 일정한 조건에서 같은 시행을 n번 반복했을 때, 사건 A가 일어난 횟수를 r<sub>n</sub> 이라 하면, 이 때 n이 한없이 커짐에 따라 상대도수 <sup>r<sub>n</sub></sup>/n 이 일정한 값 p에 가까워지면 p를 사건 A가 일어날 통계적 확률

     <img src="..\img\picture214.png" alt="png" style="zoom:80%;" />

#### **조건부 확률**

사건 A가 일어났을 때의 사건 B의 조건부확률

- 조건부확률 

   <img src="..\img\picture215.png" alt="png" style="zoom:80%;" />

- 독립사건 (사건 A가 일어나는 여부가 사건 B가 일어날 확률에 영향을 미치지 않을 때)

   <img src="..\img\picture216.png" alt="png" style="zoom:80%;" />

- 종속사건 (사건 A가 일어나는 여부가 사건 B가 일어날 확률에 영향을 미칠 때)

   <img src="..\img\picture217.png" alt="png" style="zoom:80%;" />

- 확률의 곱셈정리

  - 두 사건 A와 B가 동시에 일어날 확률

     <img src="..\img\picture218.png" alt="png" style="zoom:80%;" />

  - 서로 독립인 두 사건 A와 B가 동시에 일어날 확률

     <img src="..\img\picture219.png" alt="png" style="zoom:80%;" />

- 독립 시행

  매번 같은 조건에서 어떤 시행을 반복할 때, 각 시행의 결과가 다른 시행의 결과에 아무런 영향을 주지 않는 경우

  - 한 번 시행에서 사건 A가 일어날 확률이 p, 이 시행을 독립적으로 n회 반복할 때, 사건 A가 r회 일어날 확률

     <img src="..\img\picture220.png" alt="png" style="zoom:80%;" />

#### 확률분포

- 확률변수 : 어떤 시행에서 표본공간의 각 원소에 하나의 실수 값을 대응시키는 것, P(X = x)

- 이산확률변수 : 취할 수 있는 값이 유한개이거나 무한히 많더라도 자연수와 같이 일일이 셀 수 있는 확률변수

- 연속활률변수 : 어떤 범위에 속한 모든 실수 값을 취할 수 있는 확률변수

- 확률분포 : 이산확률변수 X가 취하는 값(x<sub>i</sub>)과 X가 이 값(x<sub>i</sub>)을 취할 확률(p<sub>i</sub>)의 대응 관계

   <img src="..\img\picture222.png" alt="png" style="zoom:80%;" />

- 확률질량함수 : 확률분포의 관계식

    <img src="..\img\picture221.png" alt="png" style="zoom:80%;" />

- 연속확률변수의 평균, 분산, 표준편차

    <img src="..\img\picture224.png" alt="png" style="zoom:80%;" />

   <img src="..\img\picture223.png" alt="png" style="zoom:80%;" />               <img src="..\img\picture226.png" alt="png" style="zoom:80%;" /> <img src="..\img\picture225.png" alt="png" style="zoom:80%;" />

- 평균, 분산, 표준편차의 성질

    <img src="..\img\picture227.png" alt="png" style="zoom:80%;" />

- 이항분포, <img src="..\img\picture237.png" alt="png" style="zoom:70%;" />

  - 1회의 시행에서 사건 A가 일어날 확률을 p, n회의 독립시행에서 그 사건 A가 일어나는 횟수를 확률변수 X라 할 때, 확률변수 X의 확률질량함수

     <img src="..\img\picture228.png" alt="png" style="zoom:80%;" />

  - 이항분포의 평균, 분산, 표준편차

     <img src="..\img\picture229.png" alt="png" style="zoom:80%;" />

- 확률밀도함수 : 연속확률변수 X가 구간 [a, b]에 속하는 모든 실수값을 취하고

   <img src="..\img\picture230.png" alt="png" style="zoom:80%;" /> 와 같이 나타낼 수 있을 때 

- 확률밀도함수의 성질

    <img src="..\img\picture231.png" alt="png" style="zoom:80%;" /> 

- 정규분포, <img src="..\img\picture234.png" alt="png" style="zoom:70%;" /> 

  : 연속확률변수 X의 확률밀도함수 f(x)가 <img src="..\img\picture232.png" alt="png" style="zoom:70%;" /> 일 때

- 정규분포곡선의 성질

   <img src="..\img\picture235.png" alt="png" style="zoom:70%;" />

- 표준정규분포 : 평균이 0, 표준편차가 1인 정규분포 N(0, 1)

- 정규분포의 표준화

   <img src="..\img\picture236.png" alt="png" style="zoom:70%;" />

- 이항분포와 정규분포 : 확률변수 X가 이항분포 <img src="..\img\picture237.png" alt="png" style="zoom:70%;" /> 를 따를 때, n이 충분히 크면 X의 분포는 근사적으로 정규분포 <img src="..\img\picture238.png" alt="png" style="zoom:70%;" /> 을 따름 (단, p + q = 1)

#### 통계적 추정

- 전수조사 : 조사 대상이 되는 자료 전체를 조사하는 것

- 표본조사 : 조사하고자 하는 자료로부터 일부 대상을 뽑아 그 성질을 조사하고, 그 결과로부터 자료 전체의 성질을 추측하는 것

- 모집단 : 조사 대상이 되는 집단 전체

- 표본 : 모집단에서 뽑은 자료 일부

- 임의추출 : 모집단의 각 원소를 같은 확률로 추출하는 것

- 임의표본 : 임의추출된 표본

- 복원추출 : 한 개의 자료를 추출한 후 다시 되돌려 놓고 추출하는 것

- 비복원추출 : 한 개의 자료를 추출한 후 다시 되돌려 놓지 않고 추출하는 것

- 모평균(m), 모분산(σ<sup>2</sup>), 모표준편차(σ)

- 표본평균(X¯), 표본분산(S<sup>2</sup>), 표본표준편차(S)

   <img src="..\img\picture239.png" alt="png" style="zoom:70%;" />

- 표본평균의 분포

  - 모집단이 정규분표 <img src="..\img\picture240.png" alt="png" style="zoom:70%;" /> 을 따르면, 표본평균은 정규분포 <img src="..\img\picture241.png" alt="png" style="zoom:70%;" /> 을 따름
  - 모집단이 정규분포를 따르지 않아도 n이 충분히 크면 표본평균은 정규분포 <img src="..\img\picture241.png" alt="png" style="zoom:70%;" /> 에 가까워짐

- 모평균의 추정 : 모집단에서 추출한 표본을 이용하여 모평균을 추측하는 것

- 신뢰도 : 표본평균의 분포로부터 모평균이 포함될 구간을 얻을 때, 그 구간에 모평균이 포함될 확률

- 신뢰구간 : 모평균이 존재할 것으로 추정되는 구간

- 모평균의 신뢰구간 : 정규분포 <img src="..\img\picture240.png" alt="png" style="zoom:70%;" />을 모집단에서 크기가 n인 표본을 임의추찰할 때

  - 신뢰도 95%의 신뢰구간

     <img src="..\img\picture242.png" alt="png" style="zoom:70%;" />

  - 신뢰도 99%의 신뢰구간

     <img src="..\img\picture243.png" alt="png" style="zoom:70%;" />

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

     <img src="..\img\picture134.png" alt="png" style="zoom:60%;" />

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

      <img src="..\img\picture142.png" alt="png" style="zoom:60%;" />

- 평균, 분산, 표준편차의 성질

   <img src="..\img\picture143.png" alt="png" style="zoom:60%;" /> 

- 이항분포 (binomial distribution)

  : 한 번의 시행에서 사건 A 가 일어날 확률이 p 로 일정할 때, n 번의 독립시행에서 사건 A 가 일어나는 횟수를 확률변수 X 라 하면 X 의 확률질량함수는 <img src="..\img\picture144.png" alt="png" style="zoom: 67%;" /> (단, q = 1-p)

  기호로 <img src="..\img\picture145.png" alt="png" style="zoom: 67%;" />
  - 이 때, 평균, 분산, 표준편차

      <img src="..\img\picture146.png" alt="png" style="zoom:75%;" /> 

- 큰 수의 법칙

  : 어떤 시행에서 사건 A가 일어날 확률이 p일 때, n번의 독립시행에서 사건 A가 일어나는 획수를 X라 하면 임의의 양수 h에 대하여

   <img src="..\img\picture147.png" alt="png" style="zoom:70%;" />

## 연속확률변수와 확률분포

 **continuous probability distribution and  probability distribution**

- **정규분포( Standard normal distribution)**

  : 자연 현상이나 사회 현상을 관찰하여 얻은 자료의 상대도수를, 계급의 크기를 작게하여 히스토그램으로 나타내면 자료의 개수가 커질수록 어떤 값을 중심으로 대칭적으로 분포하고, 중심에서 멀어질수록 도수가 작아지는 종 모향의 곡선에 가까워짐

   <img src="..\img\picture148.png" alt="png" style="zoom:90%;" />
  - **연속확률변수** 

    : 확률변수 X가 어떤 구간에 속하는 모든 실숫값을 취할 때, X를 연속확률변수라고 부름

  - **확률밀도함수** (Probability Density Function) : 

    <img src="..\img\picture149.png" alt="png" style="zoom:80%;" /> 

     <img src="..\img\picture150.png" alt="png" style="zoom:80%;" />


- 연속확률변수의 평균, 분산, 표준편차

  - 구간 [\alpha, \beta] 에서 정의된 연속확률변수 X의 확률밀도함수가 f(x) 일 때, 

       <img src="..\img\picture151.png" alt="png" style="zoom:60%;" />

  - 평균, 분산, 표준편차의 성질

       <img src="..\img\picture152.png" alt="png" style="zoom:60%;" />

- 정규분포 ( normal distribution )

  - 연속확률변수 X의 확률밀도함수 f(x)가  <img src="..\img\picture155.png" alt="png" style="zoom:60%;" /> 

  - 정규분포곡선

    : 위 f(x)의 그래프 <img src="..\img\picture156.png" alt="png" style="zoom:60%;" />

     <img src="..\img\picture157.png" alt="png" style="zoom:90%;" />

    ​                     <img src="..\img\picture158.png" alt="png" style="zoom:80%;" />

  - 오일러 상수

    : 정규분포를 정의하기 위함

     <img src="..\img\picture153.png" alt="png" style="zoom:80%;" />        <img src="..\img\picture154.png" alt="png" style="zoom:80%;" />

  - 정규분포곡선의 성질

     <img src="..\img\picture159.png" alt="png" style="zoom:60%;" />

     <img src="..\img\picture160.png" alt="png" style="zoom:60%;" />

     <img src="..\img\picture161.png" alt="png" style="zoom:70%;" />

    - 정규분포의 정의가 상당히 복잡하여 확률을 구하기 어렵기 때문에,

      정규분포를 평균이 0이고 표준편차가 1인 표준정귭군포로 변환하여 사용

  - **표준정규분포**(Standard normal distribution)

    - 평균이 0이고, 표준편차가 1인 정규분포 N(1, 0)

  - 확률변수 Z가 표준정규분포를 따를 때, Z의 확률밀도함수는 <img src="..\img\picture162.png" alt="png" style="zoom:60%;" />

  - 정규분포의 표준화

    : 일반적인 정규분포를 표준정규분포로 바꾸는 방법

     <img src="..\img\picture163.png" alt="png" style="zoom:60%;" />

  - 확률변수 X가 이항분포 B(n, p)를 따를 때, n이 충분히 크면 확률변수 <img src="..\img\picture164.png" alt="png" style="zoom:60%;" /> 는 표준정규분포 N(0, 1)을 따름

    - 이항분포와 정규분포의 관계

      : 확률변수 X가 이항분포 B(n, p)를 따를 때, n이 충분히 크면 X는 근사적으로 정규분포 <img src="..\img\picture166.png" alt="png" style="zoom:60%;" />를 따름

      - n이 충분히 크다는 것은 일반적으로 np >= 5, nq >=5 일 때를 뜻함

## 모평균의 추정

 **estimation of population mean** 

- **전수조사** : 조사 대상 전체를 조사

- **표본 조사** : 일부분만 택하여 조사

  - **모집단** : 표본조사에서 조사 대상 전체

    **추출**

    - **임의 추출** : 모집단에 속하는 각 대상을 같은 확률로 추출
    - **복원 추출** : 한 개의 자료를 추출한 후 추출한 것을 되돌려 놓고 다시 추출하는 것
    - **비복원 추출** : 되돌려 놓지 않고 계속하여 추출하거나 동시에 여러 개를 추출하는 것

    **모집단의**

    - **모평균 (m)** : 모집단에서 조사하고자 하는 특성을 나타내는 확률변수 X의 평균
    - **모분산 (σ<sup>2</sup>)** : 모집단에서 조사하고자 하는 특성을 나타내는 확률변수 X의 분산
    - **모표준편차 (σ)** : 모집단에서 조사하고자 하는 특성을 나타내는 확률변수 X의 표준편차

  - **표본** : 조사하기 위하여 뽑은 모집단의 일부분

    - **표본의 크기** : 표본에 포함된 대상의 개수

    **표본의**

    - **표본평균** (<img src="..\img\picture168.png" alt="png" style="zoom:60%;" />) : 모집단에서 임의추출한 크기가 n인 표본 X<sub>n</sub>의 평균

       <img src="..\img\picture169.png" alt="png" style="zoom:70%;" />

      - 표본평균 <img src="..\img\picture168.png" alt="png" style="zoom:60%;" /> 의 평균 : <img src="..\img\picture171.png" alt="png" style="zoom:70%;" />
      - 표본평균 <img src="..\img\picture168.png" alt="png" style="zoom:60%;" />  의 분산 : <img src="..\img\picture172.png" alt="png" style="zoom:70%;" />  (n: 표본의 크기)
      - 표본평균 <img src="..\img\picture168.png" alt="png" style="zoom:60%;" /> 의 표준편차 : <img src="..\img\picture173.png" alt="png" style="zoom:70%;" />

    - **표본분산 (S<sup>2</sup>)** : 모집단에서 임의추출한 크기가 n인 표본 X<sub>n</sub>의 분산

       <img src="..\img\picture170.png" alt="png" style="zoom:70%;" />

    - **표본표준편차 (S)** : 모집단에서 임의추출한 크기가 n인 표본 X<sub>n</sub>의 표준편차

- 표본평균의 분포

  - 모평균이 m, 모분산이 σ<sup>2</sup>인 모집단에서 크기가 n인 표본을 임의추출할 때, 다음이 성립

     <img src="..\img\picture174.png" alt="png" style="zoom:70%;" />

- **추정** : 모집단의 성질을 알려고 할 때, 전수조사가 어려운 경우 모집단의 일부인 표본을 조사하여 얻은 정보를 통해 모집단의 성질을 추측 가능. 이 때, 표본에서 얻은 자료를 근거로 모집단의 특성을 나타내는 값을 추측하는 것

  - 표본평균을 이용한 모평균 추정

     <img src="..\img\picture175.png" alt="png" style="zoom:70%;" />

    - 신뢰도 95%의 신뢰구간이란 크기가 n인 표본을 여러 번 추출하여 신뢰구간을 만들 때, 

      모평균 m을 포함하는 구간이 약 95%라는 뜻

    - 표본의 크기 n이 충분히 크면 모표준편차(σ)와 표본표준편차(S)가 거의 같아지므로 σ대신 S를 사용

    - 표본의 크기가 일정할 때 신뢰도가 높아지면 신뢰구간의 길이는 길어짐

      한편, 신뢰도가 일정할 때 표본의 크기가 커지면 신뢰구간의 길이는 짧아짐

       <img src="..\img\picture176.png" alt="png" style="zoom:70%;" />

## 모비율의 추정

- **모비율** (<img src="..\img\picture178.png" alt="png" style="zoom:70%;" />) : 모집단에서의 <u>어떤 사건에 대한 비율</u>을 고려할 때, 그 비율을 그 사건에 대한 모비율이라고 함

  - 일반적으로 모비율 p의 값을 추정하기 위해서는 모집단에서 임의 추출한 표본을 이용할 수 있음

  - 확률변수 X는 어떤 사건이 일어날 확률이 p인 시행을 n번 하였을 때, 그 사건이 일어난 횟수이므로 이항분포 B(n, p)를 따름

    - 따라서 확률변수 X의 평균과 분산은 <img src="..\img\picture181.png" alt="png" style="zoom:70%;" />

  - 모비율의 신뢰구간

     <img src="..\img\picture184.png" alt="png" style="zoom:70%;" />

- **표본비율** (<img src="..\img\picture177.png" alt="png" style="zoom:70%;" />) : 모집단에서 <u>임의추출한 표본에서의 비율</u>을 그 사건에 대한 표본비율이라고 함

   <img src="..\img\picture180.png" alt="png" style="zoom:70%;" />

  - 표본비율 <img src="..\img\picture177.png" alt="png" style="zoom:70%;" />의 평균과 분산 및 표준편차

     <img src="..\img\picture182.png" alt="png" style="zoom:80%;" />

  - 표본비율 <img src="..\img\picture177.png" alt="png" style="zoom:70%;" />의 분포

     <img src="..\img\picture183.png" alt="png" style="zoom:70%;" />

    - n이 충분히 크다는 것은 일반적으로 np >= 5, nq >=5 일 때를 뜻함



<br>

<Br>

> Reference
>
> Sooji Shin
>
> http://soojishin.com/ 
>
> [문제 풀이](# https://www.mathfactory.net/11261 )