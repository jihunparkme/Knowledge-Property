# 과목평가

<br/>

## JAVA_0824

### 기본문법

- 연산자

```text
A & B & C 	← A, B, C 모두 판단 
A | B | C 	← A, B, C 모두 판단

A && B && C ← A, B, C 순차적으로 판단, 하나라도 거짓이면, 나머지를 판단하지 않음
A || B || C ← A, B, C 순차적으로 판단, 하나라도 참이면, 나머지를 판단하지 않음
```

- 로컬변수범위

```text
변수가 선언된 함수 내에서만 유효하며, 함수가 종료되면 메모리에서 사라짐

ㅇ 지역변수
	- 값의 초기화 이후 사용
	- 메서드 내에 선언

ㅇ 멤버변수
	- 타입에 따른 자동 초기화
	- 메서드 밖에 선언
```

- switch

```java
switch(입력변수) {
    case 입력값1: ...
         break;
    case 입력값2: ...
         break;
    ...
    default: ...
         break;
}
```

- if

```java
if (조건문) {
    <수행할 문장1> 
    <수행할 문장2>
    ...
}else if (조건문) {
    <수행할 문장1>
    <수행할 문장2>
    ...
}else if (조건문) {
    <수행할 문장1>
    <수행할 문장2>
    ...
...
} else {
   <수행할 문장1>
   <수행할 문장2>
   ... 
}
```

- for

```java
for (초기치; 조건문; 증가치)

for (type var: iterate) {
    body-of-loop
}
```

- while

```java
switch(입력변수) {
    case 입력값1: ...
         break;
    case 입력값2: ...
         break;
    ...
    default: ...
         break;
}
```

<br/>

### Class Design

- 생성자

```text
Class 를 만들 때, 아무런 생성자를 만들지 않으면, Compiler 가 기본생성자( Default Constructor)를 자동으로 생성
```

- toString()

```text
toString() method 는 객체를 만들면 자동으로 만들어 지는데 (사실은 Object Class 로부터 상속) default 로 객체의 주소 정보를 String type 으로 return 

System.out.println(객체) 형태로 객체의 현재 상태를 주소 정보가 아닌 member variables 의 값을 출력하려면 toString() method 를 재정의
```

- modifier

```text
   구분 	Same Class 		Same Package 		Sub Class 		Universe
private	 	  O 			   X 				 X 				X
(default) 	  O 			   O				 X 				X
protected 	  O				   O 				 O 				X
public 		  O 			   O 				 O 			    O
```

<br/>

### 상속

- 상속

```text
- Class B 가 다른 Class A 의 member variables과 method를 그대로 받으면 B가 A를 상속받는다  -> public class B extends a {}

- 어떤 Class가 아무런 상속을 받지 않은 경우, 자동으로 Object Class가 부모

- Java는 단일 상속만 가능
```

- 생성자 호출

```text
- 상속을 받으면서 자신만의 member variables 와 methods 를 가질 수 있음

- 자식 Class의 기본 생성자는 부모 Class의 생성자를 별도로 호출하지 않으면
부모 Class의 기본 생성자를 호출. 하지만 부모 Class의 기본 생성자가 없으면 오류 발생

- super()로 부모 Class의 생성자를 호출할 경우, 항상 첫번째 라인에 와여 함
```

<br/>

### 다형성

- Overriding

```text
- 상속 관계에서 부모 Class의 method를 자식 Class에서 재정의 가능
- method 재정의 시 @Override Annotation 사용 권장
	- 부모 Class의 특정 method를 재정의한다고 compiler에게 명시
	- 부모 Class에 해당 method가 없는 경우 compile 오류 발생
```

- Overloading

```text
- name이 같아도, parameter가 다르면 별개의 method로 간주
- 생성자(Constructor)도 동일
```

- 다형성 활용

