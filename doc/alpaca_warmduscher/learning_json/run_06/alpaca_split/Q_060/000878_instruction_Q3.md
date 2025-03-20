For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/entity/HeatPumpEntity.java' with name 'HeatPumpEntity.java' where below a part of it is displayed... 
```java
@Entity(name = "HEAT_PUMP")
@Table(indexes = {
       @Index(name = "HEAT_PUMP_IX_1", columnList = "measurementDate"),
})
public class HeatPumpEntity {
   @Id
   private String id = UUIDUtils.generateShortTextUUID();
```
What is the purpose of the `@Entity` and `@Table` annotations, and what does the `@Index` annotation signify in this context?