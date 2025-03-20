For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/services/info/InfoService.java' with name 'InfoService.java'... 
Considering the `getMemoryInfo()` method:
```java
@RequestMapping("/memory")
@ResponseBody
public MemoryInfo getMemoryInfo() {
    return MemoryInfo.getCurrent();
}
```
What are the potential drawbacks of directly calling a static method like `MemoryInfo.getCurrent()` within a controller method, especially in a production environment, and what alternatives might you consider?