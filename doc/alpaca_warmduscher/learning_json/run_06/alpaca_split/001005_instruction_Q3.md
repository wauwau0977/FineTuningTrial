For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/entity/meteoswiss/MeteoSwissEntity.java' with name 'MeteoSwissEntity.java' where below a part of it is displayed...
```java
@Entity(name = "METEO_SWISS")
@Table(indexes = {
       @Index(name = "METEO_SWISS_IX_1", columnList = "createDate"),
       @Index(name = "METEO_SWISS_IX_2", columnList = "sunshineMeasureDate"),
       @Index(name = "METEO_SWISS_IX_3", columnList = "temperatureMeasureDate"),
})
public class MeteoSwissEntity {
```
What is the purpose of the `@Index` annotations and how do they contribute to database performance? Explain what each index is targeting.