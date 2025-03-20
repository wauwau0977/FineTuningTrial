For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/services/info/bean/MemoryInfo.java' with name 'MemoryInfo.java' where below a part of it is displayed...
```java
public static MemoryInfo getCurrent() {
    MemoryInfo memoryInfo = new MemoryInfo();
    final int kB = 1024;
    memoryInfo.setFreeMemoryKb(Runtime.getRuntime().freeMemory() / kB);
    memoryInfo.setTotalMemoryKb(Runtime.getRuntime().totalMemory() / kB);
    memoryInfo.setMaxMemoryKb(Runtime.getRuntime().maxMemory() / kB);
    memoryInfo.setAvailableProcessors(Runtime.getRuntime().availableProcessors());
    return memoryInfo;
}
```
Explain the role of the `final int kB = 1024;` line within the `getCurrent()` method, and why it is necessary.