For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/entity/SessionDevice.java' with name 'SessionDevice.java' where below a part of it is displayed... 
```java
   private String sessionId;
   private String clientId;
   private Date sessionCreateDate = new Date();
   private String agentString;
   private String ip;
```
What is the significance of initializing `sessionCreateDate` with `new Date()`? What potential issues could arise from this approach?