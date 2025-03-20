For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/device/service/impl/HeatingDataReadServiceMock.java' with name 'HeatingDataReadServiceMock.java'... 
The code includes the following:
```java
@Override
public List<String> scanAllRegisters(int maxRegister) {
    return List.of("Not implemented");
}
```
What is the purpose of having a method that always returns "Not implemented"? What design considerations might have led to this choice, and what are the potential downsides of this approach?