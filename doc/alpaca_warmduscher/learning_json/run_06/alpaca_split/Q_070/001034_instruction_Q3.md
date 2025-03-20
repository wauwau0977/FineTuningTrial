For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/device/service/HeatingDataPoller.java' with name 'HeatingDataPoller.java' where below a part of it is displayed...
```java
@Scheduled(fixedDelayString = "${thserver.pollingInterval:PT60s}", initialDelay = 0)
public void pollData() {
   long t0 = System.currentTimeMillis();
   HeatPumpEntity heatPumpEntity;
   try {
       heatPumpEntity = heatingDataReadService.getData();
   } catch (Throwable e) {
       String msg = "Exception while reading data from ModBus or MockService.";
       log.error(msg, e);
       throw new RuntimeException(msg, e);
   }
   heatPumpRepository.save(heatPumpEntity);
   log.info("Did poll data and persisted it successfully. dt=" + (System.currentTimeMillis() - t0));
}
```
Explain the purpose of the `@Scheduled` annotation in the `pollData` method.  What configuration determines the interval at which this method is executed, and what does the `initialDelay = 0` signify?