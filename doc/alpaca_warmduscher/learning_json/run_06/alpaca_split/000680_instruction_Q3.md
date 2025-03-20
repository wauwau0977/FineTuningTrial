For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/ThserverApplication.java' with name 'ThserverApplication.java' where below a part of it is displayed... 
```java
public ThserverApplication(HeatingDataReadService heatingDataReadService, AuditLogRepository auditLogRepository, InfoBean infoBean, StartupData startupData) {
    this.auditLogRepository = auditLogRepository;
    this.infoBean = infoBean;
    this.startupData = startupData;
    log.info("Created and initialized with heatingDataReadService=" + heatingDataReadService.getClass().getSimpleName());
    log.info("Started " + infoBean);
}
```
What is the purpose of this constructor, and what dependencies are being injected into the `ThserverApplication` class?