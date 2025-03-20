For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/Utils.java' with name 'Utils.java' where below a part of it is displayed... 
```java
public static LocalDateTime convertUTCToSwitzerlandTime(LocalDateTime dateTime) {
    if (dateTime == null) {
        return null;
    }
    return dateTime.atZone(ZoneId.of("UTC")).withZoneSameInstant(ZoneId.of("Europe/Zurich")).toLocalDateTime();
}
```
Explain the purpose of this method and describe how it converts a `LocalDateTime` object from UTC to Switzerland time. Break down each step of the conversion process.