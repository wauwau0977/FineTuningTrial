For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/dao/meteoswiss/MeteoSwissRepository.java' with name 'MeteoSwissRepository.java' where below a part of it is displayed...

```java
@Query(value = "select * from meteo_swiss ms where station_id=:stationId order by temperature_measure_date desc limit :maxRows", nativeQuery = true)
List<MeteoSwissEntity> getLastEntries(String stationId, int maxRows);
```

What does the `@Query` annotation signify in this context, and what is the purpose of `nativeQuery = true`? Explain how the SQL query within the annotation is used to retrieve data.