For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/cache/CachingConfig.java' with name 'CachingConfig.java' where below a part of it is displayed...

```java
@Configuration
@EnableCaching
public class CachingConfig {
   @Bean
   public CacheManager cacheManager() {
       return new ConcurrentMapCacheManager("sessionDeviceCache");
   }
}
```

What is the purpose of the `@EnableCaching` annotation in this configuration class, and how does it relate to the `@Bean` definition for `cacheManager()`?