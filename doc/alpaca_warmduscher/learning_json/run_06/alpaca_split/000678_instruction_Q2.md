For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/ThserverApplication.java' with name 'ThserverApplication.java'... 
Consider the following snippet from the `logStartup` method:

```java
Map<String, Object> detailInfo = new TreeMap<>();
detailInfo.put("startupTimes", startupData);
detailInfo.put("memoryInfo", MemoryInfo.getCurrent());
detailInfo.put("serverInfo", infoBean);
this.auditLogRepository.save(new AuditLogEntity("SERVER", "START", "STARTUP", Utils.toJSON(detailInfo), null, null));
```

What is the purpose of using `TreeMap` for `detailInfo`, and what are the benefits and drawbacks of choosing `TreeMap` over other `Map` implementations (like `HashMap`) in this specific context?