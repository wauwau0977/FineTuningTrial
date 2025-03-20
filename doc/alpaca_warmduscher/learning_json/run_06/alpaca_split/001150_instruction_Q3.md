For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/ThException.java' with name 'ThException.java' where below a part of it is displayed... 

```java
public class ThException extends RuntimeException {
   public ThException(String message) {
       super(message);
   }
   public ThException(String message, Throwable cause) {
       super(message, cause);
   }
}
```

What is the overall design goal of this `ThException` class, considering it offers constructors for both a message and a message with a cause? What kind of use cases would benefit most from this custom exception?