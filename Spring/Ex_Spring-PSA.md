# Spring PSA

PSA(Portable Service Abstraction)

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

### Controller

- @Controller 클래스 안에 @GetMapping 혹은 @PostMapping 으로 요청을 Mapping하게 됨
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






> example : https://github.com/spring-projects/spring-petclinic