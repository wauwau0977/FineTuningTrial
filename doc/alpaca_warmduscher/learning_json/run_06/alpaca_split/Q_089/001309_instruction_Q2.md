For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/DateTimeConfig.java' with name 'DateTimeConfig.java'... 
Consider the following section of code:
```java
private static final DateTimeFormatter dateFormat = DateTimeFormatter.ISO_DATE;
private static final DateTimeFormatter dateTimeFormat = DateTimeFormatter.ISO_DATE_TIME;
```
What are the advantages of using `DateTimeFormatter.ISO_DATE` and `DateTimeFormatter.ISO_DATE_TIME` instead of defining custom date/time patterns (e.g., "yyyyMMdd" or "yyyy-MM-dd HH:mm:ss") directly? What potential issues might arise if you were to switch to custom patterns?