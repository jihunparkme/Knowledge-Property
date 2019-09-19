# Spring IoC

제어권이 역전된 것 !?

<br>

## IoC : Inversion of Control
- 일반적으로는 자신이 사용할 의존성을 자신이 만들어서 사용

  ```java
  class OwnerController {
  	private OwnerRepository repository = new OwnerRepository();
  }
  ```

- Spring IoC란, 자신이 사용할 의존성을 누군가 만들어 주는 것. 이것이 제어권의 역전

  ```java
  class OwnerController {
      private OwnerRepository repo;  // OwnerRepository를 사용하지만 자신이 만들지 않음
      
      // OwnerController 밖에서 누군가가 의존성을 줄 수 있도록 생성자를 통해 의존성을 받아옴
      // (=제어권 역전)
      public OwnerController(OwnerRepository repo) {
          this.repo = repo;
      }
  } 
  
  class OwnerControllerTest {
      @Test
      public void create(){
          // 의존성 주입은 = DI(Dependency Injection), DI도 IoC에 포함
          OWnerRepository repo = new OwnerRepository();
          OwnerController controller = new OwnerController(repo);
      }
  }
  ```

  - spring이 bean이라는 객체와 의존성을 관리

    - 의존성 관리란? 필요한 의존성을 필요할 때 적절히 주입해주는 것

<br>

## IoC(Inversion of Control) Container

- Bean을 만들고, Bean들의 의존성을 엮어주고, 만들어진 Bean들을 제공 !
- ApplicationContext 혹은 BeanFactory를 사용
  - 알아서 의존성을 주입을 해주기 때문에 실제로(직접) 사용할 일이 없음
  - IoC Container를 사용하면 아무런 코드를 넣지 않아도 IoC Container에 등록된 Bean을 가져다 사용 가능
- 의존성 주입은 IoC Container 안에 들어있는 Bean끼리만 가능