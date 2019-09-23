# Spring PSA

PSA(Portable Service Abstraction)

- Portable(휴대용의)이란 환경의 변화와 관계없이 일관된 방식으로 기술 접근 환경을 제공(코드 변경 X)
  - Coding : Servlet, Reactive
    - Server : Tomcat, Jetty, Netty, Undertow

<br>

## Spring PSA? example

- 기존의 Servlet을 사용한 GET, POST 처리

  ```java
  // (/owners/new)
  public class OwnerCreateServlet extends HttpServlet {
      
      // GET
      @Override
      protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException
          super.doGet(req,resp);
  	}
  
  	// POST
  	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException)
          super.doPost(req, resp);
  	}
  }
  ```

  

- Spring PSA을 사용한 GET, POST 처리

  - annotation을 사용하여 코딩을 했지만, 아래에서는 Servlet 기반으로 코드가 동작
  - 추상화 계층을 사용하여 더 편리하게 코딩

  ```java
  @Controller
  class OwnerController {
      
      private static final String VIEWS_OWNER_CREATE_RO_UPDATE_FORM = 			
          										"owners/createOrUpdateOwnerForm"
      
      //...
      
      @GetMapping("/owners/new")
      public String initCreationForm(Map<String, Object> model) {
          Owner owner = new Owner();
          model.put("owner", owner);
          return VIEWS_OWNER_CREATE_RO_UPDATE_FORM;
      }
      
      @PostMapping("/owners/new")
      public String processCreationForm(@Valid Owner owner, BindingResult result) {
          if (result.hasErrors()) {
              return VIEWS_OWNER_CREATE_OR_UPDATE_FORM;
          } else {
              this.owners.save(owner);
              return "redirect:/owners/" + owner.getId();
          }
      }
  }
  ```

<br>

## Spring Web MVC

MVC(Model-View-Controller)

- Spring PSA 중 하나

### Controller

- @Controller 클래스 안에 @RequestMapping(@GetMapping 혹은 @PostMapping) 으로 요청을 Mapping하게 됨
- Mapping이란 뒤의 url에 해당하는 요청이 들어왔을 때, 그 요청을 메소드가 처리하게끔 Mapping한다는 의미 
- // OwnerController.java

    ```java
    // Controller annotation을 사용하면 요청을 Mapping할 수 있는 클래스로 설정
    @Controller		// this is Controller
    class OwnerController {
                                 // VIEWS_OWNER_CREATE_RO_UPDATE_FORM is View
        private static final String VIEWS_OWNER_CREATE_RO_UPDATE_FORM = 	
                                                    "owners/createOrUpdateOwnerForm"

        //...

        // Mapping
        @GetMapping("/owners/new")	
        public String initCreationForm(Map<String, Object> model) {
            Owner owner = new Owner();	// this is Model
            model.put("owner", owner);
            return VIEWS_OWNER_CREATE_RO_UPDATE_FORM;  	// this is View
        }

        // Mapping
        @PostMapping("/owners/new")	
        public String processCreationForm(@Valid Owner owner, BindingResult result) {
            if (result.hasErrors()) {
                return VIEWS_OWNER_CREATE_OR_UPDATE_FORM;	// this is View
            } else {
                this.owners.save(owner);  // this is Model
                return "redirect:/owners/" + owner.getId();
            }
        }
    }
    ```

### View

- View는 /src/resources/templates/owners/createOrUpdateOwnerForm.html(경로)
- 이 파일은 thymeleaf template 엔진을 사용해서 만들어진 View
- // OwnerController.java

    ```java
    @Controller
    class OwnerController {
                                 // VIEWS_OWNER_CREATE_RO_UPDATE_FORM is View
        private static final String VIEWS_OWNER_CREATE_RO_UPDATE_FORM = 	
                                                    "owners/createOrUpdateOwnerForm"

        //...
    ```

- // createOrUpdateOwnerForm.html

    ```java
    <html ... >

    <body>

        <h2>Owner</h2>     // owner is Model
        <form> th:object="${owner}" class="form-horizontal" ...

    // ...
    ```

### Model

- // createOrUpdateOwnerForm.html

    ```java
    <html ... >

    <body>

        <h2>Owner</h2>   // owner is Model
        <form> th:object="${owner}" class="form-horizontal" ...

    // ...
    ```

 - // OwnerController.java

    ```java
    @Controller
    class OwnerController {
        //...

        // Mapping
        @GetMapping("/owners/new")	
        public String initCreationForm(Map<String, Object> model) {
            Owner owner = new Owner();	// Owner is Model
            model.put("owner", owner);
            return VIEWS_OWNER_CREATE_RO_UPDATE_FORM;
        }

        // Mapping
        @PostMapping("/owners/new")	
        public String processCreationForm(@Valid Owner owner, BindingResult result) {
            if (result.hasErrors()) {
                return VIEWS_OWNER_CREATE_OR_UPDATE_FORM;
            } else {
                this.owners.save(owner);	// Owner is Model
                return "redirect:/owners/" + owner.getId();
            }
        }
    }
    ```

<br>

## Spring Transaction

Spring PSA 중 하나

- 사용하는 기술에 따라 `JpatransactionManager`, `Datasource Transactionmanager`, `Hibernate Transactionmanager` 중 골라서 사용 가능



##### Transaction

- Database에서 Data를 주고 받는 과정에서 A-B-C 작업이 모두 완료해야 할 때
  - A, B, C 중 하나의 작업이라도 잘못 되면 그 작업을 다 같이 하면 안됨
  - 작업이 되려면 A, B, C 다 같이 되거나, 아니면 다 같이 취소해야 함



##### Spring Transaction

- @Transactional 이라는 annotation만 붙이면, 해당 메소드는 Transaction 처리가 작동
  - 명시적인 data transaction 코딩을 해주지 않더라도 spring에서 제공 

<br>




> example : https://github.com/spring-projects/spring-petclinic
> refer  : https://www.inflearn.com/course/spring_revised_edition/dashboard