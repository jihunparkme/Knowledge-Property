# C Language

<Br>

## 포인터

### 포인터란?

- 주소를 저장하는 변수
- C 언어의 장점 중 하나
- 사용 장점
  - 메모리 주소를 참조해서 다양한 자료형 변수들의 접근과 조작 용이
  - 메모리 주소를 참조하여 배열과 같은 연속된 데이터에 접근과 조작 용이
  - 동적 할당된 메모리 영역(힙영역)에 접근과 조작 용이 

### 포인터 변수의 선언과 사용

- 포인터 변수의 선언
  

 <img src="..\img\pointer1.png" alt="img" style="zoom:150%;" />

  - ex)
    
     <img src="..\img\pointer2.png" alt="img"  />

  ```C
  #include <stdio.h>
  
  int main() {
  	char c = 'A';
  	char* cp = NULL;	// 포인터 선언
  
  	cp = &c;			// 포인터에 자료형의 주소를 저장
  
  	printf("%x, %c, %c\n", &c, c, *&c);
  	printf("%x, %x, %x\n", &cp, cp, *&cp);
  
  	printf("%c\n", c);		// 직접 접근
  	printf("%c\n", *cp);	// 간접 접근
  }
  ```

  ```
  53f993, A, A
  53f984, 53f993, 53f993		// c의 주소와 cp의 주소가 같다는 것을 확인
  A
  A
  ```

  - ex)
    
     <img src="..\img\pointer3.png" alt="img"  />

  ```c
  #include <stdio.h>
  
  int main() {
  	int a = 0, b = 0, c = 0;
  	int* ip = NULL;		// 포인터 변수 선언
  
  	ip = &a;		// 변수 a의 주소 저장
  	*ip = 10;
  	printf("%d %d %d %d\n", a, b, c, *ip);
  
  	ip = &b;		// 변수 b의 주소 저장
  	*ip = 20;
  	printf("%d %d %d %d\n", a, b, c, *ip);
  
  	ip = &c;		// 변수 c의 주소 저장
  	*ip = 30;
  	printf("%d %d %d %d\n", a, b, c, *ip);
  }
  ```

  ```
  10 0 0 10
  10 20 0 20
  10 20 30 30
  ```

- 잘못 사용된 포인터
  

 <img src="..\img\pointer4.png" alt="img"  />

- 포인터 변수의 초기화 방법 2가지
  
   <img src="..\img\pointer5.png" alt="img"  />

### 다차원 포인터 변수의 선언과 사용

- 다차원 포인터 변수?

  - 2차원 이상의 포인터 변수를 의미
    - int* p1 = NULL;         //1차원 포인터 변수
      
      -역할 : 일반 변수의 주소를 저장
      
    - int** p2 = NULL;       //2차원 포인터 변수
      
      -역할: 1차원 포인터 변수의 주소를 저장
      
    - int*** p3 = NULL;     //3차원 포인터 변수 
      
      -역할: 2차원 포인터 변수의 주소를 저장
    
  - ex)
    
     <img src="..\img\pointer6.png" alt="img"/> <img src="..\img\pointer7.png" alt="img"/> <img src="..\img\pointer8.png" alt="img"/>
    
    ```C
    #include <stdio.h>
    
    int main() {
    	char c1 = 'A';
    	char* cp = NULL;	// 1차원 포인터 변수 선언
    	char** cpp = NULL;	// 2차원 포인터 변수 선언
    
    	cp = &c1;
    	cpp = &cp;			// 1차원 포인터 변수의 주소 저장
    
    	printf("%c %x %x \n", c1, cp, cpp);		// 각 변수에 저장된 데이터 출력
    	printf("%x %x %x \n", &c1, &cp, &cpp);	// 각 변수의 주소 출력
    	printf("%c %c %c \n", c1, *cp, **cpp);	// 문자 출력
    }
    ```
    
    ```
    A eff8a7 eff898
    eff8a7 eff898 eff88c
    A A A
    ```
  

### 주소의 가감산

