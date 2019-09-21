# Spring AOP

AOP(Aspect Oriented Programming) - 관점 지향 프로그래밍

### AOP?

- Before) 흩어진 Action AAA와 BBB

  - 똑같은 일을 수행하는 흩어진 코드들은 수정 시 모두 찾아서 다 바꿔주어야 하는 번거로움이 생김

  ```java
  // class A의 method a, method b는 메시지만 다를 뿐 똑같은 일을 수행
  class A {
      method a () {
          AAA // AAA Action 수정시 다른 클레스 & 메서드를 다 찾아서 수정
          Today is Saturday.
          BBB
      }
       
      method b () {
          AAA
          Hi, My name is Aaron.
          BBB
      }
  }
  
  // 다른 클래스인 class B도 마찬가지로 class A와 같은 일을 수행
  class B {
      method c() {
          AAA
          OH Im hungry.
          BBB
      }
  }
  ```

- After) 모아놓은 Action AAA와 BBB

  - Spring AOP

  ```java
  // 각 클래스와 메서드는 하던 일만 남겨두고
  class A {
      method a () {
          Today is Saturday.
      }
      
      method b () {
          Hi, My name is Aaron.
      }
  }
  
  class B {
      method c() {
          OH Im hungry.
      }
  }
  
  // 공통 Action을 별도의 클래스, 별도 메서드로 뺴냄
  class action {
      method aaabbb(JoinPoint point) {
          AAA
          point.excute()
          BBB
      }
  }
  ```

#### AOP를 구현하는 방법

- AOP 구현 전

  - 프로램의 성능을 측정하는 함수를 여러 메서드에 사용할 경우

    ```java
    public String AOPTestMethod01( ... ) {
        StopWatch stopWatch = new StopWatch();
    	stopWatch.start();
    
    	// 메서드 수행 1
            
        stopWatch.stop();
    	System.out.println(stopWatch.prettyPrint());
    
     	return ..
    }
    
    public String AOPTestMethod02( ... ) {
        StopWatch stopWatch = new StopWatch();
    	stopWatch.start();
    
    	// 메서드 수행 2
            
        stopWatch.stop();
    	System.out.println(stopWatch.prettyPrint());
    
     	return ..
    }
    ```

- AOP 구현

  - 코드가 없는데도 있는것처럼 할 수 있게?!

  1. **컴파일** 

     - A.java 에서 A.class 로 컴파일되는 과정 안에 AOP를 주입 ([AspectJ](https://www.eclipse.org/aspectj/)가 제공)

     > A.java ---(AOP)----> A.class

  2. **바이트코드 조작**

     - A.java -> A.class 로 컴파일된 후 ClassLoader가 class를 읽고 메모리를 올리는 과정에서 AOP 동작 ([AspectJ](https://www.eclipse.org/aspectj/)가 제공)

     > A.java -> A.class ----(AOP)----> Memory

  3. **프록시 패턴 (proxy pattern)** 

     - Spring AOP가 사용하는 방법 
     - 디자인 패턴 중 하나를 사용해서 AOP와 같은 효과를 내는 방법
     - https://refactoring.guru/design-patterns/proxy

<br>

<br>

# 프록시 패턴 (proxy pattern)

기존의 코드를 건드리지 않고 새 기능 추가하기!?

Spring AOP에서는 proxy가 대부분 자동으로 이루어짐

<p align="center">
    <img src="../img/proxy.jpg">
	<p align="center"> 출처 : https://refactoring.guru/design-patterns/proxy </p>
</p>

- Payment.java

  ```java
  public interface Payment {
      void pay(int amount);
  }
  ```

- Cash.java

  ```java
  // stopWatch 기능이 없는 Cash
  public class Cash implements Payment {
      @Override
      public void pay(int amount) {
          System.out.println(amount + " 현금 결제")
      }
  }
  ```
  
- Store.java

  ```java
  // Client
  public class Store {
      Payment payment;
      
      public Store(Payment payment) {
          this.payment = payment;
      }
      
      public void buySomething(int amount) {
          payment.pay(amount);
      }
  }
  ```
- CashPerf.java

  ```java
  // (Proxy) stopwatch 기능이 추가된 CashPerf
  // 이러한 Proxy가 bean으로 등록될 때 자동으로 생성됨
  public class CashPerf implements Payment {
      Payment cash = new Cash();
      
      @Override
      public void pay(int amount) {
          StopWatch stopWatch = new StopWatch();
          stopWatch.start();
          
          cash.pay(amount);
          
          stopWatch.stop();
          System.out.println(stopWatch.prettyPrint());
      }
  }
  ```
  
- StoreTest.java

  ```java
  public class StoreTest {
      @Test
      public void testPay() {
          // CashPerf proxy를 사용할 경우 stopWatch 기능이 동작
          Payment cashPerf = new CashPerf();  
          
          // 그냥 Cash 객체를 사용할 경우 
          // Payment cashPerf = new Cash(); 
          
          Store store = new Store(cashPerf);
          store.buySomething(amount:100);
    }
  }
  ```
  



