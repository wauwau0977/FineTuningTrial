For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/entity/audit/AuditLogEntity.java' with name 'AuditLogEntity.java' where below a part of it is displayed...
```java
@Lob
@Type(type = "org.hibernate.type.TextType")
private String message;
@Lob
@Type(type = "org.hibernate.type.TextType")
private String detail;
```
What is the purpose of the `@Lob` and `@Type` annotations used for the `message` and `detail` fields, and why are they necessary?