For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/dao/HeatPumpRepository.java' with name 'HeatPumpRepository.java'... 
Consider the following method signature:

```java
List<HeatPumpStatisticsEntity> findBetweenDatesLimitByFixedIntervalStats(
           Date measurement_date_start,
           Date measurement_date_end,
           @Param("group_every_nth_second") int groupEveryNthSecon;
```

This method retrieves heat pump statistics aggregated by a fixed time interval. Explain the purpose of the `@Param("group_every_nth_second")` annotation and how the `groupEveryNthSecon` parameter influences the query execution and the resulting data. Be specific about what the native query does with this parameter.