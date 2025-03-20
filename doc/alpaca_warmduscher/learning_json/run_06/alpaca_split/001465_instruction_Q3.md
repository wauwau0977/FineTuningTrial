For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/services/meteoswiss/MeteoSwissService.java' with name 'MeteoSwissService.java' where below a part of it is displayed...
```java
if (groupEveryNthSecond > 0 && maxRows > 0) {
    throw new ThException("Either supply 'groupEveryNthSecond' or 'maxRows' as a param. Both is not possible");
}
if (groupEveryNthSecond < 0 && maxRows < 0) {
    throw new ThException("At least supply one limiting criteria, either 'groupEveryNthSecond' or 'maxRows' as a param.");
}
```
What is the purpose of these two `if` statements within the `getBetweenDates` method? Explain the validation logic they implement.