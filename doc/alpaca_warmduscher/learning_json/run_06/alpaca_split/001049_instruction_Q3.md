For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/device/service/HeatingDataReadService.java' with name 'HeatingDataReadService.java' where below a part of it is displayed... 

```java
public interface HeatingDataReadService {
   void init() throws Exception;
   HeatPumpEntity getData() throws Throwable;
   List<String> scanAllRegisters(int maxRegister);
}
```

What is the purpose of defining `HeatingDataReadService` as an *interface* rather than a concrete class? Explain the benefits this design choice offers.