For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/dao/HeatPumpRepository.java' with name 'HeatPumpRepository.java' where below a part of it is displayed... 

```java
   @Query(value = "SELECT measurement_date, AVG(temperature) AS avg_temperature " +
           "FROM heat_pump_measurements " +
           "WHERE measurement_date BETWEEN :measurement_date_start AND :measurement_date_end " +
           "GROUP BY measurement_date " +
           "ORDER BY measurement_date ASC " +
           "LIMIT :maxRows")
   List<HeatPumpMeasurement> findMeasurements(
           @Param(value = "measurement_date_start") Date measurementDateStart,
           @Param(value = "measurement_date_end") Date measurementDateEnd,
           @Param(value = "maxRows") int maxRows,
           @Param(value = "group_every_nth_second") int groupEveryNthSecond
   );
```

What is the purpose of the `GROUP BY measurement_date` clause in this SQL query?  How does this affect the results returned?