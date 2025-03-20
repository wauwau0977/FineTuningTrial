For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/entity/SessionRequest.java' with name 'SessionRequest.java' where below a part of it is displayed...
```java
@Entity(name = "SESSION_REQUEST")
@Table(indexes = {
       @Index(name = "SESSION_REQUEST_IX_1", columnList = "requestDate"),
       @Index(name = "SESSION_REQUEST_IX_2", columnList = "clientId"),
       @Index(name = "SESSION_REQUEST_IX_3", columnList = "sessionId"),
})
public class SessionRequest {
```
What is the purpose of the `@Entity` and `@Table` annotations, and how do the `@Index` annotations contribute to database performance?