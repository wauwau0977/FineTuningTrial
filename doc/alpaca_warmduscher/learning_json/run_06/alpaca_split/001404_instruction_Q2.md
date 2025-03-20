For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/services/heating/HeatPumpDataService.java' with name 'HeatPumpDataService.java'... 
Consider the following method snippet:

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
       // ... rest of the method
   }
```

What is the purpose of the conditional statement `if (groupEveryNthSecond > 0 && maxRows > 0)`? Explain the reasoning behind preventing both parameters from being supplied simultaneously. What potential issue would arise if both parameters were allowed?