```java
// 부모 Type으로 자식 Type의 객체를 Reference 
// 한 개의 Type으로 여러 하위 Type의 객체를 할당받을 수 있음
Object o = new Phone();
Object o = new FolderblePhone();
Phone p = new FolderblePhone();

// 하나의 타입으로 다양한 타입의 실제 객체를 참조

// 재정의(Overriding)된 method만 부모 Type으로 선언한 변수로 호출 가능
// 동적 바인딩 : 함수에 대해서만 자식이 재정의를 했다면 자식 함수가 불림

// 자식 변수에 직접 접근은 불가, 함수를 이용해서 접근해야 함.

/*
[ 상속관계 ]
   A	a(int i){}
   |
   B	b(){}
   |
   C	a(){}, b(int i){}
   |
   D	a(itn i){}, b(){}
   |
   E	a(){}, b(){}
*/

A x = new C(); x.a();	// 오류 : 부모 Class의 method를 재정하지 않았음.
						// 부모 영역만 쳐다보고 있으므로, 자식에만 있는 영역은 접근 불가
C x = new E(); x.b(3);	// C의 b(int i)함수 수행
D x = new B(); x.b();	// 오류 : 자식 Type으로 부모 Type의 객체를 Reference 할 수 없음
B x = new D(); x.a(3);	// D의 a(int i)함수 수행
 						// B는 A에게 상속받았기때문에 a(int i)함수를 상속받은 상태
						// 그 함수를 D에서 재정의한 것이므로
```

- Instanceof

```text
현재 Reference되고 있는 객체가 상속 관계에서 어떤 객체인지 확인
```

- InnerClass(Local)

```java
- Class 안에서 다시 정의되는 Class(member Class)
- 다른 Class에서 사용되지 않고 바깥 Class에서만 의미가 있을 경우 사용

public class OuterPhone {
	
	InnerChip ic;
	
	class InnerChip{
		String serialNo;
	}
	// 생성자 안에서 Inner Class 호출
	public OuterPhone(String serialNo) {
		ic = new InnerChip();
		ic.serialNo = serialNo;
	}
	public OuterPhone() {
		ic = new InnerChip();
	}
}
```

- InnerClass(anonymous)

```java
- Class 안에서 이름이 없이 만들어지는 무명클래스
  - 미완성타입의 자료형을 객체 생성과 동시에 일회성으로 완성
- 재사용되지 않고, 한 번만 사용(ex. Button - 버튼은 다 다른 동작을 수행)
- Event Handling처럼 Interface에 정의된 method의 구현부를 객체 생성 시점에 전달
    
public class PhoneTest {
	public static void main(String[] args) {
		AnonymousFolder af  = new AnonymousFolder();
        // 객체를 생성하는 코드에 바로 Class의 내용을 전달
		af.setFolder(new Folder() {

			@Override
			public void fold() { System.out.println("Anonymous-fold"); }
			@Override
			public void open() { System.out.println("Anonymous-open"); }
			
		});
		
		af.getFolder().fold();
		af.getFolder().open();
	}
}
```

- InnerClass(static)

```java
- Class 안에서 다시 정의되는 Class
- 다른 Class에서 사용되지 않고 바깥 Class에서만 의미가 있을 경우 사용
- 별도의 객체가 만들어지지 않음
  - Class 안에서 static한 변수, 함수, 클래스는 객체 생성 시 열외
    
public class OuterPhoneStatic {

	static class InnerChip{
		public static String serialNo = "12345";
	}

}
```

- Final Class

```java
더이상 자식 Class를 만들지 않을 경우, final keyword를 Class 앞에 사용
    
public final class Phone {
    // ...
}
```

- Modifier

| Modifier | 특징                                                         |                                      |
| :------: | :----------------------------------------------------------- | ------------------------------------ |
|  static  | 별도의 객체를 사용하지 않고 바로 사용<br />Class 이름으로 사용<br />static method 안에서 this.super 사용 불가<br />static method 는 재정의(overriding) 불가 | Math.random()<br />Integer.MAX_VALUE |
|  final   | 상수, 값 변경 불가<br />final method는 재정의(overriding) 불가 |                                      |
| abstract | abstract Class는 상속 불가<br />abstract method는 body를 가지지 않음 |                                      |

- static{}

```java
- Class가 Memory에 Load 된 직후 수행되는 {}로 수행 코드 삽입 가능
- Class 내부에서만 사용되어야하는 초기화 코드 용도로 주로 사용
    
public class StaticBlock {
	static {
		System.out.println("Static Block !!");
	}
	
	static final int MAX_SIZE = 10;
}
```

<br/>

### super와 this

- super

```text
- 자식 클래스에서 상속받은 부모 클래스의 멤버변수를 참조할때 사용
```

- super()

```text
- 자식 클래스가 자신을 생성할 때, 부모 클래스의 생성자를 불러 초기화
(기본적으로 자식 클래스의 생성자에 추가)
```

- this

