For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/entity/analytics/BoilerStatsByHour.java' with name 'BoilerStatsByHour.java' where below a part of it is displayed...

```java
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
@JsonPropertyOrder({"hourOfTheDay", "sumBoilerDiffDecrease", "sumBoilerDiffIncrease", "numOfStatisticRecords1"})
public interface BoilerStatsByHour {
```

What is the purpose of the `@JsonPropertyOrder` annotation and how does it influence the serialization of this interface when used with Jackson?