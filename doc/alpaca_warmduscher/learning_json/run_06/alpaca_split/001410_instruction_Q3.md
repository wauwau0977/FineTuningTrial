For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/services/heating/HeatPumpDataService.java' with name 'HeatPumpDataService.java' where below a part of it is displayed...
```java
@RequestMapping("/scanRegisters")
@ResponseBody
public List<String> scanRegisters(
        @RequestParam(name = "maxRegister", defaultValue = "510", required = false) int maxRegister) {
    return heatingDataReadService.scanAllRegisters(maxRegister);
}
```
What is the role of the `heatingDataReadService` in this `scanRegisters` method?  Describe what the method does overall, and how the `@RequestParam` annotation affects the execution.