```text
- 현재 클래스의 인스턴스
- 현재 클래스의 멤버변수 지정 시 사용
```

- this()

```text
- 현재 클래스에 정의된 생성자를 부를때 사용
```



<br/>

### abstract와 interface

- Interface

```text
- 관련된 methods들을 기술하는 데, 선언부만 기술하고, 구현부는 없음
  - 미완성함수로만 이루어진 자료형, 추상 method들의 집합(methods에 집중)
- 한 Class가 여러 개의 interface를 구현(implements)할 수 있음
```

- 추상클래스

```text
- 추상(abstract) 메소드를 하나라도 가지고 있는 클래스
- abstract keyword
- 추상 메소드 : 몸통이 구현되지 않은 미완성 함수 -> 스스로 객체를 만들지 못함
- 추상 Class를 상속받는 Class는 Interface를 구현하는 Class처럼 추상 method의 구현 의무
- 추상 클래스를 상속받으면 다른 Class를 상속받을 수 없음
- Class와 Interface의 중간 역할을 수행하였으나, Interface가 default method를 가지게 되며 애매해짐
```

<br/>

### String과 StringBuilder

- String

```java
불변의 속성
문자열을 조작할 때마다 새로운 메모리 영역을 가리키도록 변경(새로운 문자열 생성)
-> 처음에 선언했던 문자열이 할당되어 있던 메모리 영역은 Garbage로 남아있다가 GC에 의해 사라짐.

* 변하지 않는 문자열을 자주 읽어들이는 경우 주로 사용
* 문자열 추가, 수정, 삭제 등의 연산이 빈번하게 발생하면 힙 메모리에 많은 임시 Garbage가 생성

String s1 = "a";
String s2 = "a";
String s3 = new String("a");
String s4 = new String("a");
System.out.println(s1 == s2);	// true
System.out.println(s2 == s3);	// false
System.out.println(s3 == s4);	// false

String a = "a";
System.out.println(a.concat("b"));	// ab
System.out.println(a);	// a
```

- StringBuilder / StringBuffer

```text
가변성
동일 객체내에서 문자열을 변경

* 문자열 추가, 수정, 삭제 등의 연산이 빈번하게 발생할 경우 주로 사용
* StringBuffer는 동기화 키워드를 지원하여 멀티쓰레드 환경에서 안전
* StringBuilder는 동기화를 지원하지 않아서 단일쓰레드에서 뛰어난 성능
```

- Object

<br/>

### Collection API

| Interface |              구현 Class              |                        설명                         |
| :-------: | :----------------------------------: | :-------------------------------------------------: |
|   List    | LinkedList<br />Stack<br />ArrayList |                 순서 O<br />중복 O                  |
|    Set    |         HashSet<br />TreeSet         |                 순서 X<br />중복 X                  |
|   Queue   |    LinkedList<br />Priority Queue    |                 순서 O<br />중복 O                  |
|    Map    | HashTable<br />HashMap<br />TreeMap  | Key, Value 쌍, 순서 X<br />Key 중복 X, Value 중복 O |

- 자주 사용하는 method

```java
boolean add(E e);
boolean remove(Object o);
boolean isEmpty();
void clear();
int size();
boolean contatins(Object o);
Object[] toArray();
Iterator<E> iterator();
```

- Iterator

```java
- 대부분의 Collection Class들은 iterator Interface를 구현
- Iterator의 method들을 통해 Collection의 각 객체에 접근
  - Collection 자료구조를 순차적으로 순회하는 도구
  - 자료들의 아이템 중 첫번째 화살표를 두고 시작

- 자주 사용하는 메서드
  - hasNext();
    - 현재 화살표가 마지막인지 여부
  - next();
    - 현재 화살표 위치의 아이템을 뱉어내고 다음 위치로 이동
        
        
public void printPatientList() {
    Iterator<Patient> itr = patientList.iterator();
    while(itr.hasNext()){
        Patient p = itr.next();
        System.out.println(p);          
    }
}
```

<br/>

### Exception 개념과 실행

```text
Java는 JVM 실행 시에 발생할 수 있는 다양한 예외 상황을 미리 정의
Throwable은 Error(오류)와 Exception(예외)로 나뉨
Exception은 다시 RuntimeException과 Other Exception으로 구분
```

