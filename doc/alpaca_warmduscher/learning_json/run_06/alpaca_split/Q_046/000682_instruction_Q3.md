For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/ThserverApplication.java' with name 'ThserverApplication.java' where below a part of it is displayed...
```java
@Scheduled(initialDelay = 50, fixedDelay = Long.MAX_VALUE)
public void logStartup() {
    Map<String, Object> detailInfo = new TreeMap<>();
    detailInfo.put("startupTimes", startupData);
    detailInfo.put("memoryInfo", MemoryInfo.getCurrent());
    detailInfo.put("serverInfo", infoBean);
    this.auditLogRepository.save(new AuditLogEntity("SERVER", "START", "STARTUP", Utils.toJSON(detailInfo), null, null));
}
```
Explain the purpose of the `@Scheduled` annotation on the `logStartup` method, and describe what data is being logged to the audit log.