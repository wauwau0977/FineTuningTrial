For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/entity/meteoswiss/MeteoSwissStatisticsEntity.java' with name 'MeteoSwissStatisticsEntity.java' where below a part of it is displayed...
```java
@Entity
@Immutable
public class MeteoSwissStatisticsEntity {
   @Id
   private String id = UUIDUtils.generateShortTextUUID();
   // ... other fields and methods ...
}
```
What is the purpose of the `@Entity` and `@Immutable` annotations in this code snippet, and how do they influence the behavior of this class within the application?