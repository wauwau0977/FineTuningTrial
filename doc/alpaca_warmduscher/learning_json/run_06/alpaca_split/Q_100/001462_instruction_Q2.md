For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/services/meteoswiss/MeteoSwissService.java' with name 'MeteoSwissService.java'... 
Consider the following code snippet from the `getBetweenDates` method:

```java
if (groupEveryNthSecond > 0 && maxRows > 0) {
    throw new ThException("Either supply 'groupEveryNthSecond' or 'maxRows' as a param. Both is not possible");
}
if (groupEveryNthSecond < 0 && maxRows < 0) {
    throw new ThException("At least supply one limiting criteria, either 'groupEveryNthSecond' or 'maxRows' as a param.");
}
```

What is the purpose of these two `if` statements? Explain the business logic they implement and why this validation is necessary. What would happen if these checks were removed, and what potential issues could arise?