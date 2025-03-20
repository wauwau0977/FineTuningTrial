For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/device/service/impl/HeatingDataReadServiceMock.java' with name 'HeatingDataReadServiceMock.java'... 
Review the following code snippet within the `getData()` method:
```java
ret.setHeatingIn(dtS / 30 + 20);
ret.setHeatingOut(dtS / 30 + 30);
ret.setSoleIn(dtS / 30 + 10);
ret.setSoleOut(dtS / 30 + 5);
ret.setBoilerTemp(dtS / 30 + 30);
```
How can you improve the readability and maintainability of this code? Consider potential issues and suggest refactoring approaches.