```java
class A{
	public void ma() throws IOException {
		B b = new B();
		b.mb();
	}
}

/////////////////////////////////////////////////////////////////////

class B{
	public void mb() throws IOException{}
}

/////////////////////////////////////////////////////////////////////

public class ExceptionTest {

	public static void main(String[] args) { 
		
		// #1 try-catch-finally
		FileInputStream fis = null;
		try {
			fis = new FileInputStream("hello.txt");	
		}catch(FileNotFoundException e) {
			System.out.println("Handing Exception : " + e.getMessage());
			e.printStackTrace();
		}finally {
			try {
				fis.close();
			}catch(Exception e) {
				e.printStackTrace();
			}
		}
		
		// #2 throws
        // throws IOException
		A a = new A();
		a.ma();
		
		// #3 throw new
        // throws IOException 발생 시
        // throws FileNotFoundException
		A a = new A();
		try {
			a.ma();
		}catch(IOException e) {
			throw new FileNotFoundException();
		}
		
		// #4 AutoCloseable - no finally for close()
		try( FileInputStream fis2 = new FileInputStream("hello.txt") ) {
			fis2.read();
		}catch(IOException e) {
			System.out.println("Handing Exception : " + e.getMessage());
			e.printStackTrace();
		}
	}
}
```

```java
// Exception  Class를 상속하여 만들고,
// super()를 통해 Exception Message를 지정
public class NotCoronaException extends Exception {
	
    private static final long serialVersionUID = 1L;

    public NotCoronaException(String msg) {
        super(msg);
    }
}

/////////////////////////////////////////////////////////////////////

public class Hospital extends Organization implements MedicalAction{
		// ...
	
	@Override
	public void addPatient(Patient p) throws NotCoronaException{	
        // throw new 로 Exception 호출
		if( ! p.isCorona() ) throw new NotCoronaException("NotConora");
		cdc.getPatientList().add(p);
	}
}

/////////////////////////////////////////////////////////////////////

public class MainTest {

	public static void main(String[] args) {
        
		// ...

		try {
			univHospital.addPatient(p3);
		}catch(NotCoronaException e) {
            // Exception Message 출력
			System.out.println(e.getMessage());
			System.out.println("등록하려는 환자는 Corona 환자가 아닙니다.");
		}
		cdc.printPatientList();
	}
}
```

<br/>

### Thread 개념과 실행

|                                    |                                                         |
| ---------------------------------- | ------------------------------------------------------- |
| 프로세스<br />(Process)            | 개별적으로 동작하는 프로그램<br />(Browser, Eclipse ..) |
| 쓰레드<br />(Thread)               | 프로세스를 구성하는 독립적인 세부 실행 단위(Unit)       |
| 멀티 프로세스<br />(Multi Process) | 여러 개의 프로세스를 동시에 수행                        |
| 멀티 쓰레드<br />(Multi Thread)    | 한 프로세스에서 여러 개의 쓰레드를 동시에 수행          |

```java
// 1. Runnable Interface 구현
public class CoronaRunnable implements Runnable {
	int num;

	public CoronaRunnable(int num) {
		this.num = num;
	}

	@Override
	public void run() {
		// Job
		System.out.println("#" + num + " is Started");
		for (int i = 0; i < 10000; i++) {
			int j = i * 100;
		}
		System.out.println(num);
	}
}

public class CoronaThreadTest {
    public static void main(String[] args) {
        for( int t=0; t<1000; t++ ) {
            CoronaRunnable cr = new CoronaRunnable(t);
            // Thread 객체 생성 시, 생성자의 Parameter로 Runable 객체 전달
            Thread thread = new Thread(cr);
            // Thread 객체 실행 시 start() 호출
            thread.start();

        }
    }
}

/////////////////////////////////////////////////////////

// 2. Thread Class 상속 (자체가 Thread)
public class CoronaThread extends Thread {
    int num;

    public CoronaThread(int num) {
        this.num = num;
    }

    @Override
    public void run() {
		// Job
        System.out.println("#" + num + " is Started");
        for( int i=0; i< 10000; i++ ) {
            int j = i*100;
        }
        System.out.println(num);
    }
}

public class CoronaThreadTest {

    public static void main(String[] args) {
        for( int t=0; t<1000; t++ ) {
			// Thread 생성
            // extends Thread의 경우 자체가 이미 Thread이므로 별도의 Thread 생성 불필요
            CoronaThread thread = new CoronaThread(t);
            // Thread 객체 생성 후 바로 start() 호출
            thread.start();
        }
    }
}
```

