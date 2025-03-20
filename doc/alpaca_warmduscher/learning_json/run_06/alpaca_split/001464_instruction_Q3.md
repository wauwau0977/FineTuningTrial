For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/services/meteoswiss/MeteoSwissService.java' with name 'MeteoSwissService.java' where below a part of it is displayed...
```java
   @RequestMapping("/getBetweenDates")
   @ResponseBody
   public List<MeteoSwissStatisticsEntity> getBetweenDates(
           @RequestParam(name = "start") Date start,
           @RequestParam(name = "end") Date end,
           @RequestParam(name = "maxRows", required = false, defaultValue = "-1") int maxRows,
           @RequestParam(name = "groupEveryNthSecond", required = false, defaultValue = "-1") int groupEveryNthSecond,
           @RequestParam(name = "stationIdList", required = false) Set<String> stationIdList
   ) throws Exception {
       // ... (code omitted) ...
   }
```
What are the input parameters of the `getBetweenDates` method, which parameters are required, and what are the default values for the optional parameters?