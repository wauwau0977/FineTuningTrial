For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/services/info/InfoService.java' with name 'InfoService.java' where below a part of it is displayed...
```java
   @RequestMapping("/memory")
   @ResponseBody
   public MemoryInfo getMemoryInfo() {
       return MemoryInfo.getCurrent();
   }
```
Explain what the `@RequestMapping` and `@ResponseBody` annotations do in this method, and how they contribute to building a RESTful API.