<br/>

### File IO 개념

- 입력

```java
bufferedReaer br =new bufferedReaer(new InputStreamReader(new FileInputStream));
- FileInputStream : 파일의 형태를 byte 로 받아 옴
- InputStreamReader : byte 형태를 단어 char 로 바꿔서 정리
- bufferedReaer : char형을 인식

* char형으로 하는 이유는 우리가 다룰 때 byte 형태보다 char형이 접근이 용이

BufferInputStream br=new BufferInputStream (new FileInputStream));
- BufferInputStream : byte 형태로 입력을 받음

* FileInputStream 이후에 BufferInputStream를 사용하는 이유는 버퍼에 저장을 해 한꺼번에 입력을 받아 속도를 더욱 빠르게 하기 위한 기능
```

- 출력

```java
bufferedwriter br =new bufferedwriter (new outputStreamReader(new FileoutputStream))
- FileoutputStream : 파일의 형태를 byte 로 입력
- outputStreamwrite : char 형태를 단어 byte 로 바꿔서 정리
- bufferedwriter : char형을 인식

* char형으로 하는 이유는 우리가 다룰 때 byte 형태보다 char형이 접근이 용이

BufferOutputStream br=new BufferOutputStream (new FileOutputStream));
- BufferOutputStream : byte 형태로 출력을 함

* FileOutputStream 이후에 BufferOutputStream를 사용하는 이유는 버퍼에 저장을 해 한꺼번에 출력을 해 속도를 더욱 빠르게 하기 위한 기능
```

- 객체 직렬화

```java
객체 직렬화 : 데이터를 가지고 있는 객체를 그대로 전송할 수 있는 형태(byte)로 바꾸는 방법을 말합니다.

ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream());

ObjectInputStream ois =new ObjectInputStream(new FileInputStream());

- 이것을 해주기 위해 객체 직렬화해줄 대상에 Serializable 을 implements
- 이때 transient를 변수에 붙이면 해당 변수는 객체 직렬화에서 제외
```

<br/>

### Network

- TCP/UDP 개념

```text
- TCP : 전송의 보장
  - 데이터가 순서대로 도착, 데이터 도착을 확인(미수신 시 재전송)
  
- UDP : 전송의 보장 X 
  - 데이터 도착에 순서가 없음, 데이터 도착을 확인 안함
  - Broadcasting에 많이 활용 (ex. 방송, 라디오..)
```

- Network API

```java
// Server
public class NetworkSimpleServer {
	public static void main(String[] args) {
		int port = 5100;
		// Port 번호를 생성자에 전달
		try (ServerSocket serverSocket = new ServerSocket(port)) {

			System.out.println("NetworkSimpleServer Started");

			while (true) {
				// Socket 객체가 생성되면 Clinet의 접속을 대기
                // Client가 접속하면 .accept()가 호출되면서 Socket 객체를 전달
				Socket socket = serverSocket.accept();
                // Socket으로부터 IOStream을 얻어 통신
                // Client가 접속하면 필요한 Service 수행 후 다시 다른 Client 접속을 받음
                // 동시에 많은 Client 접속 시 Thread 적용 필요
				OutputStream output = socket.getOutputStream();
				PrintWriter writer = new PrintWriter(output, true);
				writer.println("Hello SSAFY!");
			}

		} catch (IOException e) {
			System.out.println("NetworkSimpleServer exception: " + e.getMessage());
			e.printStackTrace();
		}

		System.out.println("NetworkSimpleServer Ended");
	}
}


// Client
public class NetworkSimpleClient {

	public static void main(String[] args) {
		String host = "localhost";
		int port = 5100;
        
		// IP와 Port번호를 이용해서 Socket 객체 생성
		try (Socket socket = new Socket(host, port)) {
			// Server에 접속되면 socket 객체로부터 IO Stream을 얻어 통신
			InputStream input = socket.getInputStream();
			BufferedReader reader = new BufferedReader(new InputStreamReader(input));

			String message = reader.readLine();
			System.out.println(message);

		} catch (IOException e) {
			System.out.println("NetworkSimpleClient exception: " + e.getMessage());
			e.printStackTrace();
		}
	}
}


// HTTP Server
public class NetworkHttpServer {
	public static void main(String[] args) throws IOException {
		// localhost:8080 접속
		try (ServerSocket ss = new ServerSocket(8080)) {
			System.out.println("[WebServer is ready]");
			
			while (true) {
				try ( Socket socket = ss.accept() ) {

					BufferedWriter bw = 
                        new BufferedWriter(
                        new OutputStreamWriter(socket.getOutputStream(), "UTF-8"));
					
					String html = "<html><body><h1>Hello SSAFY!! 와우!</h1></body></html>";
					bw.write("HTTP/1.1 200 OK \r\n");
					bw.write("Content-Type: text/html;charset=utf-8\r\n");
					bw.write("Content-Length: " + html.length() + "\r\n");
					bw.write("\r\n");
					bw.write(html);
					bw.write("\r\n");
	                bw.flush();

				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
```



