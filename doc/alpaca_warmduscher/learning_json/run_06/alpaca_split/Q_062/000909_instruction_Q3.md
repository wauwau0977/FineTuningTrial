For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/entity/SessionDevice.java' with name 'SessionDevice.java' where below a part of it is displayed... 
```java
@Entity(name = "SESSION_DEVICE")
@Table(indexes = {
       @Index(name = "SESSION_DEVICE_IX_1", columnList = "sessionCreateDate"),
       @Index(name = "SESSION_DEVICE_IX_2", columnList = "sessionId"),
       @Index(name = "SESSION_DEVICE_IX_3", columnList = "clientId"),
})
public class SessionDevice {
```
What is the purpose of the `@Index` annotations, and how might these indexes improve database performance?