For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/data/meteoswiss/MeteoDataPoller.java' with name 'MeteoDataPoller.java' where below a part of it is displayed...
```java
@Scheduled(fixedDelayString = "${thserver.meteoSwiss.pollingInterval:PT900s}", initialDelay = 0)
public void pollData() {
    long t0 = System.currentTimeMillis();
    try {
        List<MeteoSwissEntity> meteoSwissEntity = meteoDataService.getData();
        meteoSwissRepository.saveAll(meteoSwissEntity);
    } catch (Throwable e) {
        String msg = "Exception while reading data from MeteoSwiss";
        log.error(msg, e);
        throw new RuntimeException(msg, e);
    }
    log.info("Did poll live data from MeteoSwiss completed and persisted successfully. dt=" + (System.currentTimeMillis() - t0));
}
```
Explain the purpose of the `@Scheduled` annotation and the parameters used. What happens if `meteoDataService.getData()` throws an exception?