<br/>

### JDBC API

```java
public class JDBCMySQLTest1 {

    public static void main(String[] args)throws Exception {
        // 1. Driver Loading
        // JDBC Driver를 DriverManager에 등록
        Class.forName("com.mysql.cj.jdbc.Driver");
        
        // 2. Connection 
        Connection con = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/corona_db?serverTimezone=UTC&useUniCode=yes&characterEncoding=UTF-8","ssafy","ssafy");
        
        // 3. Statement Create
        PreparedStatement pst = con.prepareStatement("select * from patient");
        
        // 4. SQL Execute ()
        ResultSet rs=st.executeQuery();

        // 5. result
        while(rs.next()){
            System.out.println(rs.getString("name")+" : "+rs.getInt("age"));
        }
        
        // 6. close
        rs.close();
        st.close();
        con.close();
    }
}
```

```text
### Connection

- JDBC DriverMAnager를 히용하여 DB에 연결되면 연결 객체인 Connection 객체를 얻음
  - Connection 객체로부터 SQL문을 작성할 수 있는 Statement / PreparedStatement 객체를 얻음
  - SQL문이 준비가 되면 executeQuery(SELECT) 또는 executeUpdate(INSERT, UPDATE, DELETE) 수행
  - 사용 후 반드시 close() 하여 연결 끊기
  - 연결 과정은 매우 비싼 프로세스이므로 DB를 자주 사용하는 경우 Connection Pool을 활용하여 연결을 관리

### Statement

- 가장 기본적인 SQL 작성 객체
- 전달된 SQL을 수행 시 내부적으로 SQL을 다시 작성하는 구조로 효율성이 떨어짐
- SQL Injection 등 보안에 불리
  - 대신 PreparedStatiement 사용
  - Statement보다 효율적이고 보안에 유리

### excuteXXX

- SQL이 준비되면 Connection 객체를 통해 DB로 전달하로 DB는 SQL을 수행한 후 결과를 return
- INSERT, DELETE, UPDATE 등은 executeUpdate()를 사용하고, return 값은 영향 받은 데이터 건수
- SELECT excuteQuery()를 사용하고, return 결과를 담고 있는 ResultSet 객체

### ResultSet

- SELECT 수행 후 얻게 되는 ResultSet 객체는 Grid 구조와 같은 형태로 결과값을 가짐
- next()를 통해 데이터 건수의 존재를 확인한 후, getXXX()를 통해 데이터 건별로 컬럼 값을 얻음
- 문자열이면 getString(), 정수이면 getInt() 처럼 Type에 매칭되는 getXXX()를 호출
- Parameter는 컬럼명을 String으로 전달할 수도 있고, 숫자로 SELECT 문의 Index를 전달할 수도 있음
  - Index는 1부터
```

<br/>

### XML 파서

- SAX

```text
- 문서를 한번 쭉 읽으면서 tag의 발생별로 처리
- 빠른 반면 한번에 처리하기 때문에 다양한 탐색 불가
- tag를 만나면 실행되는 event 기반의 처리 방식을 사용하므로 별도의 Handler 필요
  - 각 tag의 발생에 따라 수행할 Job을 정의
```

