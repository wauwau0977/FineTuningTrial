For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/data/meteoswiss/MeteoDataPoller.java' with name 'MeteoDataPoller.java' where below a part of it is displayed...
```java
public MeteoDataPoller(MeteoDataService meteoDataService, MeteoSwissRepository meteoSwissRepository) {
    this.meteoDataService = meteoDataService;
    this.meteoSwissRepository = meteoSwissRepository;
    meteoDataService.init(); // init
    log.info("Did init MeteoDataService " + meteoDataService.getClass().getSimpleName());
}
```
This code uses constructor injection. Explain the benefits of using constructor injection over other forms of dependency injection (like field injection or setter injection) in this context.