- ex)
  
 <img src="..\img\pointer9.png" alt="img"/>
  
  ```c
  #include <stdio.h>
  
  int main() {
  	char c = 'A';
  	char* cp = NULL;
  	char** cpp = NULL;
  
  	cp = &c;
  	cpp = &cp;
  
      // 주소의 가산
  	printf("%x %x %x \n", &c, &cp, &cpp);
  	printf("%x %x %x \n", &c + 1, &cp + 1, &cpp + 1);
  
      // 값의 가산
  	printf("%c %x %x \n", c, cp, cpp);
  	printf("%c %x %x \n", c + 1, cp + 1, cpp + 1);
  }
```
  
  ```
  5af7ab 5af79c 5af790
  5af7ac 5af7a0 5af794
  // char는 크기가 1이므로 주고값 1 증가, 포인터 변수는 크기가 4이므로 주소값 4 증가
  
  A 12ffbe7 12ffbd8
  B 12ffbe8 12ffbdc
  // A의 다음 주소 값인 B가 출력, 포인터 변수의 주소도 1 증가
```
  
- ex)
  
<img src="..\img\pointer10.png" alt="img"/> 
  
  ```c
  #include <stdio.h>
  
  int main() {
  	int array[3] = { 10,20,30 };
  	int* ip = NULL;
  	int** ipp = NULL;
  
  	ip = array;
  	ipp = &ip;
  
  	printf("%d %d %d \n", array[0], array[1], array[2]);
  	printf("%d %d %d \n", *(ip + 0), *(ip + 1), *(ip + 2));
  	printf("%d %d %d \n", *(*ipp + 0), *(*ipp + 1), *(*ipp + 2));
  }
```
  
  ```
  10 20 30
  10 20 30
  10 20 30
  ```

### 함수 포인터

- 함수의 시작 주소를 저장하는 변수
  
    <img src="..\img\pointer12.png" alt="img"/>

- 함수 포인터의 필요성
  
    - 일반적인 함수 호출 보다 빠른 처리 속도를 기대
  
  - 컴파일러, 인터프리터, 게임 프로그래밍과 같은 시스템 프로그래밍 분야에서 사용
  
  - ex)
  
      <img src="..\img\pointer11.png" alt="img"/>
  
    1. 포인팅 대상 함수: void add(double num1, double num2)
    2. 함수 포인터: void (*pointer) (double, double);
    3. 함수 포인터에 함수 시작 주소 저장: pointer=add;
    4. 함수 포인터를 이용한 함수 호출: pointer(3.1, 5.1);
  
    ```c
    #include <stdio.h>
    
    void add(double num1, double num2)
    {
    	double result;
    	result = num1 + num2;
    	printf("%lf + %lf = %lf입니다.\n", num1, num2, result);
    }
    
    int main()
    {
    	double x = 3.1, y = 5.1;
    	void(*pointer) (double, double);		//함수 포인터 선언
    
    	printf("add 함수의 주소 : %x\n", add);	// add 함수의 주소 출력
    	printf("함수 포인터의 주소 : %x \n", &pointer);		// 함수 포인터 주소 출력
    
    	pointer = add;		// 함수 포인터 pointer에 함수의 시작 주소 add를 저장
    	pointer(x, y);		// 함수 포인터를 이용한 호출
    
    	return 0;
  }
    ```
  
    ```
    add 함수의 주소 : 1231375
    함수 포인터의 주소 : 3cfb88
    3.100000 + 5.100000 = 8.200000입니다.
    ```

## 포인터와 배열

### 포인터와 1차원 배열

```c
  #include <stdio.h>
  
  int main()
  {
  	int array[3] = { 10, 20, 30 };
  	printf("%d %d %d \n", sizeof(array), sizeof(array + 0), sizeof(&array[0]));
  }
```

```
  12 4 4
  // 포인터 변수의 크기는 4
```

 <img src="..\img\pointer13.png" alt="img"/>

