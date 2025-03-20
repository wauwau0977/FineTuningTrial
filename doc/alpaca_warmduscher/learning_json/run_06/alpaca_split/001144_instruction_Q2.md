For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/ThException.java' with name 'ThException.java'...
Consider this snippet:
```java
public ThException(String message, Throwable cause) {
    super(message, cause);
}
```
What is the purpose of the `Throwable cause` parameter, and how could a developer utilize this functionality when throwing a `ThException`? Give an example scenario within the context of a temperature sensor application (Warmduscher).