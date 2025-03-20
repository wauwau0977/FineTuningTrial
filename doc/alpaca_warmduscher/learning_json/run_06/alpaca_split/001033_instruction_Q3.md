For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/device/service/HeatingDataPoller.java' with name 'HeatingDataPoller.java' where below a part of it is displayed...
```java
@Component
public class HeatingDataPoller {
   private final Logger log = LoggerFactory.getLogger(this.getClass());
   private final HeatingDataReadService heatingDataReadService;
   private final HeatPumpRepository heatPumpRepository;
   public HeatingDataPoller(HeatingDataReadService heatingDataReadService, HeatPumpRepository heatPumpRepository) {
       this.heatingDataReadService = heatingDataReadService;
       this.heatPumpRepository = heatPumpRepository;
   }
   // ... rest of the code
}
```
What is the purpose of the `@Component` annotation and the constructor in this code snippet? Explain how these elements contribute to the Spring framework's dependency injection mechanism.