- 포인터 변수를 통한 1차원 배열 요소의 주소 접근

  - 배열의 시작 주소 저장

    ```c
    #include <stdio.h>
    int main()
    {
    	int array[3] = { 10, 20, 30 };
    	int* p = NULL;
    	p = array;
    
        // 주소 확인
    	printf("%x %x %x \n", p, p + 0, &p[0]); // == array, array+0, &array[0]
    	printf("%x %x \n", p + 1, &p[1]);       // == array+1, &array[1]
    	printf("%x %x \n", p + 2, &p[2]);       // == array+2, &array[2]	
    }
    ```

    ```
    76f900 76f900 76f900
    76f904 76f904
    76f908 76f908
    ```

  - 포인터 변수를 통한 1차원 배열 요소의 값 접근

    ```c
    #include <stdio.h>
    
    int main()
    {
    	int array[3] = { 10, 20, 30 };
    	int* p = NULL;
    	p = array;
    
    	printf("%d %d %d \n", *p, *(p + 0), *&p[0]);  
    	printf("%d %d \n", *(p + 1), *&p[1]);   
    	printf("%d %d \n", *(p + 2), *&p[2]);  
    }
    ```

    ```
    10 10 10
    20 20
    30 30
    ```

    - 결론 1:　*(p+i) == *&p[i] == p[i]
    - 결론 2:　*(array+i) == *&array[i] == array[i]

- 포인터 변수와 배열의 크기 차이

  - 포인터 변수 : 4바이트로 고정
  - 배열 : 배열의 길이에 따라 가변적

- 주소 가감산을 이용한 배열의 접근
  
 <img src="..\img\pointer14.png" alt="img"/>
  
  ```c
  #include <stdio.h>
  int main()
  {
  	int array[3] = { 10, 20, 30 };
  	int* p = NULL;
      
  	p = array;		// p = &array[0];
  	printf("%d %d %d \n", p[0], p[1], p[2]);
  	printf("%d %d %d \n", *p, *(p + 1), *(p + 2));
  	// *p == *(p+0) == p[0] 
      // *(p+1) == p[1] 
      // *(p+2) == p[2]
  
  	p = array + 1;	// p = &array[1];
  	printf("%d %d %d \n", p[-1], p[0], p[1]);
  	printf("%d %d %d \n", *(p - 1), *p, *(p + 1));
  	// *(p-1) == p[-1] 
      // *p == *(p+0) == p[0] 
      // *(p+1) == p[1]
  
  	p = array + 2;	// p = &array[2];
  	printf("%d %d %d \n", p[-2], p[-1], p[0]);
  	printf("%d %d %d \n", *(p - 2), *(p - 1), *p);
  	// *(p-2) == p[-2] 
      // *(p-1) == p[-1] 
      // *p == *(p+0) == p[0]
  }
```
  
  ```
  10 20 30
  10 20 30
  10 20 30
  10 20 30
  10 20 30
  10 20 30
```
  
- 포인터 변수를 통한 1차원 배열 값 입력
  <img src="..\img\pointer15.png" alt="img"/>

  ```c
  #include <stdio.h>
  int main()
  {
  	int array[3];
  	int* p = NULL;
  
  	p = array;
  
  	*p = 10;
  	printf("%d %d %d \n", p[0], p[1], p[2]);
  
  	*(p + 1) = 20;
  	printf("%d %d %d \n", p[0], p[1], p[2]);
  
  	*(p + 2) = 30;
  	printf("%d %d %d \n", p[0], p[1], p[2]);
  }
  ```

  ```
  10 -858993460 -858993460
  10 20 -858993460
  10 20 30
  ```

- 포인터변수의 이동을 통한 1차원 배열 값 입력

     <img src="..\img\pointer16.png" alt="img"/>

  ```c
  #include <stdio.h>
  int main()
  {
  	int array[3];
  	int* p = NULL;
  
  	p = array;
  	*p = 10;
  	printf("%d %d %d \n", p[0], p[1], p[2]);
  
  	p = p + 1;
  	*p = 20;		// p[1]=20; 
  	printf("%d %d %d \n", p[-1], p[0], p[1]);
  
  	p = p + 2;
  	*p = 30;		// p[2]=30;
  	printf("%d %d %d \n", p[-2], p[-1], p[0]);
  }
  ```

  ```
  10 -858993460 -858993460
  10 20 -858993460
  10 20 30
  ```

