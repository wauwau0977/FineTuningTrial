For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/data/meteoswiss/impl/MeteoDataMockImpl.java' with name 'MeteoDataMockImpl.java' where below a part of it is displayed...

```java
   private final Logger log = LoggerFactory.getLogger(this.getClass());
   private final long t0 = System.currentTimeMillis() - 1;
```

What is the purpose of initializing `t0` to `System.currentTimeMillis() - 1`? How might this value be used later in the `getData()` method, and what effect does subtracting 1 have?