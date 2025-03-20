For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/services/heating/HeatPumpDataService.java' with name 'HeatPumpDataService.java' where below a part of it is displayed...
```java
   @RequestMapping("/lastValues")
   @ResponseBody
   public List<HeatPumpEntity> lastValues(
           @RequestParam(name = "maxRows", required = false, defaultValue = "1500") int maxRows
   ) throws Exception {
       return heatPumpRepository.getLastEntries(maxRows);
   }
```
What is the purpose of the `@RequestParam` annotation in the `lastValues` method, and how does it affect the method's behavior? Explain the meaning of `required = false` and `defaultValue = "1500"`.