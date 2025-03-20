For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/mutex/GlobalSynced.java' with name 'GlobalSynced.java' where below a part of it is displayed...

```java
private final ReentrantLock reentrantLock = new ReentrantLock();
```

Explain the purpose of `ReentrantLock` in this code. Why is a `ReentrantLock` used rather than a simpler synchronization mechanism like `synchronized`? What benefits does `ReentrantLock` provide in the context of `GlobalSynced`?