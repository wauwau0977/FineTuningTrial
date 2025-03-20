For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/MySessionFilter.java' with name 'MySessionFilter.java' where below a part of it is displayed... 

```java
    sessionDeviceRepository.findById(sessionId).ifPresentOrElse(
                   device -> log.debug("Is already in DB"),
                   () -> {
                       log.info("Need to create a session device, as it did not exist." + sessionDevice);
                       sessionDeviceRepository.save(sessionDevice);
                   });
```

What is the purpose of this code snippet within the `doFilter` method, and how does it handle existing and new session devices in the database? Explain the use of `ifPresentOrElse`.