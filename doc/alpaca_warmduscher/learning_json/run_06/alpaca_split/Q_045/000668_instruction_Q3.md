For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/Profiles.java' with name 'Profiles.java' where below a part of it is displayed... 
```java
public class Profiles {
   public static final String DEFAULT = "default";
   /**
    * use a mock implementation instead of the real modbus or the real service.
    */
   public static final String SENSOR_MOCK = "sensormock";
```
The comment above `SENSOR_MOCK` explains its purpose. How might this constant be *used* within the application to enable or disable mock sensor data? Provide a conceptual example.