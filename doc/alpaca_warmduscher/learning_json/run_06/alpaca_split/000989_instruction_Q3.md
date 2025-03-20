For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/entity/audit/AuditLogEntity.java' with name 'AuditLogEntity.java' where below a part of it is displayed... 
```java
@Entity(name = "AUDIT_LOG_ENTITY")
@Table(indexes = {
       @Index(name = "AUDIT_LOG_IX_1", columnList = "createDate"),
})
public class AuditLogEntity {
```
What is the purpose of the `@Entity` and `@Table` annotations in this code, and how does the `@Index` annotation contribute to database performance?