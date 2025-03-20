For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/entity/analytics/SoleInOutDeltaInOperationStats.java' with name 'SoleInOutDeltaInOperationStats.java' where below a part of it is displayed... 

```java
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import java.util.Date;
@JsonPropertyOrder({"measurementDateStart", "measurementDateEnd", "soleInOutDeltaInOperationAvg", "soleInOutDeltaInOperationMin", "soleInOutDeltaInOperationMax", "compressorState", "totalNumberOfProbesInSampleWindow"})
public interface SoleInOutDeltaInOperationStats {
```
What is the purpose of the `@JsonPropertyOrder` annotation and how does it affect serialization/deserialization of this interface?