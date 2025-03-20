For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/services/heating/HeatPumpDataService.java' with name 'HeatPumpDataService.java' where below a part of it is displayed...
```java
 @RequestMapping("/getBetweenDates")
 @ResponseBody
 public List<HeatPumpStatisticsEntity> getBetweenDates(
         @RequestParam(name = "start") Date start,
         @RequestParam(name = "end") Date end,
         @RequestParam(name = "maxRows", required = false, defaultValue = "-1") int maxRows,
         @RequestParam(name = "groupEveryNthSecond", required = false, defaultValue = "-1") int groupEveryNthSecond
 ) throws Exception {
     if (groupEveryNthSecond > 0 && maxRows > 0) {
         throw new ThException("Either supply 'groupEveryNthSecond' or 'maxRows' as a param. Both is not possible");
     }
     // ... more code ...
 }
```
Explain the purpose of the conditional statement `if (groupEveryNthSecond > 0 && maxRows > 0)` within the `getBetweenDates` method. What issue does it address, and what exception is thrown if the condition is met?