For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/data/meteoswiss/impl/MeteoDataServiceImpl.java' with name 'MeteoDataServiceImpl.java' where below a part of it is displayed...
```java
   @Value("${thserver.meteoSwiss.urlSunshine}")
   private String urlSunshine;
   @Value("${thserver.meteoSwiss.urlTemperature}")
   private String urlTemperature;
   @Value("${thserver.meteoSwiss.urlWindGust}")
   private String urlWindGust;
   @Value("${thserver.meteoSwiss.stationIds}")
   private List<String> stationIds;
```
What is the purpose of these `@Value` annotations, and how do they contribute to the configuration of the `MeteoDataServiceImpl` class?