```java
public class newsReportSaxHandler extends DefaultHandler {

	private ArrayList<Item> itemList = new ArrayList<>();
	private Item item;
	private StringBuilder data = null;

	boolean bItem = false;
	boolean bTitle = false;
	boolean bLink = false;
	boolean bDescription = false;
	boolean bAuthor = false;
	boolean bGuid = false;
	boolean bComments = false;
	boolean bPubDate = false;

	@Override
	public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
		if(qName.equals("item")) {
			bItem = true;
			item = new Item();
		}
		else if (qName.equals("title")) {
			bTitle = true;
		} else if (qName.equals("link")) {
			bLink = true;
		} else if (qName.equals("description")) {
			bDescription = true;
		} else if (qName.equals("author")) {
			bAuthor = true;
		} else if (qName.equals("guid")) {
			bGuid = true;
		} else if (qName.equals("comments")) {
			bComments = true;
		} else if (qName.equals("pubDate")) {
			bPubDate = true;
		} 

		data = new StringBuilder();
	}

	@Override
	public void endElement(String uri, String localName, String qName) throws SAXException {
		if(!bItem) return;
		if (bTitle) {
			item.setTitle(data.toString());
			bTitle = false;
		} else if (bLink) {
			item.setLink(data.toString());
			bLink = false;
		} else if (bDescription) {
			item.setDescription(data.toString());
			bDescription = false;
		} else if (bAuthor) {
			item.setAuthor(data.toString());
			bAuthor = false;
		} else if (bGuid) {
			item.setGuid(data.toString());
			bGuid = false;
		} else if (bComments) {
			item.setComments(data.toString());
			bComments = false;
		} else if (bPubDate) {
			item.setPubDate(data.toString());
			bPubDate = false;
		} else if (bItem) {
			itemList.add(item);
			bItem = false;
		}
	}
		
	@Override
	public void characters(char[] ch, int start, int length) throws SAXException {
		 data.append(new String(ch, start, length));
	}

	public Item getItemReport() {
		return item;
	}
	
	public ArrayList<Item> getItemReportList() {
		return itemList;
	}
}

///////////////////////////////////////////////////////////////////////////////////


public class newsParserSax {
	public static void main(String[] args) {
		String url = "http://rss.etnews.com/Section902.xml";
		SAXParserFactory saxParserFactory = SAXParserFactory.newInstance();

		try {
			SAXParser saxParser = saxParserFactory.newSAXParser();
			newsReportSaxHandler handler = new newsReportSaxHandler();
			saxParser.parse(url, handler);

			for (Item item  : handler.getItemReportList()) {
				System.out.println(item);
			}

		} catch (ParserConfigurationException | SAXException | IOException e) {
			e.printStackTrace();
		}
	}
}
```

- DOM

```text
- 문서를 다 읽고 난 후, 문서 구조 전체를 자료구조에 저장하여 탐색하면서 처리	
- 느리고, 무겁지만 다양한 탐색 가능
```

```java
public class newsParserDom {

	public static void main(String[] args) {
		
		String url = "http://rss.etnews.com/Section902.xml";
		
		DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
		DocumentBuilder builder;

		ArrayList<Item> itemList = new ArrayList<>();

		try {

			builder = factory.newDocumentBuilder();
			Document doc = builder.parse(url);
			doc.getDocumentElement().normalize();

			Element rss = doc.getDocumentElement();
			Node channel = rss.getFirstChild().getNextSibling();
			NodeList childNodes = channel.getChildNodes();
			
			for (int i = 0; i < childNodes.getLength(); i++) {
				Node node = childNodes.item(i);
				if (node.getNodeType() == Node.ELEMENT_NODE) {

					Element element = (Element) node;
					String textContent = element.getTextContent();
					String nodeName = element.getNodeName();
					switch (nodeName) {
					case "item":
						NodeList itemChildNodes = element.getChildNodes();
						Item item = new Item();
						for (int j = 0; j < itemChildNodes.getLength(); j++) {
							Node childNode = itemChildNodes.item(j);
							if (childNode.getNodeType() == Node.ELEMENT_NODE) {
								Element childElement = (Element) childNode;
								String childTextContent = childElement.getTextContent();
								String childNodeName = childElement.getNodeName();
								switch (childNodeName) {
								case "title":
									item.setTitle(childTextContent);
									break;
								case "link":
								    item.setLink(childTextContent); 
									break;
								case "description":
									item.setDescription(childTextContent);
									break;
								case "author":
									item.setAuthor(childTextContent);
									break;
								case "guid":
									item.setGuid(childTextContent);
									break;
								case "comments":
									item.setComments(childTextContent);
									break;
								case "pubDate":
									item.setPubDate(childTextContent);
									break;
								}
							}
						}
						itemList.add(item);
					}
				}
			}
		} catch (SAXException | ParserConfigurationException | IOException e1) {
			e1.printStackTrace();
		}
		
		for (Item i : itemList)
			System.out.println(i);
	}

}
```

