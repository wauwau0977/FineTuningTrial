For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/data/meteoswiss/MeteoDataPoller.java' with name 'MeteoDataPoller.java'...
Consider the constructor of `MeteoDataPoller`:
```java
public MeteoDataPoller(MeteoDataService meteoDataService, MeteoSwissRepository meteoSwissRepository) {
    this.meteoDataService = meteoDataService;
    this.meteoSwissRepository = meteoSwissRepository;
    meteoDataService.init(); // init
    log.info("Did init MeteoDataService " + meteoDataService.getClass().getSimpleName());
}
```
What potential issues could arise from calling `meteoDataService.init()` directly within the constructor? How could this be refactored to address these concerns?