### 포인터와 2차원 배열

- 2차원 배열에서 array[i] == *(array+i) 는 주소
  
    <img src="..\img\pointer17.png" alt="img"  />
  
- 1차원 배열: *(array+i) == array[i] == *&array[i] 는 값 
  
  - 2차원 배열: *(array+i) == array[i] == *&array[i] 는 주소 
  
- 포인터 변수를 통한 2차원 배열의 접근

  - 2차원 배열의 시작 주소를 저장

  - 1차원 포인터 변수는 2차원 배열을 1차원으로만 접근 가능

    ```c
    #include <stdio.h>
    int main()
    {
    	int array[2][3] = { 10,20,30,40,50,60 };
    	int* p = NULL;     //1차원 포인터 이므로 배열 접근 시 1차원 적으로 접근
    
    	p = array;	   // 포인터 변수에 배열의 시작 주소를 저장
        // p=&array[0][0]; 
        // p=array[0];
        // p=*(array+0)
    
    	printf("%x %x %x \n", &p[0], &p[1], &p[2]);	    
        //= printf("%x %x %x \n", p+0, p+1, p+2);
    	printf("%x %x %x \n", &p[3], &p[4], &p[5]);	    
        //= printf("%x %x %x \n", p+3, p+4, p+5);
    
    	printf("%d %d %d \n", p[0], p[1], p[2]);	
        //= printf("%d %d %d \n", *(p+0), *(p+1), *(p+2));
    	printf("%d %d %d \n", p[3], p[4], p[5]);	
        //= printf("%d %d %d \n", *(p+3), *(p+4), *(p+5));
    }
    
    ```

    ```
    7ffe80 7ffe84 7ffe88
    7ffe8c 7ffe90 7ffe94
    10 20 30
    40 50 60
    ```

- 배열 포인터

  - 열을 지정할 수 있는 포인터 (배열을 가리키는 포인터)
    
      <img src="..\img\pointer18.png" alt="img"  />
        

- 배열 포인터 변수를 통한 2차원 배열의 접근 (열을 지정)
  
    ```c
    #include <stdio.h>
    int main()
    {
    	int array[2][3] = { 10,20,30,40,50,60 };
    	int(*p)[3] = NULL;		// 배열 포인터 변수 p 선언
    
    	p = array;		// 포인터 변수에 배열의 시작 주소를 저장
        // p=&array[0][0]; // p=array[0]; 
    
    	printf("%d %d %d \n", p[0][0], p[0][1], p[0][2]);
    	printf("%d %d %d \n", p[1][0], p[1][1], p[1][2]);
    
    }
  ```
  
    ```
    10 20 30
    40 50 60
    ```

## 포인터 배열

- 포인터 배열

  - 주소를 저장하는 배열
    
      <img src="..\img\pointer19.png" alt="img" style="zoom:120%;" />
        

- 포인터 배열의 선언
  
    ```c
    #include <stdio.h>
    int main()
    {
    	int a = 1, b = 2, c = 3;
    	int* pointer[3] = { NULL, NULL, NULL };
    
    	pointer[0] = &a;
    	pointer[1] = &b;
    	pointer[2] = &c;
    	return 0;
    }
  ```
  
- 포인터 배열의 필요성
  
    - 포인터 변수가 많아지는 단점을 보완
  - ‘포인터 배열’의 요소로 주소를 체계적으로 관리
  
- 포인터 배열과 배열 포인터의 차이
  
  - 배열 포인터 변수
  
      -n열을 가진 2차원 배열의 시작 주소를 저장
     int (*p)[n] = NULL;
  
  - 포인터 배열 변수
  
      -여러 주소를 저장할 수 있는 배열
       int* p[3] = {NULL, NULL, NULL};